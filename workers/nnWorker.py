import PySide2.QtCore as QtC
import torch
from torch.nn.functional import interpolate
from collections import deque
from pathlib import Path
from PIL import Image as PILImage
from torchvision.transforms import Normalize, ToTensor
import torchvision.transforms.functional as TF
from tensorrt_utils import TRTModule
from .daemonWorker import DaemonWorker


class NNWorker(DaemonWorker):
    inferenceComplete = QtC.Signal(torch.Tensor, torch.Tensor, torch.Tensor, int, int, str)


    def __init__(self, daemonWidget=None, parent=None):
        super(NNWorker, self).__init__(daemonWidget=daemonWidget, parent=parent)
        self.config = daemonWidget.mainWindow.config
        self.n_cut = len(self.config.IMAGE.IMAGE_CROP_ANCHORS)
        self.crop_coords = [[
            self.config.IMAGE.IMAGE_CROP_ANCHORS[i][1],
            self.config.IMAGE.IMAGE_CROP_ANCHORS[i][0],
            self.config.IMAGE.IMAGE_SIZE[1],
            self.config.IMAGE.IMAGE_SIZE[0],
        ] for i in range(self.n_cut)]
        self.valid_categories = self.config.NEURAL_NETWORK.VALID_CATEGORIES
        self.model = TRTModule(Path.cwd() / self.config.NEURAL_NETWORK.ENGINE_PATH)
        self.tensor_converter = ToTensor()
        self.normalizer = Normalize(
            mean=self.config.NEURAL_NETWORK.IMAGE_MEAN,
            std=self.config.NEURAL_NETWORK.IMAGE_STD,
        )
        self.queue = deque()
        self.calculateRoiCropbox()

    def calculateRoiCropbox(self):
        self.image_roi = self.config.IMAGE.IMAGE_ROI
        self.image_size = self.config.IMAGE.IMAGE_SIZE
        zero_mask = torch.zeros((1, self.image_size[1], self.image_size[0]), dtype=torch.float32)

        if self.image_roi[0] > 0:
            self.left_mask = TF.crop(zero_mask, 0, 0, self.image_size[1], self.image_roi[0])
        else:
            self.left_mask = None
        if self.image_roi[0] + self.image_roi[2] < self.image_size[0]:
            self.right_mask = TF.crop(zero_mask, 0, self.image_roi[0] + self.image_roi[2],
                                  self.image_size[1], self.image_size[0] - self.image_roi[0] - self.image_roi[2])
        else:
            self.right_mask = None
        if self.image_roi[1] > 0:
            self.top_mask = TF.crop(zero_mask, 0, self.image_roi[0], self.image_roi[1], self.image_roi[2])
        else:
            self.top_mask = None
        if self.image_roi[1] + self.image_roi[3] < self.image_size[1]:
            self.bottom_mask = TF.crop(zero_mask, self.image_roi[1] + self.image_roi[3], self.image_roi[0],
                                   self.image_size[1] - self.image_roi[1] - self.image_roi[3], self.image_roi[2])
        else:
            self.bottom_mask = None

        self.cropbox_roi = [self.image_roi[1], self.image_roi[0], self.image_roi[3], self.image_roi[2]]

    def concatenate(self, roi, scale_factor=1):
        cat_list = []
        if self.top_mask is not None:
            cat_list.append(
                self.top_mask.to(roi.device)
                if scale_factor == 1 else
                interpolate(self.top_mask, scale_factor=scale_factor, mode='nearest').to(roi.device)
            )
        cat_list.append(roi)
        if self.bottom_mask is not None:
            cat_list.append(
                self.bottom_mask.to(roi.device)
                if scale_factor == 1 else
                interpolate(self.bottom_mask, scale_factor=scale_factor, mode='nearest').to(roi.device)
            )
        roi = torch.cat(cat_list, dim=1)
        cat_list = []
        if self.left_mask is not None:
            cat_list.append(
                self.left_mask.to(roi.device)
                if scale_factor == 1 else
                interpolate(self.left_mask, scale_factor=scale_factor, mode='nearest').to(roi.device)
            )
        cat_list.append(roi)
        if self.right_mask is not None:
            cat_list.append(
                self.right_mask.to(roi.device)
                if scale_factor == 1 else
                interpolate(self.right_mask, scale_factor=scale_factor, mode='nearest').to(roi.device)
            )
        result = torch.cat(cat_list, dim=2)

        return result

    @QtC.Slot(str)
    def enqueueImage(self, image_path):
        self.queue.append(image_path)
        self.sendText.emit("接收到岩渣图像'{img_name}'，正在处理中...".format(img_name=Path(image_path).name), 1000, 1)
        self.processNextImage()

    @QtC.Slot()
    def processNextImage(self):
        if self.queue:
            image_path = self.queue.popleft()
            self.nnInference(image_path)

    def nnInference(self, image_path):
        img = PILImage.open(image_path).convert('L')
        img = self.tensor_converter(img)
        for i in range(self.n_cut):
            _img = TF.crop(img, *self.crop_coords[i])
            _img_input = self.normalizer(TF.crop(_img, *self.cropbox_roi)).unsqueeze(0).cuda()
            out = self.model(_img_input)
            if out[2].item() in self.valid_categories:
                self.inferenceComplete.emit(
                    _img,
                    self.concatenate(out[0].squeeze(0).cpu()),
                    self.concatenate(out[1].squeeze(0).cpu()),
                    out[2].item(),
                    out[3].item(),
                    Path(Path(image_path).parent / f"{Path(image_path).stem}_{i}{Path(image_path).suffix}").as_posix()
                )

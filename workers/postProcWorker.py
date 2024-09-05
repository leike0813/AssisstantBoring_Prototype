import PySide2.QtCore as QtC
import numpy as np
import datetime
import re
import torch
from collections import deque
from pathlib import Path
from .daemonWorker import DaemonWorker
from .postProcUtil import *


class PostProcWorker(DaemonWorker):
    plotMuckImage = QtC.Signal(np.ndarray)
    plotMuckParameter = QtC.Signal(float, list)
    sendRockGrade = QtC.Signal(int)


    def __init__(self, daemonWidget=None, parent=None):
        super(PostProcWorker, self).__init__(daemonWidget=daemonWidget, parent=parent)
        self.config = daemonWidget.mainWindow.config
        self.contour_extractor = ContourExtractor(
            kernel_shape=self.config.POST_PROCESSING.kernel_shape,
            kernel_size=self.config.POST_PROCESSING.kernel_size,
            **self.config.POST_PROCESSING.EXTRACTOR
        )
        self.statistical_analyzer = StatisticalAnalyzer(
            kernel_shape=self.config.POST_PROCESSING.kernel_shape,
            kernel_size=self.config.POST_PROCESSING.kernel_size,
            **self.config.POST_PROCESSING.STATISTICAL
        )
        self.visualizer = Visualizer(
            **self.config.POST_PROCESSING.VISUALIZATION
        )

        self.cur_cycle_begin = datetime.datetime.now()
        self.queue = deque()
        self.creationTimeRegExp = re.compile(self.config.IMAGE.CREATION_TIME_REGEXP)

    @QtC.Slot(torch.Tensor, torch.Tensor, torch.Tensor, int, int, str)
    def enqueueImage(self, orig_image, boundary_mask, region_mask, category, grade, img_path):
        self.queue.append((orig_image, boundary_mask, region_mask, category, grade, img_path))
        self.sendRockGrade.emit(grade)
        self.processNextImage()

    @QtC.Slot()
    def processNextImage(self):
        if self.queue:
            image_info = self.queue.popleft()
            self.processImage(*image_info)

    def processImage(self, orig_image, boundary_mask, region_mask, category, grade, image_path):
        contour_dict = self.contour_extractor(orig_image, boundary_mask, region_mask)
        image_size = (orig_image.shape[-2], orig_image.shape[-1])
        contour_dict, statistic_dict, grain_dist_dict, grain_dist_parameters = self.statistical_analyzer(
            contour_dict, image_size)
        result_image, orig_image = self.visualizer(orig_image, contour_dict, statistic_dict, grain_dist_dict,
                                     grain_dist_parameters)

        self.sendText.emit("岩渣图像'{img_name}'处理完毕。".format(img_name=Path(image_path).name), 1000, 1)
        self.plotMuckImage.emit(result_image)
        self.plotMuckParameter.emit(
            self.timeParser(image_path),
            [
                statistic_dict['volume']['total'] / 1e9,
                grain_dist_parameters['area']['D50'],
                grain_dist_parameters['area']['Cu'],
                grain_dist_parameters['area']['Cc'],
                grain_dist_parameters['area']['CI'],
            ]
        )

    def timeParser(self, img_path):
        time_str = self.creationTimeRegExp.findall(Path(img_path).stem)
        creation_time = datetime.datetime.strptime(time_str[0][0] + time_str[0][1], '%y%m%d%H%M%S%f')
        if Path(img_path).stem.endswith('0'):
            return (creation_time - self.cur_cycle_begin).total_seconds()
        elif Path(img_path).stem.endswith('1'):
            return (creation_time - self.cur_cycle_begin + datetime.timedelta(milliseconds=10)).total_seconds()
        else:
            raise NotImplementedError
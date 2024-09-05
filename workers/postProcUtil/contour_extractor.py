import numpy as np
import pandas as pd
import cv2
import torch
from .pproc_functions import (
    calculate_valid_contours,
)
from .pproc_enums import *
from cv_utils import (
    torch2cv,
    global2part_contour,
    global2part_image,
    filter_lowerbound,
)


class ContourExtractor:
    def __init__(self, region_prob_thresh=0.45, boundary_prob_shift=0.1, center_prob_thresh=0.8, center_open_iter=1,
                 erosion_mode='iterative', max_erosion_iter=5, center_rel_dist_thresh=3.0,
                 gaussian_kernel_size=15, kernel_shape='ellipse', kernel_size=3, apply_stage2=False):
        self.region_prob_thresh = region_prob_thresh
        self.boundary_prob_shift = boundary_prob_shift
        self.center_prob_thresh = center_prob_thresh
        self.center_open_iter = center_open_iter
        self.erosion_mode = getattr(ErosionMode, erosion_mode.capitalize(), ErosionMode.Iterative)
        self.max_erosion_iter = max_erosion_iter
        self.center_rel_dist_thresh = center_rel_dist_thresh
        self.gaussian_kernel_size = gaussian_kernel_size
        kernel_shape = getattr(KernelShape, kernel_shape.capitalize(), KernelShape.Ellipse)
        self.kernel = cv2.getStructuringElement(kernel_shape, (kernel_size, kernel_size))
        self.apply_stage2 = apply_stage2


    def __call__(self, orig_image: torch.Tensor, boundary_pred: torch.Tensor, region_pred: torch.Tensor):
        orig_image = torch2cv(orig_image)
        orig_image_watershed = (cv2.GaussianBlur(orig_image, (self.gaussian_kernel_size, self.gaussian_kernel_size), 0)\
                               * (1. - torch2cv(boundary_pred.squeeze(0), convert_value=False))).astype(np.uint8)

        region_subtract = torch2cv(self.get_subtracted(boundary_pred, region_pred).squeeze(0), convert_value=False)
        contour_dict = self.extract_and_separate_contours(region_subtract, orig_image_watershed)

        return contour_dict

    def get_subtracted(self, boundary_pred, region_pred):
        return filter_lowerbound(
            region_pred - (boundary_pred - self.region_prob_thresh - self.boundary_prob_shift).clip(0, 1),
            self.region_prob_thresh,
        )

    def extract_and_separate_contours(self, region_subtract, orig_image):
        region_mask = (region_subtract > self.region_prob_thresh).astype(np.uint8)
        contours, _ = cv2.findContours(region_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contour_infos = []
        for contour in contours:
            if contour.shape[0] > 2:  # filter out the illegal coutours
                bbox = cv2.boundingRect(contour)
                part_contour = global2part_contour([contour], bbox)[0]
                part_region_subtract = global2part_image(region_subtract, bbox)
                # part_region_mask = global2part_image(region_mask, bbox)
                part_region_mask = np.zeros((bbox[3], bbox[2]), dtype=np.uint8)
                cv2.fillPoly(part_region_mask, [part_contour], 1)
                part_region_subtract *= part_region_mask
                if self.apply_stage2:
                    part_orig_image = global2part_image(orig_image, bbox)
                    part_orig_image = cv2.cvtColor(part_orig_image, cv2.COLOR_GRAY2BGR)
                else:
                    part_orig_image = None

                contour_infos.append(calculate_valid_contours(
                    part_contour, part_region_subtract, part_region_mask, bbox, part_orig_image, self.center_prob_thresh,
                    self.center_open_iter, self.max_erosion_iter, self.erosion_mode, self.kernel, self.center_rel_dist_thresh
                ))

        contour_dict = pd.DataFrame(columns=['id', 'points', 'bbox', 'center'])
        contour_dict.set_index('id', drop=True, inplace=True)
        contour_count = 0
        for sep_contour in contour_infos:
            for c in sep_contour:
                contour_dict.loc[contour_count] = [c[0], c[2], c[1]]
                contour_count += 1

        return contour_dict

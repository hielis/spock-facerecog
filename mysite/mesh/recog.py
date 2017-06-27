import sys
import os
import dlib
import glob
import numpy as np
from skimage import io
import math

predictor_path = "shape_detector.dat"
list_of_points[1, 2, 3]; #list here the interesting features

alpha = 0.3926
ratio_mm_pix_x = 0.3
ratio_mm_pix_y = 0.3
focal_length = 35
b = 2

x_0 = 13 * ratio_mm_pix_x
y_0 = 13 * ratio_mm_pix_y

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


def funct(f):
    print("Processing file: {}".format(f))
    img = io.imread(f)
    win.clear_overlay()
    win.set_image(img)
    dets = detector(img, 1)
    for k, d in enumerate(dets):
        shape = predictor(img, d)
        l = [shape.part(i) for i in list_of_points]
        return l

def solve_system(x_r, y_r, x_l, y_l):
    delta_x_l = (x_l - x_0)/focal_length
    delta_y_l = (y_l - y_0)/focal_length
    delta_x_r = (x_r - x_0)/focal_length
    delta_y_r = (y_r - y_0)/focal_length

    b = np.array([b * delta_x_l, b * delta_y_l, b * delta_x_r])
    a = np.array([[ (delta_x_l - 1) * math.cos(alpha), 0, (delta_x_l + 1) * math.sin(alpha)],
                  [ (delta_y_l) * math.cos(alpha),-1, (delta_y_l) * math.sin(alpha)],
                  [ (delta_x_r - 1) * math.cos(alpha), 0, (delta_x_r + 1) * math.sin(alpha)]])
    return np.linealg.solve(a, b)

def solve(x_r, y_r, x_l, y_l):
    x_r_p = x_l * ratio_mm_pix_x
    y_r_p = y_r * ratio_mm_pix_y
    x_l_p = x_l * ratio_mm_pix_x
    y_r_p = y_r * ratio_mm_pix_y
    return solve_system(x_r_p, y_r_p, x_l_p, y_l_p)

import sys
import os
import dlib
import glob
from skimage import io

predictor_path = ""
list_of_points[1, 2, 3]; #list here the interesting features


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

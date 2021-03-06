import sys
import os
import dlib
import glob
import numpy as np
from skimage import io, color
import math
import argparse
from PIL import ImageFile, Image
ImageFile.LOAD_TRUNCATED_IMAGES = True
#io.use_plugin('test', 'imshow')
predictor_path = "/home/hielis/dev/web/spock-facerecog/mysite/shape_detector.dat"
list_of_points = [1, #ear left
				8, #chin
				16, #ear right
				28, # upper part of the nose
				30,
				18,#eyebrow left
				21,
				23,#eyebrow right
				26,
				31,
				34,
				37,#eye left
				41,
				43,#eye right
				47,
				49,
				54,
				59]; #list here the interesting features

alpha = 0.3926
ratio_mm_pix_x = 4.44
ratio_mm_pix_y = 4.44
focal_length = 35
b = 2*ratio_mm_pix_x

x_0 = 399 * ratio_mm_pix_x
y_0 = 313 * ratio_mm_pix_y

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


def funct(f):
    #print("Processing file: {}".format(f))
    img = Image.open(f).convert('RGB')
    imgp = np.array(img)
    dets = detector(imgp, 1)
    l = []
    #print len(dets)
    for k, d in enumerate(dets):
        shape = predictor(imgp, d)
        l = [shape.part(i) for i in list_of_points]
    return l

def solve_system(x_r, y_r, x_l, y_l):
	delta_x_1 = (x_r - x_0) / (2 * focal_length)
	delta_x_2 = (x_l - x_0) / (2 * focal_length)
	delta_y_1 = (y_r - y_0) / (2 * focal_length)
	delta_y_2 = (y_l - y_0) / (2 * focal_length)
	x = - (b / (2 * focal_length * math.cos(alpha))) * (delta_x_1*(1 - (delta_x_1 / focal_length)) + delta_x_2*(1 - (delta_x_2 / focal_length)))
	z = (b / (2 * focal_length * math.sin(alpha))) * (delta_x_1*(1 - (delta_x_1 / focal_length)) - delta_x_2*(1 - (delta_x_2 / focal_length)))
	y =  - (delta_y_1 * b / focal_length) * (1 - (1 / focal_length)*(1 / ((delta_x_1 / focal_length) - 1)))
	print (x, y, z) 
	return (x, y, z) 

def solve(x_r, y_r, x_l, y_l):
    x_r_p = x_r * ratio_mm_pix_x
    y_r_p = y_r * ratio_mm_pix_y
    x_l_p = x_l * ratio_mm_pix_x
    y_l_p = y_r * ratio_mm_pix_y
    (x, y, z) = (solve_system(x_r_p, y_r_p, x_l_p, y_l_p))
    return (x*(1/ratio_mm_pix_y), y*(1/ratio_mm_pix_y), z*(1/ratio_mm_pix_y))

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("filename_r")
	parser.add_argument("filename_l")

	arg = parser.parse_args()
	l_r = funct(arg.filename_r)
	l_l = funct(arg.filename_l)
	p = 11
	pair = [l_r[p].x, l_r[p].y, l_l[p].x, l_l[p].y]
	print pair
	#print "Solution"
	print solve(pair[0], pair[1], pair[2], pair[3])
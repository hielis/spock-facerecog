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
list_of_points = range(18, 65)#list here the interesting features

q = 8
alpha = math.pi / q
ratio_mm_pix_x = 0.45
ratio_mm_pix_y = 0.73
r = 210
focal_length = 1
b = 1

x_0 = 450
y_0 = 300

x0p = (1 / (2 * (ratio_mm_pix_x*math.cos(alpha))))
y0p = (1 / (2 * (ratio_mm_pix_y*math.sin(alpha))))

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor(predictor_path)


def funct(f):
    #print("Processing file: {}".format(f))
    img = Image.open(f).convert('RGB')
    #width, height = img.size
  
    #print x_0, y_0
    imgp = np.array(img)
    dets = detector(imgp, 1)
    l = []
    #print len(dets)
    for k, d in enumerate(dets):
        shape = predictor(imgp, d)
        l = [shape.part(i) for i in list_of_points]
    return l

def solve_system(x_r, y_r, x_l, y_l):
	delta_x_1 = (x_r - x_0)
	delta_x_2 = (x_l - x_0)
	delta_y_1 = (y_r - y_0)
	delta_y_2 = (y_l - y_0)
	print (delta_x_1 ,delta_x_2, delta_y_1, delta_y_2)

	x = (1 / (2 * (ratio_mm_pix_x*math.cos(alpha)))) * (delta_x_1 + delta_x_2)
	z =  - (1 / (2 * (ratio_mm_pix_y*math.sin(alpha)))) * (delta_x_1 - delta_x_2)
	y = - delta_y_1
	#print (x, y, z) 
	return (x, y, z) 

def solve(x_r, y_r, x_l, y_l):
    x_r_p = x_r
    y_r_p = y_r
    x_l_p = x_l
    y_l_p = y_l
    (x, y, z) = (solve_system(x_r_p, y_r_p, x_l_p, y_l_p))
    return (x, y, z)

def to_list_of_results(f1, f2):
	l_r = funct(f1)
	l_l = funct(f2)
	res = []
	for a, b in zip(l_r, l_l):
		c = solve(a.x, a.y, b.x, b.y)
		res.append({'x' : (c[0]+x0p)*ratio_mm_pix_x/r, 'y' : (c[1] + y0p)*ratio_mm_pix_y/r , 'z' : (c[2] + x0p)/r})
	return res



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
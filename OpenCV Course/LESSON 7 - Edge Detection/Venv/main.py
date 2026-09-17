import os 
import numpy as np
import cv2

img = cv2.imread(os.path.join('.','Data', 'taekwondo.jpg'))
img_resize = cv2.resize(img, None, fx = 0.1, fy = 0.1)
img_edge = cv2.Canny(img_resize, 100, 200)
img_edge_dilate = cv2.dilate(img_edge, np.ones((3,3), dtype = np.int8))
img_edge_erode = cv2.erode(img_edge_dilate, np.ones((3,3), dtype = np.int8))


cv2.imshow('img_resize', img_resize)
cv2.imshow('img_edge', img_edge)
cv2.imshow('img_edge_dilate', img_edge_dilate)
cv2.imshow('img_edge_erode', img_edge_erode)

cv2.waitKey(0)
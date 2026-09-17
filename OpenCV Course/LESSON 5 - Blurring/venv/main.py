import os

import cv2

img = cv2.imread(os.path.join('.','Data', 'Kucing1.jpg'))

k_size = 7 
img_blur = cv2.blur(img, (k_size, k_size))
img_gaussian_blur = cv2.GaussianBlur(img, (k_size, k_size), 5)
img_medium_blur = cv2.medianBlur(img, k_size)

cv2.imshow('img', img)
cv2.imshow('img_blur', img_blur)
cv2.imshow('img_gaussian_blur', img_gaussian_blur)
cv2.imshow('img_medium_blur', img_medium_blur)

cv2.waitKey(0)
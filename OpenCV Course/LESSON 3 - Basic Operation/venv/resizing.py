# resizing
import os

import cv2 

img = cv2.imread(os.path.join('.','Data','Kucing2.jpg'))

resized_img = cv2.resize(img, (640, 380))

print(resized_img.shape)
print (img.shape)

cv2.imshow('img', img)
cv2.imshow('resized_img', resized_img)
cv2.waitKey(0)

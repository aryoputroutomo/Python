# crop
import os

import cv2 

img = cv2.imread(os.path.join('.','Data', 'Kucing1.jpg'))

print(img.shape)

cropped_img = img[100:300, 150:400]

cv2.imshow('img', img)
cv2.imshow('cropped_img', cropped_img)
cv2.waitKey(0)
import os 

import cv2 

img = cv2.imread(os.path.join('.', 'Data', 'Kucing2.jpg'))

cv2.imshow('img', img)
cv2.waitKey(0)
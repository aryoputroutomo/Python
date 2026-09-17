import os 

import cv2

img = cv2.imread(os.path.join('.','Data', 'papan tulis.jpg'))
print(img.shape)

# Line 
cv2.line(img, (62, 36), (300, 187), (0, 255, 0), 3)
print("cv2.line(img, (Titik awal garis dalam bentuk koordinat), (Titik akhir garis dalam bentuk koordinat),(Warna garis dalam format BGR (Blue, Green, Red)), Ketebalan garis")

# Rectangle
cv2.rectangle(img, (300, 187), (363, 248), (0,0,255), 5)
print("cv2.rectangle(img, (Koordinat sudut kiri atas), (Koordinat sudut kanan bawah), (warna), ketebalan")

Tes = cv2.rectangle(img, (400, 187), (463, 248), (0, 0, 255), -1)

# Circle
cv2.circle(img, (149, 239), 40, (255, 0, 0), 5)
print("cv2.circle(gambar, (koordinat titik puusat), jari jari, (warna), ketebalan)")

# Text
cv2.putText(img, 'Hallo Sayang', (308,100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
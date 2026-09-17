import cv2 as cv
import os

# Hapus tulisan PASTE_DI_SINI dan tekan Ctrl+V / Paste di dalam tanda kutip
path_manual = r"Data/papan tulis.jpg" 

if not os.path.exists(path_manual):
    print("Bahkan jalur manual pun salah. Coba cek lagi klik kanan 'Copy Path'-nya.")
else:
    img = cv.imread(path_manual)
    cv.namedWindow('Cek Koordinat')
    
    def cek_koordinat(event, x, y, flags, param):
        if event == cv.EVENT_LBUTTONDOWN:
            print(f"X = {x}, Y = {y}")
            
    cv.setMouseCallback('Cek Koordinat', cek_koordinat)
    cv.imshow('Cek Koordinat', img)
    cv.waitKey(0)
    cv.destroyAllWindows()

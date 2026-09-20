# Continue, Pass, Break

# Pass digunakan untuk melewati perintah di dalam loop, tidak akan di eksekusi dan akan melanjutkan ke perintah berikutnya. 
# sedangkan Continue digunakan untuk melanjutkan ke iterasi berikutnya dari loop. 
# Break digunakan untuk menghentikan loop sepenuhnya.


# Continue 
angka = 0 
print (f'angka sekarang adalah {angka}')

while angka < 10:
    angka += 1
    print (f'angka sekarang adalah {angka}')
    if angka == 5:
        print ('angka 5 ditemukan, lanjut ke iterasi berikutnya')
        print ('ini adalah perintah sebelum continue\n')
        continue # Akan membuat loop langsug ke atas tanpa mengeksekusi perintah di bawahnya
    print (f'hallo')
print ('selesai\n')

# Tanpa Continue
angka = 0 
print (f'angka sekarang adalah {angka}')

while angka < 10:
    angka += 1
    print (f'angka sekarang adalah {angka}')
    if angka == 5:
        print ('angka 5 ditemukan, lanjut ke iterasi berikutnya')
        print ('nice')
        
    print (f'hallo')
print ('selesai\n')

# Pass
angka = 0
print (f'angka sekarang adalah {angka}')
while angka < 10:
    angka += 1
    
    if angka == 5:
        print ('nice')
        pass # perintah kosong

    print (f'angka sekarang adalah {angka}')
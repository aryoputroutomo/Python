import random

angka_rahasia = random.randint (1, 30)
tebakan = 0 
jumlah_tebakan = 0

print ('Pikirkan angka antara 1 - 30')
while tebakan != angka_rahasia:
    tebakan = int(input("Masukkan angka tebakan = "))
    jumlah_tebakan += 1

    if tebakan < angka_rahasia:
        print ('terlalu rendah! Coba Lagi')
    elif tebakan > angka_rahasia:
        print ('terlalu tinggi! Coba Lagi')
    else:
        print (f"selamat kamu berhasil menebak, kamu menebak {jumlah_tebakan} kali")
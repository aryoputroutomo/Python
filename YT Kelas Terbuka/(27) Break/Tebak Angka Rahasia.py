
angka_rahasia = 7

while True:
    angka = int(input('Masukkan angka tebakan anda: '))

    if angka == angka_rahasia:
        print ('benar, anda berhasil menebak angka rahasia')
        break

    print('coba lagi, tebakan anda salah')
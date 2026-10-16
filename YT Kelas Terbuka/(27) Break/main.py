angka = 0 

while angka < 10:
    angka += 1
    print (f"angka sekarang: {angka}")

    if angka == 5:
        print ('assalammualaikum')
        break

    print('hallo')                                                                                

print('akhir dari program\n')

# TANPA BREAK
angka = 0 

while angka < 10:
    angka += 1
    print (f"angka sekarang: {angka}")

    if angka == 5:
        print ('assalammualaikum')

    print('hallo')                                                                                

print('akhir dari program\n')

# Digabung Input dan Break
data_int = int(input('masukkan angka: '))
angka = 0

while True:
    angka += 1
    print (f"angka sekarang: {angka}")

    if angka == data_int:
        print ('assalammualaikum')
        break

    print('hallo')                                                                                

print('akhir dari program\n')
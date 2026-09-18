usia = int(input('Usia = '))

if usia < 12:
    harga_tiket = 30000
elif usia <= 59:
    harga_tiket = 50000
else:
    harga_tiket = 35000

print(f'Harga Tiket = {harga_tiket}')
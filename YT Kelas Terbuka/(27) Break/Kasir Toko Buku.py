total_harga = 0
while True:
    tanya = input('Masukkan harga barang (ketik "selesai" untuk berhenti): ')

    if tanya == 'selesai':
        print ('pembelian selesai')
        break

    harga = int(tanya)
    total_harga += harga

    print(f'total harga sekarang: {total_harga}')
total_belanja = 0
print (5*'-', 'Sistem kasir toko ganteng ', 5*'-' )
print ('ketik "selesai" pada nama barang untuk menghitung total\n')

while True:
    nama_barang = input('Masukkan nama barang = ')
    if nama_barang.lower() == 'selesai':
        break

    harga_barang = int(input('masukkan harga barang = '))
    total_belanja += harga_barang

print ('-'*30)
print (f'total bayar = Rp{total_belanja:,.2f}')
print ('terimakasih sudah berbelanja')
target_tabungan = int(input('masukkan targeet tabungan = '))
jumlah_uang = 0
total_hari = 0

while True:
    uang = int(input('masukkan jumlah uang = '))
    jumlah_uang += uang
    total_hari += 1
    print (f'hari ke-{total_hari}: Rp{jumlah_uang:,}')
    if jumlah_uang >= target_tabungan:
        print (f'jumlah uang = {jumlah_uang}, target tercapai dalam {total_hari} hari')
        break

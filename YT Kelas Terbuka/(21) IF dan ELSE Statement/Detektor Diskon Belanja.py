total_belanja = 150000

if total_belanja > 100000:
    persen_diskon = 0.1
else:
    persen_diskon = 0

Nilai_Diskon = total_belanja * persen_diskon
Total_Bayar = total_belanja - Nilai_Diskon

print (f'Total Belanja = {total_belanja}')
print (f'Potongan Diskon = {Nilai_Diskon}')
print (f'Total Bayar = {Total_Bayar}')
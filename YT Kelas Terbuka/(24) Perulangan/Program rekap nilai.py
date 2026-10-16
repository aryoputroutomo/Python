jumlah_mahasiswa = int(input('Masukkan jumlah mahasiswa: '))
total_nilai = 0

for i in range (1, jumlah_mahasiswa + 1):
    nilai = float(input(f'Nilai mahasiswa {i}: '))
    total_nilai += nilai

    if nilai > 90:
        print('Nilai A')
    elif nilai > 80:
        print('Nilai B')
    elif nilai > 70:
        print('Nilai C')
    else:
        print('Nilai D')
    
    if i == 1:
        tertinggi = nilai
        terendah = nilai
    else:
        if nilai > tertinggi:
            tertinggi = nilai
        if nilai < terendah:
            terendah = nilai 

rata_rata = total_nilai / jumlah_mahasiswa

print (f'Total nilai dari {jumlah_mahasiswa} mahasiswa adalah: {total_nilai}')
print (f'Rata-rata nilai: {rata_rata}')
print (f'Nilai tertinggi: {tertinggi}')
print (f'Nilai terendah: {terendah}')
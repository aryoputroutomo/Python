# ==========================================
# PROGRAM INPUT HARGA MAKANAN ANAK UNDIP
# ==========================================
print('''
# Nama Kelompok : Kelompok 36
# Anggota & NIM : 
21120126140130	NENZA ADITYA PERMANA PUTRA
21120126120012	HANIFAH KEISHA DIANANDA DEWI
21120126130060	ASHFA RIZQUNA
21120126120019	ARYO PUTRO UTOMO
# Kelompok      : 36
# Shift         : Shift 6
''')
# ==========================================

nama = ["Aryo", "Nenza", "Hanifah", "Ashfa"]

harga = []
porsi = []

total_harga = 0
total_porsi = 0

for i in range(len(nama)):
    print("\nData", nama[i])

    h = int(input("Masukkan harga makanan : Rp "))
    p = int(input("Masukkan jumlah porsi  : "))

    harga.append(h)
    porsi.append(p)

    total_harga += h * p
    total_porsi += p

rata_rata = total_harga / total_porsi

print("\n==========================================")
print("           HASIL PERHITUNGAN")
print("==========================================")

for i in range(len(nama)):
    print(nama[i], ":",
          harga[i], "x", porsi[i],
          "=", harga[i] * porsi[i])

print("------------------------------------------")
print("Total harga belanjaan  : Rp", total_harga)
print("Total seluruh porsi    :", total_porsi)
print("Rata-rata biaya/porsi  : Rp", rata_rata)
print("==========================================")
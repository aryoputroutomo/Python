# ==========================================
# PROGRAM PENJUMLAHAN MATRIKS 2x3
# ==========================================

print('''
# =========================================
# Nama Kelompok : Kelompok 36
# Anggota & NIM : 
21120126140130	NENZA ADITYA PERMANA PUTRA
21120126120012	HANIFAH KEISHA DIANANDA DEWI
21120126130060	ASHFA RIZQUNA
21120126120019	ARYO PUTRO UTOMO
# Kelompok      : 36
# Shift         : Shift 6
# =========================================
''')

# Matriks stok shift pagi
pagi = [
    [10, 15, 20],
    [25, 30, 35]
]

# Matriks stok shift sore
sore = [
    [5, 10, 15],
    [10, 20, 25]
]

# Proses penjumlahan kedua matriks
hasil = [
    [pagi[0][0] + sore[0][0],
     pagi[0][1] + sore[0][1],
     pagi[0][2] + sore[0][2]],

    [pagi[1][0] + sore[1][0],
     pagi[1][1] + sore[1][1],
     pagi[1][2] + sore[1][2]]
]

# Menampilkan matriks
print("\nStok Shift Pagi:")
for baris in pagi:
    print(baris)

print("\nStok Shift Sore:")
for baris in sore:
    print(baris)

print("\nHasil Penjumlahan Stok:")
for baris in hasil:
    print(baris)

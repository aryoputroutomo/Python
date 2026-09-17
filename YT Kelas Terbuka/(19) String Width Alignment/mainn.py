# Width and Multiline 
# Data 
data_nama = 'Alex'
data_umur = 19
data_tinggi = 176
data_nomor_sepatu = 44

# String standard
print (f'{5*'='} DATA {'='*5}')
print (f' Nama = {data_nama}, Umur = {data_umur}, Tinggi = {data_tinggi}, Nomor sepatu = {data_nomor_sepatu}')

# string multiline (\n)
print (f' \n {5*'='} DATA {'='*5}')
print (f' Nama = {data_nama} \n Umur = {data_umur} \n Tinggi = {data_tinggi} \n Nomor sepatu = {data_nomor_sepatu}')

# String Multiline (kutip triplets)
print (f"""
Nama = {data_nama}
Umur = {data_umur}
Tinggi badan = {data_tinggi}
Nomor sepatu = {data_nomor_sepatu}
""")

# Mengatur agar rapi
print (f"""
Nama         = {data_nama}
Umur         = {data_umur}
Tinggi badan = {data_tinggi}
Nomor sepatu = {data_nomor_sepatu}
""")

# rata kanan 
print (f"""
Nama         = {data_nama:>8}
Umur         = {data_umur:>8}
Tinggi badan = {data_tinggi:>8}
Nomor sepatu = {data_nomor_sepatu:>8}
""")
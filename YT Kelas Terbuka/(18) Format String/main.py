# Contoh generic
# String
nama = 'Sri'
str = f'Hello {nama}'
print(str)

# Angka
angka = 2026.5
format_str = f'angka = {angka}'
print (format_str)

# True False 
boolean = True 
format_str1 = f'boolean = {boolean}'
print (format_str1)

# Bilangan jutaan  
angka = 3000000
format_str2 = f'Duit = {angka:,}'
print (format_str2)

# Bilangan desimal
angka1 = 342.87765
format_str3 = f'Desimal = {angka1:.2f}'
print (format_str3)

# Menampilkan leading zero
angka2 = 342.87765
format_str4 = f'Desimal = {angka2:8.2f}'
print (format_str4)

angka3 = 342.87765
format_str5 = f'Desimal = {angka3:6.2f}'
print (format_str5)

angka4 = 342.87765
format_str6 = f'Desimal = {angka4:08.2f}'
print (format_str6)

# Menampilkan tanda + atau -
angka_minus = -6
angka_positif = 9
print (f'minus = {angka_minus}')
print (f'positif = {angka_positif}')

# Jika ingin menampilkan tanda nya
angka_minus = -6
angka_positif = 9
print (f'minus = {angka_minus:+d}')
print (f'positif = {angka_positif:+d}')

# Jika angka desimal
angka_minus = -6.9763
angka_positif = 9.374
print (f'minus = {angka_minus:+.2f}')
print (f'positif = {angka_positif:+.2f}')

# Memformat persen 
persentase = 0.036
print (f'persen = {persentase}')

persentase = 0.036
print (f'persen = {persentase:%}')

persentase = 0.036
print (f'persen = {persentase:.3%}')

# Operasi Aritmatika di dalam placeholder
Nilai1 = 3
Nilai2 = 7
print (f'{Nilai1} + {Nilai2} = {Nilai1 + Nilai2}')

Nilai1 = 2000
Nilai2 = 70
print (f'{Nilai1} x {Nilai2} = {Nilai1 * Nilai2:,}')

# Format amgka lain (binary, octal, hexadecimal)
Angka = 999
print (f'Binary = {bin(angka)}')
print (f'Octal = {oct(angka)}')
print (f'hex = {hex(angka)}')

# Operasi dan manipulasi string

# 1. menyambung string (concatenate)
nama_pertama = 'Agas'
nama_tengah = 'Tyo'
nama_akhir = 'Cahyo'

Nama_Lengkap = nama_pertama + nama_tengah + nama_akhir 
print ('Nama lengkap =', Nama_Lengkap)

Nama_lengkap = nama_pertama + ' ' + nama_tengah + ' ' + nama_akhir
print (f'Nama lengkap = {Nama_lengkap}')

nama_pertama = input('Nama pertama = ')
nama_kedua = input('Nama kedua = ')
nama_ketiga = input ('Nama ketiga = ')

nama_anjing = nama_pertama + ' ' + nama_kedua + ' ' + nama_ketiga
print ('Nama lengkap = ',nama_anjing)

# 2. menghitung panjang string
panjang = len(nama_anjing)
print (f'jumlah string = {nama_anjing} adalah {panjang}')

# 3. operator untuk string
print ('\nMengecek apakah ada komponen char atau string di string')
d = 'd'
status = d in  Nama_lengkap
print (f'string {d} ada di {Nama_lengkap} = {str(status)}')

d = 'd'
status = d not in  Nama_lengkap
print (f'string {d} tidak ada di {Nama_lengkap} = {str(status)}')

# Mengulang string 
print ('='*10)
print (10*'=')

# Indexing 
print (f'Index ke-0 = {Nama_lengkap[0]}')
print (f'Index ke-1 = {Nama_lengkap[1]}')
print (f'Index ke-(-2) = {Nama_lengkap[-2]}')

print (f'Index ke-(1-4) = {Nama_lengkap[1:5]}')
print (f'Index ke-(0-7) = {Nama_lengkap[0:8]}')

print (f'Index ke-(0,2,4,6,8) = {Nama_lengkap[0:9:2]}')

# item paling kecil 
print (f'Item paling kecil = {min(Nama_lengkap)}')

# item paling besar 
print (f'Item paling besar = {max(Nama_lengkap)}')

ascii_code = ord(' ')
print (f'ASCII Code dari spasi adalah {str(ascii_code)}')
data = 117 
print (f'Char untuk ASCII 117 = {chr(data)}')

# 4. Operator dalam bentuk method 
data = 'Khayla15'
jumlah = data.count('a')
print (f'Jumlah a pada {data} adalah {str(jumlah)}')


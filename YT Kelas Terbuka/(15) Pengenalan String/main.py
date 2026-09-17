
data = 'ini adalah string'
print (data)
print (type(data))

# 1. Cara membuat string 

print ('''
1. dengan menggunakan singke quote '...'
2. dengan menggunakan double qute "..."
''')

data = 'Menggunakan single quote'
print (data)

data = "Menggunakan double quote"
print (data)

# Jika di gabung 
print ('"hallo, apa kabar"')
print ("'Halo, apa kabar'")

# 2. Menggunakan tanda \
# membuat tanda ' menjadi string 
print ('mari solat jum\'at') 
print ("mari solat jum'at")

# backlash (\) 
#Blacklash hanya satu akan eror 
#Bagaimana tanda blacklash bisa muncul dalam tampilan? #dengan menambahkan blacklash lagi, jadi double
print('C:\\user\\Aryo')

# tab (\t) 
# spasi ke samping (menjauh)
print('Ucup\tOtong')
print('Ucup\t\totong')

# backspace (\b)
# mendekat
print('Ucup \botong')

# Newline (\n)
# spasi kebawah
print('Baris pertama.\nBaris kedua.')

# 3. String Literal atau raw

# raw string 
print (r'C:\new folder')

# multiline literal string
print ('''
Nama : Ucup 
Kelas : 3 SMA
''')

# multiline Literal String dan Raw
print (r'''
Nama : Agastyo Cahyo Utomo\Agas 
Kelas : 2 SMP
Website : https://www.com/ganteng.ID
''')
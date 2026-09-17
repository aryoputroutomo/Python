# Operator dalam bentuk methods 
## merubah case dari string 

# merubah semua ke upper case 
salam = 'bro!'
print('Normal = ' + salam)
salam = salam.upper ()
print('Upper = ' + salam)

# PERCOBAAN 
p = 'jing'
p = p.upper()
print ('nyacK = ' + p)

# Merubah semua ke lower case 
alay = 'ASUUUU'
print ('normal = ' + alay)
alay = alay.lower()
print ('Lower = ' + alay)

## pengecekan dengan is X method 

# contoh pengecekan lower case 
salam = 'sist'
apakah_lower = salam.islower()
print (salam + ' is lower = ' + str(apakah_lower)) # HASILNYA BOOL

# PERCOBAAAN 
teknik = 'Jaya'
apakah_lower = teknik.islower()
print (teknik + ' is lower = ' + str(apakah_lower)) # HASILNYA BOOL

# contoh pengecekan Upper case
salam = 'sisst'
apakah_Upper = salam.isupper()
print (salam + ' is Upper = ' + str(apakah_Upper))

# PERCOBAAN 
ANJING = 'JAYA'
apakah_upper = ANJING.isupper()
print (ANJING + ' is Upper = ' + str(apakah_upper))

# isalpha() <-- untuk mengecek semuanya huruf
# isalnum() <-- untuk mengecek huruf & angka ## Terdapat di pasword 
# isdecimal() <-- untuk mengecek angka saja
# isspace() <-- untuk mengecek spasi, tab, newline (\n)
# istitle() <-- mengecek semua kata dimulai dengan huruf besar

judul = 'Spiderman New Brand'
cek_judul = judul.istitle()
print (f'Apakah {judul} istitle? = {str(cek_judul)}')

judul1 = "It's okay bro?" 
cek_judul1 = judul1.istitle()
print (f'Apakah {judul1} istitle? = {str(cek_judul1)}')

judul2 = "It is okay bro?" 
cek_judul2 = judul2.istitle()
print (f'Apakah {judul2} istitle? = {str(cek_judul2)}')

## mengecek komponen 
#startswith()
#endswith()
cek_start = 'Aryo Putro Utomo'.startswith('Aryo')
print (f'apakah benar Aryo Putro Utomo dimulai dari Aryo? {str(cek_start)}')

### COBA COBA ###
cek_start1 = 'Aryo Putro Utomo'
koreksi = cek_start1.startswith('Aryo')
print (f'Apakah benar {cek_start1} dimulai dari Aryo? {str(koreksi)} ')

cek_start2 = 'Aryo Putro Utomo'.startswith('Utomo')
print (f'Apakah Aryo Putro Utomo dimulai dari Utomo? {str(cek_start2)}')

cek_end = 'Aryo Putro Utomo'.endswith('Utomo')
print (f'Apakah kata akhir dari Aryo Putro Utomo adalah Utomo? {str(cek_end)}')

### COBA COBA ###
cek_end1 = 'Aryo Putro Utomo'.endswith('Aryo')
print (f'Apakah kata akhir dari Aryo Putro Utomo adalah Aryo {str(cek_end1)}')

## Penggabungan komponen
# join()
# split()
pisah = ['aku','sayang','kamu']
print (pisah)

# PEMISAHAN KE GABUNGAN
gabungan = ','.join(pisah)
print (gabungan)
gabungan1 = ' '.join(pisah)
print (gabungan1)
gabungan2 = ' ekhem '.join(pisah)
print (gabungan2)

# GABUNGAN KE PEMISAHAN
gabungan3 = 'akuekhemsayangekhemkamu'.split('ekhem')
print (gabungan3)

# Alokasi karakter
# rjust()
# ljust()
# center()
print (f'{5*'='} data {'='*5}')

kanan = 'Kanan'.rjust(10)
print (f"'{kanan}'")

### COBA COBA ###
kanan1 = 'ANJING LU'.rjust(10)
print (f"'{kanan1}'")
kanan2 = 'kanan'.rjust(20,'=')
print (f"'{kanan2}'")

kiri = 'Kiri'.ljust(10)
print (f"'{kiri}'")

### COBA COBA ###
kiri1 = 'ANJING LU'.ljust(10)
print (f"'{kiri1}'")
kiri2 = 'kiri'.rjust(20,'-')
print (f"'{kiri2}'")


tengah = 'Tengah'.center(10)
print (f"'{tengah}'")

### COBA COBA ###
tengah1 = 'Tengah'.center(20,'-')
print (f"'{tengah1}'")

# kebalikannya -> strip()
tengah2 = tengah1.strip('-') # Menghilangkan tanda "-"
print (f"'{tengah2}'")

kiri3 = kiri.strip() # Menghilangkan spasi
print (f"'{kiri3}'")

kanan3 = kanan2.strip('=')
print (f"'{kanan3}'")
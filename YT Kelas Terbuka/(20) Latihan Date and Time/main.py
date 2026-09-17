# Date and Time 

### TIME
import datetime 
hari_ini = datetime.date.today() 
print (hari_ini)

import datetime as dt 
hari_ini2 = dt.date.today()
print (hari_ini2)

### TANGGAL
tanggal = dt.date(2008,4,18)
print (tanggal)

tanggal1 = 2005,200,77
print (tanggal1)

### CARA CEK HARI 
import datetime as dt
hari_ini3 = dt.date.today()
print (f'Hari ini adalah hari = {hari_ini3:%A}')

tanggal2 = dt.date(2008,4,18)
print (f'Tanggal 18 April 2008 adalah hari {tanggal2:%A}')

## CASE
print ('Silakan masukkan tanggal, bulan, dan tahun lahir anda\n')
tanggal = int(input (f'tanggal = '))
bulan = int(input (f'bulan \t= ')) # NOTE Tidak bisa didahului angka 0
tahun = int(input (f'tahun \t= '))

tanggal_lahir = dt.date(tahun,bulan,tanggal)
print (f'tanggal lahirmu adalah {tanggal_lahir} di hari {tanggal_lahir:%A}')

umur_hari = hari_ini - tanggal_lahir
umur_tahun = umur_hari.days // 365
umur_bulan_sisa = (umur_hari.days % 365) //30
print (f'Umur anda adalah {umur_hari}')
print (f'Umuar anda adalah {umur_tahun} tahun')
print (f'Umur bulan sisa adalah {umur_bulan_sisa} bulan')

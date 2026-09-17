# Operasi Aritmatika

a = 10
b = 3 

# Operasi tambah (+)
hasil = a + b
print(a,'+',b,'=', hasil)

# Operasi kurang (-)
hasil = a - b
print(a,'-',b,'=', hasil)

# Operasi kali (*)
hasil = a * b
print(a,'x',b,'=', hasil)

# Operasi bagi (/)
hasil = a / b
print(a,':',b,'=', hasil)

# Operasi eksponen/pangkat (**)
hasil = a ** b
print(a,'**',b,'=', hasil)

# Operasi modulus/sisa pembagian (%)
hasil = a % b
print(a,'%',b,'=', hasil)

# Operasi floor division (//)
hasil = a // b
print(a,'//',b,'=', hasil)

# prioritas operasi, operational precedence 

x = 3
y = 2
z = 4

hasil = x ** y * z + x / y - y % z // x
print (x,'**',y,'*',z,'+',x,'/',y,'-',y,'%',z,'//',x,'=', hasil)

x = 2 
y = 4 
hasil = x % y
print (hasil)

hasil = x + y * z 
print (x,'+',y,'*',z,'=',hasil)
hasil = (x + y) * z 
print ('(',x,'+',y,')','*',z,'=',hasil)
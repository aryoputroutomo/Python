# Operasi yang dpt dilakukan dgn penyingkatan
# Operasi ditambah dengan assignment

a = 5 # ini adalah assignment
print ('nilai a =', a )

a = a + 1 
print ('nilai a =', a)

print (40*'=')

a += 1 # artinya adalah a = a + 1 
print ('nilai a += 1, nilai a menjadi', a)

a -= 2 # artinya adalah a = a - 2 
print ('nilai a -= 2, nilai a menjadi', a)

a *= 3 # artinya adalah a = a x 3 
print ('nilai a x= 3, nilai a menjadi', a)

a /= 5 # artinya adalah a = a : 5
print ('nilai a := 5, nilai a menjadi', a)

# modulus dan floor division

b = 10
print ('\nnilai b =', b)
b %= 3 # artinya adalah b = b % 3 
print ('nilai b %= 3, nilai b menjadi', b)

b = 10
print ('\nnilai b =', b)
b //= 3 # artinya adalah b = b // 3 
print ('nilai b //= 3, nilai b menjadi', b)

# Pangkat

a = 7 
print('\nnilai a =', a)
a **= 4
print('nilai a **= 4, nilai a menjadi', a)

print (40*'=')
# Operasi Bitwise
# OR
c = True 
print('\nnilai c =', c)
c |= False
print('nilai c |= false, nilai c menjadi', c)

c = False
print('\nnilai c =', c)
c |= False
print('nilai c |= false, nilai c menjadi', c)

c = True 
print('\nnilai c =', c)
c |= True
print('nilai c |= True, nilai c menjadi', c)

print (40*'=')
# AND
c = True 
print('\nnilai c =', c)
c &= False
print('nilai c &= false, nilai c menjadi', c)

c = False
print('\nnilai c =', c)
c &= False
print('nilai c &= false, nilai c menjadi', c)

c = True 
print('\nnilai c =', c)
c &= True
print('nilai c &= True, nilai c menjadi', c)

print (40*'=')
# XOR
c = True 
print('\nnilai c =', c)
c ^= False
print('nilai c ^= false, nilai c menjadi', c)

c = False
print('\nnilai c =', c)
c ^= False
print('nilai c ^= false, nilai c menjadi', c)

c = True 
print('\nnilai c =', c)
c ^= True
print('nilai c ^= True, nilai c menjadi', c)

print (40*'=')
# Geser geser
d = 0b0100
print ('\nnilai d =', format(d,'04b'))
d >>= 2 
print ('nilai d >>= 2, nilai d menjadi', format(d,'04b'))

d <<= 1
print ('nilai d <<= 1, nilai d menjadi', format(d,'04b'))

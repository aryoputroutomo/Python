#Kalkulator sederhana

print (20*'=')
print ('Kalkulator sederhana')
print (20*'=' + '\n')

angka_1 = float(input('masukan angka 1 = '))
operator = input ('operator (+,-,x,:) = ')
angka_2 = float(input('masukan angka 2 = '))

# Percabangan 
if operator == '+':
    hasil = angka_1 + angka_2
    print (f'hasil = {hasil}')
    print (f'hasil =', hasil)

elif operator == '-':
    hasil = angka_1 - angka_2
    print (f'hasil = {hasil}')
    print (f'hasil =', hasil)

elif operator == 'x':
    hasil = angka_1 * angka_2 
    print (f'hasil = {hasil}')
    print (f'hasil =', hasil)   

elif operator == ':':
    hasil = angka_1 / angka_2
    print (f'hasil = {hasil}')
    print (f'hasil =', hasil)

else: 
    print ('salah woii, masukan yg bener!')
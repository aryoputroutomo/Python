angka_1 = float(input('Masukan angka = '))
operator = input('Masukan (+,-,x,:) = ')
angka_2 = float(input('Masukan angka = '))

if operator == '+':
    hasil = angka_1 + angka_2 
    print('hasil =', hasil)

if operator == '-':
    hasil = angka_1 - angka_2
    print ('hasil =', hasil )

if operator == 'x':
    hasil = angka_1 * angka_2 
    print ('hasil = ', hasil)

if operator == ':':
    hasil = angka_1 / angka_2
    print ('hasil =', hasil)




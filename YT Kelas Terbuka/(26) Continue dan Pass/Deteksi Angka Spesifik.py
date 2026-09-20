angka = range(1, 16)

for i in angka:
    if i % 5 == 0:
        print (f'{i} = kelipatan 5 ditemukan')
        continue

    if i == 7:
        pass 

    print(i)
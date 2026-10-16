username_benar = 'aryo'
password_benar = 'khayla15'
maksimal_percobaan = 3
percobaan = 0 

while percobaan < maksimal_percobaan:
    username = input('Username: ')
    password = input('password: ')
    percobaan += 1
    print (f'percobaan ke-{percobaan}')

    if username == username_benar and password == password_benar:
        print ('login berhasil')
        break
    else:
        print ('login gagal')

        if percobaan == maksimal_percobaan:
            print ('percobaan login sudah maksimal, silahkan coba lagi nanti')
        else:
            print (f'sisa percobaan = {maksimal_percobaan - percobaan}')

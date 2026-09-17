import webbrowser
nama = input('Masukkan nama = ')
command = input('Masukkan perintah = ')

if command == 'buka yt':
    webbrowser.open('https://www.youtube.com')
    print (f'OKe {nama}, saya membuka youtube')

elif command == 'buka gogle':
    webbrowser.open('https://wwwgoogle.com')
    print(f'Oke {nama} saya membuka google')

elif command == 'buka wa':
    webbrowser.open('https://web.whatsapp.com/')
    print(f'Oke {nama} saya membuka WhatsApp')

elif command == 'buka ig':
    webbrowser.open('https://www.instagram.com/')
    print(f'Oke {nama} saya membuka Instagram')

else :
    print (f'Maaf {nama} Perintah tidak tersedia')
# IF ELSE
#kata = input("Masukkan kata: ")
#kata_kasar = ['asu', 'babi', 'anjing', 'bangsat', 'kontol', 'memek', 'jembut', 'jancok', 'bajingan', 'tai', 'tolol', 'goblok', 'bego', 'bangke', 'brengsek', 'kampret', 'setan', 'sialan']

#if kata in kata_kasar:
#        print(f"Kata kasar '{kata}' terdeteksi!")
#else:
#        print(f"Kata '{kata}' tidak termasuk kata kasar.")

# BREAK 

Komentar = ['halo', 'apa kabar', 'selamat datang!', 'asu', 'sampai jumpa']

for kata in Komentar:
    kata = input("Masukkan kata: ")
    if kata == 'asu':
        print(f"Kata kasar '{kata}' terdeteksi!")
        break
    else:
        print(f"Kata '{kata}' tidak termasuk kata kasar.")
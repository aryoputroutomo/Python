nomor_kartu = input("Masukkan nomor kartu: ")
if nomor_kartu == "123456789":
    pin = input("Masukkan PIN: ")
    if pin == "1234":
        print("Akses diterima. Selamat datang!")
    else:
        print("PIN salah. Akses ditolak.")
else:
    print("Nomor kartu tidak valid. Akses ditolak.")

umur = int(input("Masukkan umur Anda: "))
if umur >= 13:
    tinggi = float(input("Masukkan tinggi badan Anda (dalam cm): "))
    if tinggi >= 150:
        print("Selamat! Anda memenuhi syarat dan boleh naik wahana.")
    else:
        print("Umur cukup, tetapi tinggi badan Anda kurang dari 150 cm (Akses Ditolak)")
else:
    print("Maaf, wahana ini hanya untuk usia 13 tahun ke atas.")
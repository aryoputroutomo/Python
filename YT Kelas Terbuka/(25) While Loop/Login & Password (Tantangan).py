#username = ""
#password = ""

#while username != "Aryo":
    #username = input("username = ")

#while password != "khayla":
    #password = input("password = ")
#print ("Login Berhasil")

# VERSI SEKARANG
username_benar = "Aryo"
password_benar = "khayla"
username = ""
password = ""

while username != username_benar or password != password_benar:
    username = input("username = ")
    password = input("password = ")
    print ("Login Gagal")
print ("Login Berhasil")
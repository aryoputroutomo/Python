# Latihan membuat segitiga 

sisi = 12

# 1. Menggunakan for
# Dummy variabel
count = 1
for i in range(sisi):
    print("*" * count)
    count += 1

print("\n")
# 2. Menggunakan while

count = 1
while True:
    print("*" * count)
    count += 1
    if count > sisi:
        break

print("\n")
# 3. skip ganjil 

count = 1
while True:
    if count%2:
        count += 1
        continue
    # akan print jika genap
    print("*" * count)
    count += 1
    # akan break jika count melebihi sisi
    if count > sisi:
        break

print("\n")
# 4. Segitiga sama sisi
count = 1
spasi = int(sisi/2)
while True:
    if (count%2):
        print (" "*spasi, "+"*count)
        spasi -= 1
        count += 1
    else:
        count += 1
        continue
    if count > sisi:
        break


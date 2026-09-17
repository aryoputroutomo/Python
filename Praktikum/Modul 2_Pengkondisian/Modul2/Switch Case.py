menu = int(input("Pilih menu (1-3): "))

match menu:
    case 1:
        print("Ayam Bali Crispy")
    case 2:
        print("Ayam Balap")
    case 3:
        print("Orak Arik Magelangan")
    case _:
        print("Menu tidak tersedia")

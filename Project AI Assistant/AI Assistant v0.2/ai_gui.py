import tkinter as tk

# Membuat jendela utama
window = tk.Tk()

# Judul aplikasi
window.title("N.E.X AI Assistant")

# Ukuran jendela
window.geometry('500x400')

# Teks sambutan
label = tk.Label(
    window,
                 text = 'Hallooo Saya N.E.X AI Assistant. \n\n Apa yang bisa saya bantu?',
                 font = (f'Arial {16}')
                 )

label.pack(pady=50)

#Menjalankan aplikasi
window.mainloop()
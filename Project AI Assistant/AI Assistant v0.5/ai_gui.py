import tkinter 
import pyttsx3

# TEXT TO SPEECH
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

# JENDELA UTAMA 

window = tkinter.Tk()

window.title ('N.E.X AI Assistant')
window.geometry ('600x500')

# FUNGSI KIRIM PESAN
def send_message():
    message = input_box.get()

    if message:
        chat.insert(tkinter.END, 'Kamu: ', message, '\n')
        chat.insert(tkinter.END, 'N.E.X: Halo, Aryo! hmmm gimana kabarmu? \n\n')

        input_box.delete(0, tkinter.END)

# judul
title = tkinter.Label(
    window,
    text = 'N.E.X AI Assistant',
    font = (f'Arial {20}')
)
title.pack(pady = 10)

# Area percakapan 
chat = tkinter.Text(
    window, 
    height = 20, 
    width = 70
)
chat.pack(padx = 10, pady = 10)

# Kotak input 
input_box = tkinter.Entry (
    window, 
    width = 50
)
input_box.pack(side = 'left', padx = 10, pady = 10)

# Tombol kirim 
send_button = tkinter.Button(
    window,
    text = 'Kirim',
    command = send_message
)
send_button.pack(side = 'left', pady = 10)

# Mulai aplikasi
window.mainloop()
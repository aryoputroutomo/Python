import tkinter 
import pyttsx3
import threading 

# TEXT TO SPEECH

def speak(text):
    def run():
        engine = pyttsx3.init()
        engine.say(text)
        engine.runAndWait()

    threading.Thread(target = run, daemon = True).start()
# JENDELA UTAMA 

window = tkinter.Tk()

window.title ('N.E.X AI Assistant')
window.geometry ('600x500')

# FUNGSI KIRIM PESAN
def send_message():
    message = input_box.get()

    if message:
        # Tampilkan pesan dari pengguna
        chat.insert(
            tkinter.END,
            "Kamu: " + message + "\n"
        )

        # Respons AI
        response = "Halo juga, Aryo!"

        # Tampilkan respons AI
        chat.insert(
            tkinter.END,
            "N.E.X: " + response + "\n\n"
        )

        # Hapus isi kotak input
        input_box.delete(0, tkinter.END)

        # Jalankan suara
        speak(response)

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

# Sapaan awal 
chat.insert(
    tkinter.END,
    'N.E.X: Halo, ada yang bisa kubantu?\n\n'
)

window.after(
    500,
    lambda: speak('Halo, ada yang bisa kubantu?')
)

# Mulai aplikasi
window.mainloop()

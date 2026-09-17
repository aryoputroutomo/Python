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
        chat.insert(tkinter.END, 'Kamu: ' + message + '\n')
        chat.insert(tkinter.END, 'N.E.X: Halo, Aryo! hmmm gimana kabarmu? \n\n')

        input_box.delete(0, tkinter.END)
        speak('Halo, Aryo! hmmm gimana kabarmu?')

# judul
title = tkinter.Label(
    window,
    text = 'N.E.X AI Assistant',
    font = ('Arial',22,'bold')
)
title.pack(pady = 15)

# Area percakapan 
chat = tkinter.Text(
    window, 
    height = 20, 
    width = 70,
    font = ('Arial', 11),
    wrap = 'word'
)
chat.pack(padx = 10, pady = 10, fill = 'both', expand = True)

# Frame Input 
input_frame = tkinter.Frame(window)

input_frame.pack(fill = 'x', padx = 15, pady = 15)

# Kotak input 
input_box = tkinter.Entry (
    input_frame, 
    font = ('Arial', 11)
)
input_box.pack(side = 'left', fil = 'x', expand = True, padx = (0,10))

# Tombol kirim 
send_button = tkinter.Button(
    input_frame,
    text = 'Kirim',
    command = send_message
)
send_button.pack(side = 'right')

# Sapaan awal 
chat.insert(
    tkinter.END,
    'N.E.X: Halo, ada yang bisa kubantu?\n\n'
)

window.after(
    500,
    lambda: speak('Halo, ada yang bisa kubantu?')
)

# ENTER = KIRIM 
input_box.bind(
    '<Return>',
    lambda event: send_message()
)

# Mulai aplikasi
window.mainloop()

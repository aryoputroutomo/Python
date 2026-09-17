import tkinter 

window = tkinter.Tk()

window.title ('N.E.X AI Assistant')
window.geometry ('600x500')

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
    text = 'Kirim'
)
send_button.pack(side = 'left', pady = 10)

window.mainloop()

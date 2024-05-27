#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
import qrcode

def generador_qr():
    name = title.get()
    text = entry_url.get()
    qr = qrcode.make(text)
    qr.save(str(name) + ".png" )
    global Image
    Image = PhotoImage(file=str(name) + ".png")
    Image_view.config(image=Image)

def refresh_window():
    entry_url.delete(0, 'end')
    title.delete(0, 'end')
    Image.__del__()

root = tk.Tk()
root.wm_title("Create QR")
root.wm_geometry("1000x750")
root.config(bg="black")
root.resizable(False, False)

button_refresh = tk.Button(root, text="Refresh", command=refresh_window, bg="#2c2c2c")
button_refresh.place(x=40, y= 450)

Label(root, text="Nombre ", fg="white", bg="black", font=20).place(x=40,y=100)
title = Entry(root, width=13, font="arial 20", bg="#6a6a6a")
title.place(x=40, y=120)

Label(root, text="URL", fg="white", bg="black", font=20).place(x=40,y=200)
entry_url = Entry(root,width=30, font="arial 20", bg="#6a6a6a")
entry_url.place(x=40, y=220)

Button(root, text="Generar QR",width=20, height=2, bg="#2c2c2c", fg="white", command=generador_qr ).place(x=40, y= 350)

Image_view = Label(root,bg="black")
Image_view.pack(padx=50, pady=10, side=RIGHT)

photo = tk.PhotoImage(file="logocr2.png")
label = tk.Label(root, image=photo).place(x=400, y= 580)

menu_bar = tk.Menu(root, bg="#2c2c2c")
menu_options = tk.Menu(menu_bar, tearoff=0, bg="#2c2c2c")
menu_options.add_command(label="Nuevo", command=refresh_window)
menu_options.add_command(label="Cerrar", command=quit)

root.config(menu=menu_bar)
menu_bar.add_cascade(label="Menu", menu=menu_options)

tk.mainloop()


import tkinter as tk
from tkinter import *
import os
from threading import Thread
from PIL import Image, ImageTk

root = tk.Tk()
root.title("Vedalingo")
root.geometry("1025x600+200+100")
root.configure(background="#fff")
root.resizable(False,False)

####################################################################
#Brown Background Image
image2 =Image.open('Background.jpg')
image2 =image2.resize((1025,600), Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)
lbl = tk.Label(root, text="Explore More",justify='left', font=('Times', 30,'bold'), height=2, width=45 ,bg="White",fg="black")
lbl.place(x=0, y=20)

image3 = Image.open('logo.png')
image3 = image3.resize((147,73), Image.ANTIALIAS)
background_image3 = ImageTk.PhotoImage(image3)
background_label3 = tk.Label(root, image=background_image3, bg='white')
background_label3.image = background_image3
background_label3.place(x=10, y=28)  # , relwidth=1, relheight=1)

#Creating frame for books grid
frame = tk.Frame(root,bg="white")
frame.grid(row=0, column=0, padx=100, pady=150)

# Setting window icon of master window 
root.iconbitmap("small_icon_logo.ico")


root.mainloop()

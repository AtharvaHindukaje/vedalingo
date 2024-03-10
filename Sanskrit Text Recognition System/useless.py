import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as ms
import cv2
import sqlite3
import os
import numpy as np
import time

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="white")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Sanskrit Text Recognition System")


# Setting window icon of master window 
root.iconbitmap("small_icon_logo.ico")

#hides resize and minimize icons
#root.attributes('-toolwindow', True)
##################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#For background Image
#label_l1 = tk.Label(root, text="",font=("Microsoft YaHei UI Light", 5, 'bold'),
 #                  background="#152238", fg="white", width=60, height=10)
#label_l1.place(x=0, y=0)

#For background Image
image2 = Image.open('logo.png')
image2 = image2.resize((177,250), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image, bg='white')
background_label.image = background_image
background_label.place(x=25, y=-30)  # , relwidth=1, relheight=1)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%



def reg():
    from subprocess import call
    call(["python","registration.py"])

def log():
    from subprocess import call
    call(["python","login.py"])
    
def exitapp():
  if mbox.askokcancel("Exit", "Do you want to exit?"):
      root.destroy()


button1 = tk.Button(root, text="Register",command=reg,width=18, height=1,font=('Microsoft YaHei UI Light', 15, ' bold '), bg="#805033", fg="white", borderwidth=0, cursor="hand2")
button1.place(x=100, y=700)

button2 = tk.Button(root, text="Login", command=log, width=18, height=1,font=('Microsoft YaHei UI Light', 15, 'bold'), bg="#805033", fg="white", borderwidth=0, cursor="hand2")
button2.place(x=400, y=700)

button3 = tk.Button(root, text="Exit",command=exitapp,width=10, height=1,font=('Microsoft YaHei UI Light', 10, ' bold '), bg="red", fg="white", borderwidth=0, cursor="hand2")
button3.place(x=1350, y=700)

root.mainloop()
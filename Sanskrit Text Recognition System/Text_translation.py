import os
from gtts import gTTS
from translate import Translator
from PIL import Image , ImageTk   
import tkinter as tk
from tkinter import ttk, LEFT, END
from tkinter import * 
import tkinter as tk
from tkinter import ttk, LEFT, END
import time
import numpy as np
import cv2
import os
from PIL import Image , ImageTk     
from PIL import Image 
import sqlite3
##############################################+=============================================================

root = tk.Tk()
root.geometry("1025x600+200+100")
root.resizable(False,False)
root.title("Vedalingo Language Translation")
root.configure(background="#fff")

# Setting window icon of master window 
root.iconbitmap("small_icon_logo.ico")

###########################################################################

c=StringVar()
c1=StringVar()
data=StringVar()

input_frame = tk.LabelFrame(root, text=" --INPUT-- ", width=480, height=300, bd=5, font=('times', 15, ' bold '),bg="lightblue1")
input_frame.grid(row=0, column=0, sticky='nw')
input_frame.place(x=100, y=180)

output_frame = tk.LabelFrame(root, text=" --OUTPUT-- ", width=300, height=300, bd=5, font=('times', 15, ' bold '),bg="indian red")
output_frame.grid(row=0, column=0, sticky='nw')
output_frame.place(x=600, y=180)

############################################################################


def update_label(str_T):
     #result_label=tk.Message(output_frame,text=str(str_T),font=('times', 30, 'bold'),width=100,bg="blue")
    # result_label.place(x=930, y=180)
    result_label = tk.Label(output_frame, text=str_T, font=('times', 15, 'bold'), bg="indian red", fg='white')
    result_label.place(relx=0.5, rely=0.5, anchor="center")
     
############################################################################


def translate(): 
    Lang1=c.get()
    print(Lang1)
    Lang2=c1.get()
    print(Lang2)
    #"1.0", "end-1c" for below
    data = input_text.get("1.0", "end")
    print(data)
    Lang3=c.get()
    print(Lang3)
    translator= Translator(from_lang=Lang1,to_lang=Lang2)
    translation = translator.translate(data)
    print(translation)
    update_label(translation)
    

############################################################################


list1 = ['English','Marathi','Hindi','sanskrit'];
list2 = ['English','Marathi','Hindi','sanskrit'];

droplist=OptionMenu(input_frame,c, *list1)
droplist.config(width=10)
c.set('From') 
droplist.place(x=100,y=180)

droplist=OptionMenu(input_frame,c1, *list2)
droplist.config(width=10)
c1.set('To') 
droplist.place(x=300,y=180)


############################################################################


#label_1 = Label(input_frame, text="INPUT TEXT",width=20,font=("bold", 10))
#label_1.place(x=20,y=30)

#input_text = Entry(input_frame,textvar=data,width=60)
#input_text.place(x=50,y=30)

input_text = Text(input_frame, width=40, height=5)  # Use Text widget for input text
input_text.place(x=50, y=30)

Button(input_frame, text='Translate', width=20, bg='brown', fg='white', command=translate, relief="flat", borderwidth=0, cursor="hand2").place(x=150,y=230)



root.mainloop()

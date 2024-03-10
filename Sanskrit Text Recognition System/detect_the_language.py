#language detect
#1.English
#2.Hindi
#3.Bengali
#4.Gujarati
# imported necessary library
import tkinter
from tkinter import *
import tkinter as tk
import tkinter.messagebox as mbox
import nltk
import pycountry
from nltk.stem import SnowballStemmer


# created main window
window = Tk()
window.geometry("1025x600+200+100")
window.resizable(False,False)
window.title("Detecting Language")
window.configure(background="#fff")

# Setting window icon of master window 
window.iconbitmap("small_icon_logo.ico")


###############################################################       

# function for exiting
def exit_win():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        window.destroy()

def lang_check():
    input_text = text_enter.get("1.0", END)
    tc = nltk.classify.textcat.TextCat()
    guess_text = tc.guess_language(input_text)
    guess_lang = pycountry.languages.get(alpha_3=guess_text).name
    mbox.showinfo("Detected Language", "Detected Language :\n\n" + guess_lang)

####################################################################

# top label
sec1 = tk.Label(window,text="Enter any text or paragraph and detect Language...", font=('Microsoft YaHei UI Light',12,'bold'), fg="brown",bg='white')  # same way bg
sec1.place(x=80, y=20)

#Created text area
text_enter = tk.Text(window, height=18, width=75, font=('Microsoft YaHei UI Light',12,'bold'),bg='white',fg='black', borderwidth=3,relief="solid")
text_enter.place(x=80, y=100)

# function for clearing the entry box
def clear_entry():
    text_enter.delete("1.0", END)

# created check button
checkb = Button(window, text="DETECT",command=lang_check, font=('Microsoft YaHei UI Light',12,'bold'), width=18, bg='red',fg='black', relief="flat", borderwidth=0, cursor="hand2")
checkb.place(x =150 , y =500 )

# created clear button
clearb = Button(window, text="CLEAR", command=clear_entry, font=('Microsoft YaHei UI Light',12,'bold'), width=18,bg='red',fg='black', relief="flat", borderwidth=0, cursor="hand2")
clearb.place(x=350, y=500)

# created exit button
exitb = Button(window, text="EXIT",command=exit_win,font=('Microsoft YaHei UI Light',12,'bold'), width=18,bg='red',fg='black', relief="flat", borderwidth=0, cursor="hand2")
exitb.place(x =550 , y =500)



window.protocol("WM_DELETE_WINDOW", exit_win)
window.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import ttk, LEFT, END
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import os
import random


##############################################+=============================================================
window = tk.Tk()
window.title("Vedalingo")
window.configure(background="#fff")
window.geometry("1025x600+200+100")
window.resizable(False,False)


round_design = Image.open('round_design.png')
round_design  = round_design.resize((900,900), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(round_design)
Label(window,image=img2,bg='white').place(x=350,y=-150)


logo_img = Image.open('logo.png')
logo_img  = logo_img.resize((324,154), Image.ANTIALIAS)
img = ImageTk.PhotoImage(logo_img)
Label(window,image=img,bg='white').place(x=20,y=200)

frame= Frame(window,width=400,height=450,bg="white")
frame.place(x=500,y=70)

# Setting window icon of master window 
window.iconbitmap("small_icon_logo.ico")

email = tk.StringVar()
password = tk.StringVar()


###############################+====================================

# Sign In Image and label
       
sign_in_image = Image.open('hyy.png')
sign_in_image = sign_in_image.resize((75,75), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(frame, image=photo, bg='white')
sign_in_image_label.image = photo
sign_in_image_label.place(x=165, y=30)

sign_in_label = Label(frame, text="Sign In", bg="white", fg="#805033", font=('Microsoft YaHei UI Light',23,'bold'))
sign_in_label.place(x=145, y=110)


# ========================================================================


def on_enter(e):
    user.delete(0,'end')
def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Email')
        
user= Entry(frame, width=25, fg='black', textvariable=email, border=0, bg='white', font=('Microsoft YaHei UI Light',11))
user.place(x=90,y=180)
user.insert(0,'Email')
user.bind("<FocusIn>",on_enter)
user.bind("<FocusOut>",on_leave)

# ===== Username icon =========
username_icon = Image.open('email.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(frame, image=photo, bg='white')
username_icon_label.image = photo
username_icon_label.place(x=60, y=180)


Frame(frame,width=290,height=2,bg="#805033").place(x=60,y=207)


###############################+====================================

def on_enter(e):
    user2.delete(0,'end')
    user2.config(show='•')
    
def on_leave(e):
    name=user2.get()
    if name=='':
        user2.insert(0,'Password')
        user2.config(show='')
        
user2= Entry(frame,width=25,fg='black',border=0,textvariable=password, bg='white',font=('Microsoft YaHei UI Light',11))
user2.place(x=90,y=250)
user2.insert(0,'Password')
user2.bind("<FocusIn>",on_enter)
user2.bind("<FocusOut>",on_leave)

# ======== Password left side icon ================
password_icon = Image.open('password.png')
photo = ImageTk.PhotoImage(password_icon)
password_icon_label = Label(frame, image=photo, bg='white')
password_icon_label.image = photo
password_icon_label.place(x=60, y=250)

# ========= show/hide password ==================================================================
show_image = ImageTk.PhotoImage(file='show.png')
hide_image = ImageTk.PhotoImage(file='hide.png')

def show():
    hide_button = Button(frame, image=hide_image, command=hide, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
    hide_button.place(x=310, y=250)
    user2.config(show='')

def hide():
    show_button = Button(frame, image=show_image, command=show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=310, y=250)
    user2.config(show='•')

show_button = Button(frame, image=show_image, command=show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
show_button.place(x=310, y=250)

Frame(frame,width=290,height=2,bg="#805033").place(x=60,y=277)


###############################+====================================
        

def registration():
    window.destroy()
    from subprocess import call
    call(["python","registration.py"])
    
def login():
    # Establish Connection
    with sqlite3.connect('resistration.db') as db:
         c = db.cursor()

        # Find user If there is any found then take proper action
         db = sqlite3.connect('resistration.db')
         cursor = db.cursor()
         cursor.execute("CREATE TABLE IF NOT EXISTS registration"
                           "(username TEXT, email TEXT, Phoneno TEXT,Gender TEXT, password TEXT)")
         db.commit()
         find_entry = ('SELECT * FROM registration WHERE email = ? and password = ?')
         c.execute(find_entry, [(email.get()), (password.get())])
         result = c.fetchall()

         if result:
            msg = ""
            print(msg)
            cmd=str(email.get())
            pwd=str(password.get())
            ms.showinfo("Status", "LogIn sucessfully")
            temp='python sendmail.py'+' '+cmd+' '+pwd+' '+'loginsuccess' #we send file name + email id
            os.system(temp)
            # ===========================================
            window.destroy()
            from subprocess import call
            call(['python','image_to_text_multilang.py'])

            # ================================================
         else:
           ms.showerror('Oops!', 'Username Or Password Did Not Found/Match.')
           #conn.close()


# =========================================================
# Forgot password function

def forgot_password():

    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')

    win.title('Forgot Password')
    win.iconbitmap("small_icon_logo.ico")
    win.configure(background='white')
    win.resizable(False, False)
    forgot_email=StringVar()
    
    # ====== Email in popup ====================
    email_label3 = Label(win, text='• Email', fg="#805033", bg='white', font=("Microsoft YaHei UI Light", 11, 'bold'))
    email_label3.place(x=40, y=50)
    email_entry3 = Entry(win, bg="white", textvariable=forgot_email, border=0, width=256, font=("Microsoft YaHei UI Light", 12))
    email_entry3.place(x=40, y=80)
    Frame(win,width=256,height=2,bg="#805033").place(x=40,y=107)

    # ======= Button in popup ============   
    def send_details():
        cmd=str(forgot_email.get())
        pwd=str(forgot_email.get())
     
        temp='python sendmail.py'+' '+cmd+' '+pwd+' '+'forgot_password'  #we send file name + email id
        os.system(temp)
        ms.showinfo("Account recovery", "If account is found,details will be sent on email")
        win.destroy()
        
    update_pass = Button(win, fg='white', text='Update Password', bg='#805033', font=("Microsoft YaHei UI Light", 12, "bold"), cursor='hand2', relief="flat", border=0, command=send_details)
    update_pass.place(x=60, y=200, width=216, height=45)
    
    
    
# ============================================================================================================    
#  login button
loginn_btn = Button(frame, text="Sign in", pady=7, command=login, width=40, bg="#805033", fg="white", border=0).place(x=60,y=334) 

# Load the image
#google_img = Image.open("google_logo.png")
#google_img  = google_img.resize((20,20), Image.ANTIALIAS)
#photo = ImageTk.PhotoImage(google_img)

#btn2 = Button(frame,width=281,pady=7, image=photo,compound=tk.LEFT, text="Sign in with Google", fg="#805033", border=0).place(x=60,y=380)

# buttons on main login page
forgot_button = Button(frame, text="Forgot Password?",command=forgot_password, font=("Microsoft YaHei UI Light", 9), fg="#805033", borderwidth=0, background="white", cursor="hand2")
forgot_button.place(x=60, y=280)

label1 = Label(frame,text="Don't have an account?", fg="black", bg='white', font=('Microsoft YaHei UI Light',9))
label1.place(x=115,y=390)
siignup_btn = Button(frame, width=6, text="Sign up", command=registration, bg='white', fg="#805033", border=0, cursor='hand2')
siignup_btn.place(x=260,y=390)

window.mainloop()
import tkinter as tk
from tkinter import *
from tkinter import messagebox as ms
import sqlite3
from PIL import Image, ImageTk
import re
import random
import os
import ast


root = tk.Tk()
root.geometry("1025x600+200+100")
root.title("Vedalingo")
root.configure(background="#fff")
root.resizable(False,False)


round_design = Image.open('round_design.png')
round_design  = round_design.resize((900,900), Image.ANTIALIAS)
img2 = ImageTk.PhotoImage(round_design)
Label(root,image=img2,bg='white').place(x=350,y=-150)


logo_img = Image.open('logo.png')
logo_img  = logo_img.resize((324,154), Image.ANTIALIAS)
img = ImageTk.PhotoImage(logo_img)
Label(root,image=img,bg='white').place(x=20,y=200)

frame= Frame(root,width=400,height=450,bg="white")
frame.place(x=500,y=70)

# Setting root icon of master root
root.iconbitmap("small_icon_logo.ico")

#Creating string for storing data
Email = tk.StringVar()
#WE HAVE CHANGED IntVar() TO STRINGVAR() because by default it was showing 0 in the box use int(tk.StringVar.get()) wherever int is required
Phoneno = tk.StringVar()
terms = tk.IntVar()
password = tk.StringVar()
password1 = tk.StringVar()


# database code
db = sqlite3.connect('resistration.db')
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS registration"
               "(Email TEXT, Phoneno TEXT, tnc TEXT, password TEXT)")
db.commit()

#defined a function to redirect to login page...this function is used in bottom button
def siignin():
    root.destroy()
    from subprocess import call
    call(["python","login.py"])


# To check if password satisfies some of the properties
#Length should be between 6 to 15
#Atleast one numeral, uppercase letter, lowercase letter
def password_check(passwd): 
	
	SpecialSym =['$', '@', '#'] 
	val = True
	
	if len(passwd) < 6: 
		print('length should be at least 6') 
		val = False
		
	if len(passwd) > 15: 
		print('length should be not be greater than 15') 
		val = False
		
	if not any(char.isdigit() for char in passwd): 
		print('Password should have at least one numeral') 
		val = False
		
	if not any(char.isupper() for char in passwd): 
		print('Password should have at least one uppercase letter') 
		val = False
		
	if not any(char.islower() for char in passwd): 
		print('Password should have at least one lowercase letter') 
		val = False
		
	if not any(char in SpecialSym for char in passwd): 
		print('Password should have at least one of the symbols $@#') 
		val = False
	if val: 
		return val 
    

#gender replaced with tnc
#gend with termsterms
def insert():
    email = Email.get()
    mobile = Phoneno.get()
    tnc = terms.get()
    pwd = password.get()
    cnpwd = password1.get()

    with sqlite3.connect('resistration.db') as db:
        c = db.cursor()

    # to check mail
    #Below format
    regex='^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
    #To check if email is as per format
    if (re.search(regex, email)):
        a = True
    else:
        a = False
        
    # validation for each field
    if (email == "") or (a == False):
        ms.showinfo("Message", "Please Enter valid email")
    elif((len(str(mobile)))<10 or len(str((mobile)))>10):
        ms.showinfo("Message", "Please Enter 10 digit mobile number")
    elif (pwd == ""):
        ms.showinfo("Message", "Please Enter valid password")
    elif (terms == 0):
        ms.showinfo("Message", "Please Accept terms and conditions")
    elif(pwd=="")or(password_check(pwd))!=True:
        ms.showinfo("Message", "password must contain atleast 1 uppercase letter, 1 symbol, 1 number")
    elif (pwd != cnpwd):
        ms.showinfo("Message", "Password and confirm password must be same")
    else:
        conn = sqlite3.connect('resistration.db')
        with conn:
            cursor = conn.cursor()
            cursor.execute(
                'INSERT INTO registration(Email, Phoneno, tnc, password) VALUES(?,?,?,?)',
                (email, mobile, tnc, pwd))

            conn.commit()
            db.close()
            ms.showinfo('Success!', 'Account Created Successfully! Details sent to your email')            
            root.destroy()
            from subprocess import call
            call(["python", "Login.py"])
            #sending our first argument of email id to cmd
            temp='python sendmail.py'+' '+email+' '+pwd+' '+'registered' #we send file name + email id
            os.system(temp)
          

#####################################################################################################################################################
  
# round boy image
sign_in_image = Image.open('hyy.png')
sign_in_image = sign_in_image.resize((75,75), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(sign_in_image)
sign_in_image_label = Label(frame, image=photo, bg='white')
sign_in_image_label.image = photo
sign_in_image_label.place(x=165, y=30)

# headline for signup page
l1 = Label(frame, text="Sign Up",fg='#805033',bg='white', font=("Microsoft Yahei UI Light", 23, "bold"))
l1.place(x=145, y=110)


#######################################################################



# Accepting email field
def on_enter(e):
    t2.delete(0,'end')
def on_leave(e):
    if t2.get()=='':
        t2.insert(0,'Email')

t2 = tk.Entry(frame,fg='black', border=0, textvar=Email, width=25, font=('Microsoft Yahei UI Light', 11))
t2.place(x=90, y=170)
t2.insert(0, 'Email')
t2.bind("<FocusIn>",on_enter)
t2.bind("<FocusOut>",on_leave)

# ===== Username icon =========
username_icon = Image.open('email.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(frame, image=photo, bg='white')
username_icon_label.image = photo
username_icon_label.place(x=60, y=170)

Frame(frame,width=290,height=2,bg='#805033').place(x=60,y=200)



#######################################################################


# Accepting phone number field
#below function is used to hide text description after clicking on the box
def on_enter(e):
    t4.delete(0,'end')
def on_leave(e):
    if t4.get()=='':
        t4.insert(0,'Contact Number')

t4 = tk.Entry(frame,fg='black', border=0, textvar=Phoneno, width=25, font=('Microsoft Yahei UI Light', 11))
t4.place(x=90, y=210)
t4.insert(0, 'Contact Number')
t4.bind("<FocusIn>",on_enter)
t4.bind("<FocusOut>",on_leave)

# ===== Username icon =========
username_icon = Image.open('call.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(frame, image=photo, bg='white')
username_icon_label.image = photo
username_icon_label.place(x=60, y=210)

Frame(frame,width=290,height=2,bg='#805033').place(x=60,y=240)

   
#######################################################################


# Accepting password field
#below function is used to hide text description after clicking on the box
def on_enter(e):
    t5.delete(0,'end')
def on_leave(e):
    if t5.get()=='':
        t5.insert(0,'Password')

t5 = tk.Entry(frame,fg='black', border=0, textvar=password, width=25, font=('Microsoft Yahei UI Light', 11))
t5.place(x=90, y=250)
t5.insert(0, 'Password')
t5.bind("<FocusIn>",on_enter)
t5.bind("<FocusOut>",on_leave)

# ===== Username icon =========
username_icon = Image.open('password.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(frame, image=photo, bg='white')
username_icon_label.image = photo
username_icon_label.place(x=60, y=250)


# ========= show/hide password ==================================================================
show_image = ImageTk.PhotoImage(file='show.png')
hide_image = ImageTk.PhotoImage(file='hide.png')

def show():
    hide_button = Button(frame, image=hide_image, command=hide, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
    hide_button.place(x=330, y=250)
    t5.config(show='')

def hide():
    show_button = Button(frame, image=show_image, command=show, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
    show_button.place(x=330, y=250)
    t5.config(show='•')

show_button = Button(frame, image=show_image, command=show, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
show_button.place(x=330, y=250)

Frame(frame,width=290,height=2,bg='#805033').place(x=60,y=280)


#######################################################################


# Accepting confirm-password field

def on_enter(e):
    t6.delete(0,'end')
def on_leave(e):
    if t6.get()=='':
        t6.insert(0,'Confirm password')

t6 = tk.Entry(frame,fg='black', border=0, textvar=password1, width=25, font=('Microsoft Yahei UI Light', 11))
t6.place(x=90, y=290)
t6.insert(0, 'Confirm password')
t6.bind("<FocusIn>",on_enter)
t6.bind("<FocusOut>",on_leave)

# ===== Username icon =========
username_icon = Image.open('check.png')
photo = ImageTk.PhotoImage(username_icon)
username_icon_label = Label(frame, image=photo, bg='white')
username_icon_label.image = photo
username_icon_label.place(x=60, y=290)

# ========= show/hide confirm password field ==================================================================
show_image2 = ImageTk.PhotoImage(file='show.png')
hide_image2 = ImageTk.PhotoImage(file='hide.png')

def show2():
    hide_button2 = Button(frame, image=hide_image2, command=hide2, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
    hide_button2.place(x=330, y=290)
    t6.config(show='')

def hide2():
    show_button2 = Button(frame, image=show_image2, command=show2, relief=FLAT,activebackground="white", borderwidth=0, background="white", cursor="hand2")
    show_button2.place(x=330, y=290)
    t6.config(show='•')

show_button2 = Button(frame, image=show_image2, command=show2, relief=FLAT, activebackground="white", borderwidth=0, background="white", cursor="hand2")
show_button2.place(x=330, y=290)

Frame(frame,width=290,height=2,bg='#805033').place(x=60,y=320)


#######################################################################

# Accepting tnc field
#tk.Radiobutton(frame, text="T&C", padx=5, width=30, fg='#805033', bg='white', font=("Microsoft Yahei UI Light", 11), variable=terms, value=1).place(x=100,y=325)
check_button = tk.Checkbutton(frame, text="I agree to the terms & conditions", variable=terms, onvalue=1, offvalue=0, font=("Microsoft Yahei UI Light", 9), bg='white', fg='black')
check_button.place(x=80, y=335)


###################################################################################3333
# Load google logo image
google_img = Image.open("google_logo.png")
google_img  = google_img.resize((20,20), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(google_img)

# Load google logo image
#google_img = Image.open("google_logo.png")
#google_img  = google_img.resize((20,20), Image.ANTIALIAS)
#photo = ImageTk.PhotoImage(google_img)

btn = Button(frame,width=40,pady=7, text="Sign up", bg="#805033", fg="white", border=0, command=insert, font=("Microsoft Yahei UI Light", 9)).place(x=60,y=380)
#btn2 = Button(frame,width=281,pady=7,image=photo,compound=tk.LEFT, text="Sign up with Google", fg="#805033",command=google_registration, border=0, font=("Microsoft Yahei UI Light", 9)).place(x=60,y=430)
label = Label(frame, text="I have an account",fg='black',bg="white", font=("Microsoft Yahei UI Light", 9))
label.place(x=150,y=510)
signin = Button(frame, width='6', text="Sign in",command=siignin, bg="white", cursor='hand2', fg='#805033',border=0)
signin.place(x=250,y=510)


root.mainloop()
import os,math
import random,sys
import smtplib
import sqlite3

#sys.argv[1] means first argument. Our first argument is email id.
#we can supply more than one argument for each email
user_email=sys.argv[1]
user_pswd=sys.argv[2]
email_type=sys.argv[3]

#user_email='atharvahindukaje2002@gmail.com'
#user_password=''
#email_type='forgot_password'


# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587)
s.starttls()    # start TLS for security
s.login("vedalingo@gmail.com", "joet ntlf svcp bwby") #Authentication 

#different types of messages for each code
if email_type=='registered':
    # message to be sent   
    SUBJECT = "Welcome to Vedalingo Family"   
    TEXT = "Your account details\n\n"+"Email: "+user_email+"\n\nPassword: "+user_pswd
    
if email_type=='loginsuccess':
    # message to be sent   
    SUBJECT = "login Successful"   
    TEXT = "Dear User, \n\nYou have successfully logged into your account."
    
if email_type=='forgot_password':
    # Establish Connection
    with sqlite3.connect('resistration.db') as db:
         c = db.cursor()
         db = sqlite3.connect('resistration.db')
         c.execute('SELECT password FROM registration WHERE email = ?', [user_email])
         result = c.fetchone()
   
         if result:
             pswd = str(result[0])
             SUBJECT = "Account Recovery"   
             TEXT = "Your account details\n\n"+"Email: "+user_email+"\n\nPassword: "+pswd

            # ===========================================
            #from subprocess import call
            #call(['python','login.py'])

            # ================================================
         else:
             print('')
        #conn.close() 
             
   
         
       
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT) 

# sending the mail    
s.sendmail('vedalingo@gmail.com', user_email, message)

# terminating the session    
s.quit()


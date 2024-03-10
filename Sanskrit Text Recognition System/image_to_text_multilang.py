import tkinter as tk
from tkinter import ttk
from PIL import Image , ImageTk
from tkinter.filedialog import askopenfilename
from google.cloud import vision
from textblob import TextBlob 
import tkinter.messagebox as messagebox
import requests
import speech_recognition as sr
from googletrans import Translator
from translate import Translator as trans
from gtts import gTTS
import os
import pygame
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import cv2
from PIL import Image
import fitz  # PyMuPDF
# Initialize pygame mixer
pygame.mixer.init()

root = tk.Tk()
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.resizable(False,False)
root.title("Vedalingo")

# Setting window icon of master window 
#p1 = ImageTk.PhotoImage(file = 'small_icon_logo.png') 
#root.iconphoto(True, p1) 
root.iconbitmap("small_icon_logo.ico")

####################################################################
# Background
image2 =Image.open('Background.jpg')
image2 =image2.resize((w,h), Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)
#lbl = tk.Label(root, text="Sanskrit Text Recognition System",justify='left', font=('Times', 30,'bold'), height=2, width=65 ,bg="White",fg="black")
#lbl.place(x=0, y=21)


global file
captured_image = None  # Define a global variable to store the captured image
os.environ['GOOGLE_APPLICATION_CREDENTIALS']='electricity-374907-14faa175fc81.json'

####################################################################

import io

from tempfile import NamedTemporaryFile

import tempfile

def upload_pdf():
    global file
    file = askopenfilename(initialdir=r'', title='Select PDF', filetypes=[("PDF files", "*.pdf")])

    try:
        # Open the PDF file
        pdf_document = fitz.open(file)

        # Create a Text widget for displaying the extracted text
        text_widget = tk.Text(root, wrap="word", width=80, height=20)
        text_widget.place(x=580, y=200)

        # Clear previous content in text widget
        text_widget.delete("1.0", tk.END)

        # Initialize combined text
        combined_text = ""

        # Iterate through each page in the PDF
        for page_num in range(len(pdf_document)):
            # Get the page
            page = pdf_document.load_page(page_num)

            # Render the page as an image
            pix = page.get_pixmap()

            # Save the image to a temporary file
            with tempfile.NamedTemporaryFile(delete=False, suffix=".png") as temp_file:
                pix.writePNG(temp_file.name)
                image_path = temp_file.name

            # Detect text in the image
            text = detect_text(image_path)

            # Append detected text to the combined text
            combined_text += text + '\n'

            # Delete the temporary file
            os.unlink(image_path)

        # Close the PDF document
        pdf_document.close()

        # Display combined text in text widget
        text_widget.insert(tk.END, combined_text)

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")



#THIS FUNCTION IS FOR GETTING OUR IMAGE
def Choose():
    global file
    file = askopenfilename(initialdir=r'', title='Select Image', filetypes=[("all files", "*.*")])
    image3 =Image.open(file)
    image3 =image3.resize((450,280), Image.ANTIALIAS)
    choosen_image=ImageTk.PhotoImage(image3)
    display = tk.Label(root, image=choosen_image)
    display.image= choosen_image
    display.place(x=50, y=250)
    
####################################################################

#This function is used by text_label function to detect text
def detect_text():
    global file
    """Detects text in the file."""
    from google.cloud  import vision
    
#    from google.cloud import types
    import io
    client = vision.ImageAnnotatorClient()
    with io.open(file, 'rb') as image_file:
        content = image_file.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    texts = response.text_annotations

    for text in texts:
        return text.description        

    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))
    
####################################################################

    
#   Creating buttons for all audios
def create_button(root, language, text, x, y):
    # Change label text to display full language name
    if language == "en":
        button_text = "English"
    elif language == "hi":
        button_text = "Hindi"
    elif language == "mr":
        button_text = "Marathi"
    button = tk.Button(root, text=button_text, command=lambda: create_audio(language, text), width=10, height=1, font=('times', 15, ' bold '), bg="yellow", fg="black")
    button.place(x=x, y=y)

####################################################################


def create_audio(language, text):
    def play():
        pygame.mixer.music.load(f"{language}.mp3")
        pygame.mixer.music.play(loops=0)
        
    def stop():
        pygame.mixer.music.stop()   
        
    translator = Translator()
    translated_text = translator.translate(text, dest=language).text
    tts = gTTS(text=translated_text, lang=language)
    tts.save(f"{language}.mp3")
    #os.system(f"{language}.mp3")
    with open(f"{language}.txt", 'w', encoding="utf-8") as f:
        f.write(translated_text)
        
    popup_window = tk.Toplevel(root)
    popup_window.geometry("725x500+200+100")
    popup_window.title(f"Translation") 
    #Setting window icon of popup window 
    popup_window.iconbitmap("small_icon_logo.ico")
    # Create a Text widget
    text_widget = tk.Text(popup_window, wrap="word", width=50, height=15)
    text_widget.pack(padx=10, pady=10)
    
    # Insert translated text into the Text widget
    text_widget.insert(tk.END, translated_text)
    #text_widget.place(x=200, y=200)
    
    # Create a vertical scrollbar and associate it with the Text widget
    scrollbar = tk.Scrollbar(popup_window, command=text_widget.yview)
    scrollbar.pack(side="right", fill="y")

    # Configure the Text widget to use the scrollbar
    text_widget.config(yscrollcommand=scrollbar.set)
    
    # Function to save the translated text as a PDF file
    def save_as_pdf():
        file_path = f"{language}_translation.pdf"
        translated_text = text_widget.get("1.0", "end-1c")
        #with open(file_path, "w", encoding="utf-8") as file:
         #   file.write(translated_text)
        # Create a canvas
        c = canvas.Canvas(file_path, pagesize=letter)
        # Set font and draw text
        c.setFont("Helvetica", 12)
        c.drawString(100, 700, translated_text)
        # Save the PDF file
        c.save() 
        messagebox.showinfo("Success", "PDF file saved successfully!")
        os.system(f"{language}_translation.pdf")
        
        
    def save_as_text():
        file_path = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            # Save text as a text file
            with open(file_path, "w") as file:
                file.write(translated_text)    
    
    # Create a button to save as PDF
    save_button = tk.Button(popup_window, text="Save as PDF", command=save_as_pdf)
    save_button.pack(side="left", padx=5, pady=5)
    
    save_text_button = tk.Button(popup_window, text="Save as Text", command=save_as_text)
    save_text_button.pack(side="left", padx=5, pady=5)
    
    save_text_button = tk.Button(popup_window, text="Play", command=play)
    save_text_button.pack(side="left", padx=5, pady=5)
    
    save_text_button = tk.Button(popup_window, text="Stop", command=stop)
    save_text_button.pack(side="left", padx=5, pady=5)
       

####################################################################

def Text_Label():
    #result of text detection is stored in variable
    result_text = detect_text()
    result_label = tk.Label(root,text=str(result_text),font=('Microsoft YaHei UI Light',12,'bold'),width=50,height=20,bg='white',fg='red')
    result_label.place(x=580,y=200)    
    
    # Create buttons for each language
    languages = ["en", "hi", "mr"]
    for i, language in enumerate(languages):
        create_button(root, language, result_text, x=1350, y=250 + i * 100)
        
    # Generate translations and store them in variables
    translator = Translator()
    translated_text_mr = translator.translate(result_text, dest='mr').text
    translated_text_hi = translator.translate(result_text, dest='hi').text
    translated_text_en = translator.translate(result_text, dest='en').text                           
    
    
###############################################################       
    
def TtoT():
    from subprocess import call
    call(["python","Text_translation.py"])

####################################################################    
    
def lang_id():
    from subprocess import call
    call(["python","detect_the_language.py"])  

####################################################################  
    
def book_library():
    from subprocess import call
    call(["python","Book_Library.py"])  

####################################################################       
    
def explore():
    from subprocess import call
    call(["python","explore.py"])  

####################################################################    
    
def Exit():
    if mbox.askokcancel("Exit", "Do you want to exit?"):
        root.destroy()

####################################################################

button1 = tk.Button(root,text='Upload Image',command=Choose,font=('Microsoft YaHei UI Light',12,'bold'),width=18,bg='white',fg='black')
button1.place(x=50,y=700)

button1 = tk.Button(root,text='Upload pdf',command=upload_pdf,font=('Microsoft YaHei UI Light',12,'bold'),width=18,bg='white',fg='black')
button1.place(x=50,y=650)

button2 = tk.Button(root,text="Detect Text",command=Text_Label,font=('Microsoft YaHei UI Light',12,'bold'),width=18,bg='white',fg='black')
button2.place(x=280,y=700)

button3 = tk.Button(root,text="Identify",command=lang_id,font=('Microsoft YaHei UI Light',12,'bold'),width=18,bg='black',fg='white')
button3.place(x=510,y=50)

button4 = tk.Button(root,text="Translate",command=TtoT,font=('Microsoft YaHei UI Light',12,'bold'),width=18,bg='black',fg='white')
button4.place(x=740,y=50)

button4 = tk.Button(root,text="Library",command=book_library,font=('Microsoft YaHei UI Light',12,'bold'),width=18,bg='black',fg='white')
button4.place(x=970,y=50)

button4 = tk.Button(root,text="Explore",command=explore,font=('Microsoft YaHei UI Light',12,'bold'),width=18,bg='black',fg='white')
button4.place(x=1200,y=50)

exit = tk.Button(root, text="Exit", command=Exit,height=1, font=('Microsoft YaHei UI Light',10,'bold'),width=10,bg='red',fg='white', borderwidth=0, cursor="hand2")
exit.place(x=1400,y=700)


root.mainloop()


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

# Setting window icon of master window 
root.iconbitmap("small_icon_logo.ico")


####################################################################

#Brown Background Image
image2 =Image.open('Background.jpg')
image2 =image2.resize((1025,600), Image.ANTIALIAS)
background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=0)
lbl = tk.Label(root, text="Explore literary treasure!",justify='left', font=('Times', 30,'bold'), height=2, width=45 ,bg="White",fg="black")
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


#Functions for downloading
class DownloadManager:
    def __init__(self, filename):
        self.filename = filename
      
        self.stop_flag = False

    def download(self):
        total_size = os.path.getsize(self.filename)

        print("Download started for:", self.filename)  # Debug print
        with open(self.filename, 'rb') as f:
            while True:
                if self.stop_flag:
                    break
                data = f.read(1024)
                if not data:
                    break
                
        if not self.stop_flag:
            print("Download complete for:", self.filename)  # Debug print
            messagebox.showinfo("Download Complete", "The book has been successfully downloaded!")

def download_book(selected_book):
    if selected_book:
        book_path = os.path.join("books", selected_book)
        download_manager = DownloadManager(book_path)
        download_thread = Thread(target=download_manager.download)
        download_thread.start()

def on_book_click(event):
    item = event.widget.identify('item', event.x, event.y)
    selected_book = event.widget.item(item, 'text')
    download_book(selected_book)

# Assume books are stored in a directory called "books"
books = os.listdir("books")

for idx, book in enumerate(books):
    book_path = os.path.join("books", book)
    if os.path.isfile(book_path) and book.lower().endswith(('.jpg', '.jpeg', '.png')):
        with Image.open(book_path) as img:
            img = img.resize((100, 150), Image.ANTIALIAS)
            photo = ImageTk.PhotoImage(img)
            book_button = tk.Button(frame, image=photo, command=lambda book=book: download_book(book))
            book_button.image = photo
            book_button.grid(row=idx // 6, column=idx % 6, padx=15, pady=15) #book_buttons means images



root.mainloop()

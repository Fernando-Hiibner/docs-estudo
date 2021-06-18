from pathlib import Path
from PIL import Image, ImageTk
import tkinter as tk
from tkinter.constants import *
from tkinter.scrolledtext import ScrolledText
from tkinter.filedialog import askdirectory, askopenfilename


class App:
    def __init__(self, image_file_extensions):
        self.root = tk.Tk()
        self.image_folder_path = askdirectory()
        self.image_file_extensions = image_file_extensions
        self.create_widgets()
        self.root.mainloop()

    def create_widgets(self):
        self.list_btn = tk.Button(self.root, text='List Images', command=self.list_images)
        self.list_btn.grid(row=0, column=0)
        self.show_btn = tk.Button(self.root, text='Show Images', command=self.show_images)
        self.show_btn.grid(row=1, column=0)

        self.text = ScrolledText(self.root, wrap=WORD)
        self.text.grid(row=2, column=0, padx=10, pady=10)

        self.text.bind("<Alt-d>", lambda event: self.showDump())
        self.text.bind("<Alt-t>", lambda event: self.testeRead())
        self.text.bind("<Alt-i>", lambda event: self.insertImage())

        self.text.image_filenames = []
        self.text.images = []

    def list_images(self):
        ''' Create and display a list of the images the in folder that have one
            of the specified extensions. '''
        self.text.image_filenames.clear()
        for filepath in Path(self.image_folder_path).iterdir():
            if filepath.suffix in self.image_file_extensions:
                self.text.insert(INSERT, filepath.name+'\n')
                self.text.image_filenames.append(filepath)

    def show_images(self):
        ''' Show the listed image names along with the images themselves. '''
        self.text.delete('1.0', END)  # Clear current contents.
        self.text.images.clear()
        # Display images in Text widget.
        for image_file_path in self.text.image_filenames:
            img = Image.open(image_file_path).resize((64, 64), Image.ANTIALIAS)
            img = ImageTk.PhotoImage(img)
            self.text.insert(INSERT, image_file_path.name+'\n')
            self.text.image_create(INSERT, padx=5, pady=5, image=img)
            self.text.images.append(img)  # Keep a reference.
            self.text.insert(INSERT, '\n')

    def insertImage(self):
        self.text.delete('1.0', END)  # Clear current contents.
        self.text.images.clear()

        image_file_path_name = askopenfilename()
        img = tk.PhotoImage(file=image_file_path_name)
        self.text.insert(INSERT, image_file_path_name+'\n')
        self.text.image_create(INSERT, padx=5, pady=5, image=img)
        self.text.images.append(img)  # Keep a reference.
        self.text.insert(INSERT, '\n')

    def showDump(self):
        print(self.text.dump("1.0", END))
        print(self.text.dump("1.0", END, image=True))
        with open("Teste.txt", "w", encoding="utf-8") as oi:
            for image in self.text.images:
                image.write("Teste.png", format="png")
            oi.close()
    def testeRead(self):
        image = Image.open("pyimage1.gif")
        print(type(image))



image_file_extensions = {'.jpg', '.png'}
App(image_file_extensions)
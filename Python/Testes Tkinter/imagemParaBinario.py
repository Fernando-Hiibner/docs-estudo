import io
from PIL import Image
import tkinter as tk
from tkinter.filedialog import askdirectory, askopenfilename

#Fontes
# https://www.kite.com/python/docs/io.BytesIO
# kite.com/python/answers/how-to-convert-an-image-to-a-string-in-python
# https://www.geeksforgeeks.org/python-convert-image-to-string-and-vice-versa/

tk.Tk().withdraw()

an_image = Image.open(askopenfilename())

output = io.BytesIO()
an_image.save(output, format="png")
image_as_string = output.getvalue()

print(image_as_string [:20])


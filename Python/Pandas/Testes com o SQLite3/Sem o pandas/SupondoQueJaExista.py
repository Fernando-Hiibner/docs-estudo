from tkinter import Tk
from tkinter.filedialog import askopenfilename

import sqlite3 as sl

Tk().withdraw()
dbPath = askopenfilename(title='Choose DB file to open', filetypes=( ("DB (*.db)", "*.db"), ("All files", "*.*")))

con = sl.connect(dbPath)

with con:
    read = con.execute("select * from testeBrabo")
    for row in read:
        print(row)
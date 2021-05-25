import pandas as pd
import sqlite3 as sl

from tkinter import Tk
from tkinter.filedialog import askopenfilename

simbols = pd.DataFrame({
        "Matemática":   ["Ω", "π", "√", "≠"],
        "Matemática 2": ["⁰", "¹", "²", "³"],
        "Frações":      ["⅟", "¼", "½", "¾"],
        "Setas":        ["←", "→", "↑", "↓"],
        "Quadrados":    ["▢", "▥", "■", "▣"],
        "Triangulos":   ["▲", "◀", "▶", "▼"],
        "Circulos":     ["◌", "●", "○", "◍"],
        "Porções":      ["◖", "◗", "◓", "◐"]})

con = sl.connect("testes.db")

simbols.to_sql("SIMBOLS", con)

with con:
    read = con.execute("select * from SIMBOLS")
    for row in read:
        print(row)
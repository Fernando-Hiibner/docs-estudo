import pandas as pd
import pyodbc as db

from tkinter import Tk
from tkinter.filedialog import askopenfilename

simbols = pd.DataFrame({
        "Matematica":   ["Ω", "π", "√", "≠"],
        "Matematica2": ["⁰", "¹", "²", "³"],
        "Fracoes":      ["⅟", "¼", "½", "¾"],
        "Setas":        ["←", "→", "↑", "↓"],
        "Quadrados":    ["▢", "▥", "■", "▣"],
        "Triangulos":   ["▲", "◀", "▶", "▼"],
        "Circulos":     ["◌", "●", "○", "◍"],
        "Porcoes":      ["◖", "◗", "◓", "◐"]}, columns=['Matematica', 'Matematica2', 'Fracoes', 'Setas', 'Quadrados', 'Triangulos', 'Circulos', 'Porcoes'])

connection = db.connect('Driver={SQL Server};'
                      'Server=C1D4KF5KF2-0639\MSSQLSERVER01;'
                      'Database=TestesPandas;'
                      'Trusted_Connection=yes;')
cursor = connection.cursor()

'''cursor.execute(
    """
        create table SIMBOLOS
        (
            id INT PRIMARY KEY IDENTITY(1,1),
            Matematica VARCHAR(1) UNIQUE NOT NULL,
            Matematica2 VARCHAR(1) UNIQUE NOT NULL,
            Fracoes VARCHAR(1) UNIQUE NOT NULL,
            Setas VARCHAR(1) UNIQUE NOT NULL,
            Quadrados VARCHAR(1) UNIQUE NOT NULL,
            Triangulos VARCHAR(1) UNIQUE NOT NULL,
            Circulos VARCHAR(1) UNIQUE NOT NULL,
            Porcoes VARCHAR(1) UNIQUE NOT NULL
        );
    """
)

for row in simbols.itertuples():
    cursor.execute(
        """
            insert into SIMBOLOS(Matematica, Matematica2, Fracoes, Setas, Quadrados, Triangulos, Circulos, Porcoes) values (?,?,?,?,?,?,?,?)
        """,
        row.Matematica,
        row.Matematica2,
        row.Fracoes,
        row.Setas,
        row.Quadrados,
        row.Triangulos,
        row.Circulos,
        row.Porcoes
        )
'''
textConfig = {
    "tab": '1c', 
    "bg": 'SystemWindow', 
    "fg": 'black',
    "selectbackground": '#dddddd', 
    "selectforeground": 'black', 
    "insertbackground": 'black'}
textConfig = pd.DataFrame(textConfig, 
    columns=textConfig.keys(),
    index=[0])

cursor.execute(
    """
        create table textConfig
        (
            id INT PRIMARY KEY IDENTITY(1,1),
            tab VARCHAR(5) NOT NULL,
            bg VARCHAR(15) NOT NULL,
            fg VARCHAR(15) NOT NULL,
            selectbackground VARCHAR(15) NOT NULL,
            selectforeground VARCHAR(15) NOT NULL,
            insertbackground VARCHAR(15) NOT NULL,
        );
    """
)

for row in textConfig.itertuples():
    cursor.execute(
        """
            insert into textConfig(tab, bg, fg, selectbackground, selectforeground, insertbackground) values (?,?,?,?,?,?)
        """,
        row.tab,
        row.bg,
        row.fg,
        row.selectbackground,
        row.selectforeground,
        row.insertbackground
        )

connection.commit()
import pandas as pd
import pyodbc as db
from tkinter import Tk
from tkinter.filedialog import askopenfilename

Tk().withdraw()
rawDataPath = askopenfilename(title='Choose CSV file to open', filetypes=( ("CSV (*.csv)", "*.csv"), ("All files", "*.*")))
rawData = pd.read_csv(rawDataPath, sep = ';')
dfData = pd.DataFrame(rawData, columns=["Nome", "Descricao1", "Descricao2", "OBS"])
dfData = dfData.where(dfData.notnull(), None)


connection = db.connect('Driver={SQL Server};'
                      'Server=C1D4KF5KF2-0639\MSSQLSERVER01;'
                      'Database=TesteSQL;'
                      'Trusted_Connection=yes;')
cursor = connection.cursor()

for row in dfData.itertuples():
    cursor.execute("""INSERT INTO TesteSQL.dbo.TINF_INFTAB (TABI_NOM, TABI_DESPRI, TABI_DESSEC, TABI_OBS)
                    VALUES (?,?,?,?)
                    """,
                    row.Nome, 
                    row.Descricao1,
                    row.Descricao2,
                    row.OBS
                )
connection.commit()
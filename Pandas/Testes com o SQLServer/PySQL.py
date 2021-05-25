from ast import literal_eval
from numpy import insert
import pandas as pd
from pandas.core.frame import DataFrame
import pyodbc as db

import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkST
from tkinter.filedialog import FileDialog

class SQL():
    def __init__(self):
        self.connection = db.connect('Driver={SQL Server};'
                            'Server=C1D4KF5KF2-0639\MSSQLSERVER01;'
                            'Database=TestesPandas;'
                            'Trusted_Connection=yes;')
        self.cursor = self.connection.cursor()
        self.dtFrame = None
        self.tName = None
    

    #Fonte: https://stackoverflow.com/questions/31071952/generate-sql-statements-from-a-pandas-dataframe
    def criarSchema(self):
        schema = pd.io.sql.get_schema(self.dtFrame.reset_index(), self.tName)  
        return schema

    def criarInsert(self):
        schema = self.criarSchema()
        name = ""
        indexInit = None
        for index in range(0, len(schema)):
            if schema[index] == "\"" and indexInit == None:
                indexInit = index
            elif schema[index] != "\"" and indexInit != None:
                name += schema[index]
            elif schema[index] == "\"" and indexInit != None:
                break
        if name != self.tName:
            self.tName = name
        insert = ""
        for index, row in self.dtFrame.iterrows():
            if str(tuple(row.values)).endswith(",)"):
                valuesTuple = str(tuple(row.values)).strip(",)")
                valuesTuple += ")"
            else:
                valuesTuple = str(tuple(row.values))       
            insert += 'INSERT INTO '+self.tName+' ('+ str(', '.join(self.dtFrame.columns))+ ') VALUES '+ valuesTuple
        return insert

    def converterDictParaDT(self, dictCon, tableName = None, outputText = None, createText = None, insertText = None):
        try:
            dictCon = literal_eval(dictCon)
            self.dtFrame = pd.DataFrame([dictCon], columns=dictCon.keys(), index = [0])
            if tableName != None and tableName != '':
                self.tName = tableName
            else:
                self.tName = "NomeDaTabela"
            if outputText != None:
                outputText.config(state = 'normal')
                outputText.delete("1.0","end")
                outputText.insert("1.0", self.dtFrame.to_string())
                outputText.config(state = 'disable')
            if createText != None:
                createText.delete("1.0","end")
                createText.insert("1.0", self.criarSchema())
            if insertText != None:
                insertText.delete("1.0","end")
                insertText.insert("1.0", self.criarInsert())
        except Exception as e:
            print("Erro: ",e)
    def criarTabela(self, sql, insertText = None):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            if insertText != None:
                insertText.delete("1.0","end")
                insertText.insert("1.0", self.criarInsert())
        except Exception as e:
            print("Erro: ", e)
    def insertInto(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("Erro: ", e)



sl = SQL()

root = tk.Tk()
#root.resizable(False, False)
root.title("PySQL")
tabControl = ttk.Notebook(root)

convert = ttk.Frame(tabControl)
createTable = ttk.Frame(tabControl)
insertInto = ttk.Frame(tabControl)

tabControl.add(convert, text = "Converter")
tabControl.add(createTable, text = "Criar Tabela")
tabControl.add(insertInto, text = "Inserir na Tabela")

tabControl.pack(expand = 1, fill = "both", padx = 5, pady = 5)

#convert
convertHolderIO = ttk.Frame(convert)
convertHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')
convertHolderButton = ttk.Frame(convert)
convertHolderButton.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')


entryTextConvert = tkST.ScrolledText(convertHolderIO, tabs = ('1c'), width = 75, height = 10)
entryTextConvert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

outputTextConvert = tkST.ScrolledText(convertHolderIO, tabs = ('1c'), state = 'disable', width = 75, height = 10)
outputTextConvert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

entryTableLabel = tk.Label(convertHolderButton, text = "Nome da tabela")
entryTableLabel.pack(side = 'left', anchor = 'nw', pady = 5)
entryTableName = tk.Entry(convertHolderButton)
entryTableName.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, fill = 'x')

convertButton = ttk.Button(convertHolderButton, text="Converter")
convertButton.pack(side = 'bottom', anchor = 'se', padx = 5, pady = 5)

#createTable
createHolderIO = ttk.Frame(createTable)
createHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')

entryTextCreate = tkST.ScrolledText(createHolderIO, tabs = ('1c'), width = 75, height = 10)
entryTextCreate.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

createButton = ttk.Button(createTable, text="Criar")
createButton.pack(side = 'left', anchor = 'ne', padx = 5, pady = 5)

#insertTable
insertHolderIO = ttk.Frame(insertInto)
insertHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')

entryTextInsert = tkST.ScrolledText(insertHolderIO, tabs = ('1c'), width = 75, height = 10)
entryTextInsert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

insertButton = ttk.Button(insertInto, text="Inserir")
insertButton.pack(side = 'left', anchor = 'ne', padx = 5, pady = 5)

convertButton.config(command=lambda: sl.converterDictParaDT(entryTextConvert.get('1.0','end'), entryTableName.get(), outputTextConvert, entryTextCreate, entryTextInsert))
createButton.config(command=lambda: sl.criarTabela(entryTextCreate.get("1.0","end"), entryTextInsert))
insertButton.config(command=lambda: sl.insertInto(entryTextInsert.get("1.0","end")))

root.mainloop()
'''
{
	"tab": '1c', 
	"bg": 'SystemWindow', 
	"fg": 'black',
	"selectbackground": '#dddddd', 
	"selectforeground": 'black', 
	"insertbackground": 'black'
}
'''

    
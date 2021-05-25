from ast import literal_eval
import re
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
            print("Erro:",e)
    def criarTabela(self, sql, insertText = None):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            if insertText != None:
                insertText.delete("1.0","end")
                insertText.insert("1.0", self.criarInsert())
        except Exception as e:
            print("Erro:", e)
    def insertInto(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("Erro:", e)

    def queryDB(self, sql, outputText = None):
        try:
            out = pd.read_sql(sql, self.connection)
            if outputText != None:
                outputText.config(state = 'normal')
                outputText.delete("1.0","end")
                outputText.insert("1.0", out)
                outputText.config(state = 'disable')
        except Exception as e:
            print("Erro:",e)

class Root(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.SQL = SQL()
        self.title("PySQL")

        self.tabControl = ttk.Notebook(self)
        
        self.convert = ttk.Frame(self.tabControl)
        self.createTable = ttk.Frame(self.tabControl)
        self.insertInto = ttk.Frame(self.tabControl)
        self.queryTab = ttk.Frame(self.tabControl)

        self.tabControl.add(self.convert, text = "Converter")
        self.tabControl.add(self.createTable, text = "Criar Tabela")
        self.tabControl.add(self.insertInto, text = "Inserir na Tabela")
        self.tabControl.add(self.queryTab, text = "Consulta")

        self.tabControl.pack(expand = 1, fill = "both", padx = 5, pady = 5)

        self.createConvertTab()
        self.createCreateTab()
        self.createInsertTab()
        self.createQuery()
        self.configButtons()
        
        self.mainloop()
    def createConvertTab(self):
        self.convertHolderIO = ttk.Frame(self.convert)
        self.convertHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')
        self.convertHolderButton = ttk.Frame(self.convert)
        self.convertHolderButton.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')

        self.entryTextConvert = tkST.ScrolledText(self.convertHolderIO, tabs = ('1c'), width = 75, height = 10)
        self.entryTextConvert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.outputTextConvert = tkST.ScrolledText(self.convertHolderIO, tabs = ('1c'), state = 'disable', width = 75, height = 10)
        self.outputTextConvert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.entryTableLabel = tk.Label(self.convertHolderButton, text = "Nome da tabela")
        self.entryTableLabel.pack(side = 'left', anchor = 'nw', pady = 5)
        self.entryTableName = tk.Entry(self.convertHolderButton)
        self.entryTableName.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, fill = 'x')

        self.convertButton = ttk.Button(self.convertHolderButton, text="Converter")
        self.convertButton.pack(side = 'bottom', anchor = 'se', padx = 5, pady = 5)
    def createCreateTab(self):
        self.createHolderIO = ttk.Frame(self.createTable)
        self.createHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')

        self.entryTextCreate = tkST.ScrolledText(self.createHolderIO, tabs = ('1c'), width = 75, height = 10)
        self.entryTextCreate.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.createButton = ttk.Button(self.createTable, text="Criar")
        self.createButton.pack(side = 'left', anchor = 'ne', padx = 5, pady = 5)
    def createInsertTab(self):
        self.insertHolderIO = ttk.Frame(self.insertInto)
        self.insertHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')

        self.entryTextInsert = tkST.ScrolledText(self.insertHolderIO, tabs = ('1c'), width = 75, height = 10)
        self.entryTextInsert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.insertButton = ttk.Button(self.insertInto, text="Inserir")
        self.insertButton.pack(side = 'left', anchor = 'ne', padx = 5, pady = 5)
    def createQuery(self):
        self.queryHolderIO = ttk.Frame(self.queryTab)
        self.queryHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')

        self.queryEntryText = tkST.ScrolledText(self.queryHolderIO, tabs = ('1c'), width = 75, height = 10)
        self.queryEntryText.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.queryOutText = tkST.ScrolledText(self.queryHolderIO, tabs = ('1c'), state = 'disable', width = 75, height = 10)
        self.queryOutText.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.queryButton = ttk.Button(self.queryTab, text="Consultar")
        self.queryButton.pack(side = 'left', anchor = 'ne', padx = 5, pady = 5)

    def configButtons(self):
        self.convertButton.config(command=lambda: self.SQL.converterDictParaDT(self.entryTextConvert.get('1.0','end'), self.entryTableName.get(), self.outputTextConvert, self.entryTextCreate, self.entryTextInsert))
        self.createButton.config(command=lambda: self.SQL.criarTabela(self.entryTextCreate.get("1.0","end"), self.entryTextInsert))
        self.insertButton.config(command=lambda: self.SQL.insertInto(self.entryTextInsert.get("1.0","end")))
        self.queryButton.config(command=lambda: self.SQL.queryDB(self.queryEntryText.get("1.0","end"), self.queryOutText))

if __name__ == "__main__":
    Root()
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

    
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror, showinfo

import pandas as pd
import pyodbc as db

import re
from ast import literal_eval


class SQL(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title = "Connect"
        self.resizable(False, False)
        self.protocol("WM_DELETE_WINDOW", quit)
        
        self.titleGrid = tk.Frame(self)
        self.titleGrid.pack(side = "top", padx = 5, pady = 5)
        self.titleLabel = tk.Label(self, text = "PySQL")
        self.titleLabel.pack(side = 'top', fill = 'x', anchor = 'center')

        self.mainGrid = tk.Frame(self)
        self.mainGrid.pack(side = "top", padx = 5)
        self.mainGridL = tk.Frame(self.mainGrid)
        self.mainGridL.pack(side = "left")
        self.mainGridR = tk.Frame(self.mainGrid)
        self.mainGridR.pack(side = "right")
        
        self.driverLabel = tk.Label(self.mainGridL, text =   "Driver: ")
        self.driverLabel.pack(side = "top")
        self.serverLabel = tk.Label(self.mainGridL, text =   "Server: ")
        self.serverLabel.pack(side = "top")
        self.databaseLabel = tk.Label(self.mainGridL, text = "Database: ")
        self.databaseLabel.pack(side = "top")

        self.driverEntry = tk.Entry(self.mainGridR)
        self.driverEntry.pack(side = "top")
        self.driverEntry.insert(0, "{SQL Server}")
        self.serverEntry = tk.Entry(self.mainGridR)
        self.serverEntry.pack(side = "top")
        self.serverEntry.insert(0, "C1D4KF5KF2-0639\MSSQLSERVER01")
        self.databaseEntry = tk.Entry(self.mainGridR)
        self.databaseEntry.pack(side = "top")
        self.databaseEntry.insert(0, "TesteSQL")

        self.buttonGrid = tk.Frame(self)
        self.buttonGrid.pack(side = 'top', padx = 5, pady = 5)
        self.connectButton = ttk.Button(self.buttonGrid, text = "Conectar", command=lambda: self.connect())
        self.connectButton.pack(side = 'left', fill = 'x')
        self.exitButton = ttk.Button(self.buttonGrid, text = "Sair", command=lambda: quit())
        self.exitButton.pack(side = 'left', fill = 'x')

        self.mainloop()

        self.dtFrame = None
        self.tName = None

        self.lastSchema = None
        self.lastInsert = None

    def connect(self):
        try:
            self.connection = db.connect('Driver='+self.driverEntry.get()+
                        ';Server='+self.serverEntry.get()+
                        ';Database='+self.databaseEntry.get()+
                        ';Trusted_Connection=yes;', timeout = 1)
            self.cursor = self.connection.cursor()
            self.destroy()
        except:
            showerror("Erro", "Erro, cheque os dados de entrada")
    #Fonte: https://stackoverflow.com/questions/31071952/generate-sql-statements-from-a-pandas-dataframe
    def criarSchema(self):
        self.lastSchema = pd.io.sql.get_schema(self.dtFrame.reset_index(), self.tName, con = self.connection)
        return self.lastSchema

    def criarInsert(self):
        #Checa se o nome da tabela mudou desde que o ultimo Schema foi criado, e usa esse novo nome no Insert
        if self.lastSchema != None:
            name = ""
            indexInit = None
            for index in range(0, len(self.lastSchema)):
                if self.lastSchema[index] == "\"" and indexInit == None:
                    indexInit = index
                elif self.lastSchema[index] != "\"" and indexInit != None:
                    name += self.lastSchema[index]
                elif self.lastSchema[index] == "\"" and indexInit != None:
                    break
            if name != self.tName:
                self.tName = name

        #Essa parte gera um insert into que vai ser tipo assim:
        #insert into Teste(teste1, teste2) values ('teste1', 'teste2')
        #Porem se o nosso dicionario python for um dicionario de listas, vai dar problema
        #insert into Teste(teste1, teste2) values (['teste1','teste2'], ['teste3','teste4'])
        insert = ""
        for index, row in self.dtFrame.iterrows():
            if str(tuple(row.values)).endswith(",)"):
                values = str(tuple(row.values)).strip(",)")
                values += ")"
            else:
                values = str(tuple(row.values))       
            insert += 'INSERT INTO '+self.tName+' ('+ str(', '.join(self.dtFrame.columns))+ ') VALUES '+ values
        #Essa parte aqui resolve esse porem dos dicionarios com lista
        valuesIndex = re.search('values \(', insert, flags=re.IGNORECASE)
        valuesTuple = tuple(literal_eval("("+insert[valuesIndex.end()::]))
        if type(valuesTuple[0]) == list or type(valuesTuple[0]) == set:
            _newValuesTuple = list()
            for i in range(len(valuesTuple[0])):
                _list = list()
                for j in range(len(valuesTuple)):
                    _list.append(list(valuesTuple[j])[i])
                _newValuesTuple.append(_list)
            _valuesTuple = ""
            _valuesTupleSize = len(_newValuesTuple)-1
            _index = 0
            for _valuesList in _newValuesTuple:
                _tuple = tuple(_valuesList)
                if(_index != _valuesTupleSize):
                    _valuesTuple += str(_tuple)+", "
                else:
                    _valuesTuple += str(_tuple)
                _index += 1
            _valuesTuple = "values "+_valuesTuple
            insert = insert[0:valuesIndex.start()]+_valuesTuple
        return insert
    
    def writeTree(self, sql, outputText):
        for element in outputText.get_children():
            outputText.delete(element)
        col = list(sql.columns)
        outputText["columns"] = col

        outputText.column('#0', width=0, stretch='no')
        outputText.heading('#0', text='', anchor='w')
        
        for c in col:
            outputText.column(c, anchor="w", width = 100, stretch = 'no')
            outputText.heading(c, text=c, anchor = "w")
        end = 0
        for index, row in sql.iterrows():
            outputText.insert("",end,text=index,values=list(row))
            end += 1

    def converterDictParaDT(self, dictCon, tableName = None, textDict = None, controlVarDict = None):
        try:
            if tableName != None and tableName != '':
                self.tName = tableName
            else:
                self.tName = "NomeDaTabela"

            dictCon = literal_eval(dictCon)
            self.dtFrame = pd.DataFrame([dictCon], columns=dictCon.keys(), index=[0])

            if 'outputText' in textDict.keys() and 'outC' in controlVarDict.keys():
                outputText = textDict.pop('outputText')
                self.dtFrameForPrinting = pd.DataFrame.from_dict(dictCon, orient='index').transpose()
                if controlVarDict.pop('outC') == 1:
                    self.writeTree(self.dtFrameForPrinting, outputText)
            if 'createText' in textDict.keys() and 'schemaC' in controlVarDict.keys():
                createText = textDict.pop('createText')
                if controlVarDict.pop('schemaC') == 1:
                    createText.delete("1.0","end")
                    createText.insert("1.0", self.criarSchema())
            if 'insertText' in textDict.keys() and 'insertC' in controlVarDict.keys():
                insertText = textDict.pop('insertText')
                if controlVarDict.pop('insertC') == 1:
                    insertText.delete("1.0","end")
                    insertText.insert("1.0", self.criarInsert())
        except Exception as e:
            showerror("Erro:",e)
    def criarTabela(self, sql, insertText = None, insertControl = None):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            if insertText != None and insertControl == 1:
                insertText.delete("1.0","end")
                insertText.insert("1.0", self.criarInsert())
        except Exception as e:
            showerror("Erro:",e)
    def insertInto(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            showerror("Erro:",e)

    def queryDB(self, sql, outputText = None):
        if not sql.startswith("SET NOCOUNT ON") and not sql.startswith("set nocount on"):
            sql = "SET NOCOUNT ON;\n"+sql
        sql = sql.split(";")
        try:
            for sqlQuery in sql:
                if sqlQuery not in ['\n', '\t']:
                    sqlQuery = sqlQuery+";"
                    self.cursor.execute(sqlQuery)
                    self.connection.commit()
                    try:
                        out = pd.read_sql(sqlQuery, self.connection)
                        if outputText != None:
                            self.writeTree(out, outputText)
                        showinfo("Sucesso","Operação concluida!\n"+sqlQuery)
                        
                    except:
                        showinfo("Sucesso","Operação concluida!\n"+sqlQuery)
        except db.ProgrammingError as e:
            showerror("Erro:",e)

if __name__ == "__main__":
    showerror("Erro", "Por favor execute \"main.py\"")
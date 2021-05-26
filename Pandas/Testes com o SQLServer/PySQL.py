from ast import literal_eval
import pandas as pd
import pyodbc as db

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror
import tkinter.scrolledtext as tkST

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

        self.dtDict = None
        self.dtFrame = None
        self.tName = None

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

    def converterDictParaDT(self, dictCon, tableName = None, textDict = None, controlVarDict = None):
        try:
            dictCon = literal_eval(dictCon)
            self.dtFrame = pd.DataFrame([dictCon], columns=dictCon.keys(), index = [0])
            self.dtDict = dictCon
            if tableName != None and tableName != '':
                self.tName = tableName
            else:
                self.tName = "NomeDaTabela"
            if 'outputText' in textDict.keys() and 'outC' in controlVarDict.keys():
                outputText = textDict.pop('outputText')
                if controlVarDict.pop('outC') == 1:
                    for element in outputText.get_children():
                        outputText.delete(element)
                    cols = list(self.dtFrame.columns)
                    outputText["columns"] = cols

                    outputText.column('#0', width=0, stretch='no')
                    outputText.heading('#0', text='', anchor='w')
                    
                    for col in cols:
                        outputText.column(col, anchor="w", width = 100, stretch = 'no')
                        outputText.heading(col, text=col, anchor = "w")
                    end = 0
                    for index, row in self.dtFrame.iterrows():
                        outputText.insert("",end,text=index,values=list(row))
                        end += 1
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
            print("Erro:",e)
    def criarTabela(self, sql, insertText = None, insertControl = None):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            if insertText != None and insertControl == 1:
                insertText.delete("1.0","end")
                insertText.insert("1.0", self.criarInsert())
        except Exception as e:
            print("Erro:", e)
    def insertInto(self, sql):
        try:
            if self.dtDict != None:
                for value in self.dtDict.values():
                    if type(value) == "<class 'list'>":
                        print("OI")
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            print("Erro:", e)

    def queryDB(self, sql, outputText = None):
        try:
            out = pd.read_sql(sql, self.connection)
            if outputText != None:
                for element in outputText.get_children():
                        outputText.delete(element)
                col = list(out.columns)
                outputText["columns"] = col

                outputText.column('#0', width=0, stretch='no')
                outputText.heading('#0', text='', anchor='w')
                
                for c in col:
                    outputText.column(c, anchor="w", width = 100, stretch = 'no')
                    outputText.heading(c, text=c, anchor = "w")
                end = 0
                for index, row in out.iterrows():
                    outputText.insert("",end,text=index,values=list(row))
                    end += 1
        except Exception as e:
            print("Erro:",e)

class Root(tk.Tk):
    def __init__(self, SQLConnection):
        tk.Tk.__init__(self)
        self.SQL = SQLConnection
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

        self.controlVarOutC = tk.IntVar()
        self.controlVarSchemaC = tk.IntVar()
        self.controlVarInsertC = tk.IntVar()
        self.controlVarInsertI = tk.IntVar()

        self.controlVarOutC.set(1)

        self.createConvertTab()
        self.createCreateTab()
        self.createInsertTab()
        self.createQuery()
        self.configButtons()
        
        self.mainloop()
    def createConvertTab(self):
        self.convertPanned = tk.PanedWindow(self.convert, orient='horizontal', handlesize=16)
        self.convertPanned.pack(fill = 'both', expand=1, padx = 5, pady = 5)

        self.convertHolderIO = tk.Frame(self.convertPanned)
        self.convertHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')
        self.convertHolderButton = tk.Frame(self.convertPanned)
        self.convertHolderButton.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')
        self.convertPanned.add(self.convertHolderIO)
        self.convertPanned.add(self.convertHolderButton)

        self.IOPanned = tk.PanedWindow(self.convertHolderIO, orient = 'vertical', handlesize=16)
        self.IOPanned.pack(fill = 'both', expand=1, padx = 5, pady = 5)

        self.entryTextConvert = tkST.ScrolledText(tabs = ('1c'), width = 75, height = 10, undo=True, autoseparators=True)
        self.entryTextConvert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.outputText = ttk.Treeview(self.convertPanned)
        self.outputTextY = ttk.Scrollbar(self.outputText, orient = 'vertical', command = self.outputText.yview)
        self.outputTextX = ttk.Scrollbar(self.outputText, orient = 'horizontal', command = self.outputText.xview)

        self.outputText.config(xscrollcommand=self.outputTextX.set, yscrollcommand=self.outputTextY.set)
        self.outputTextX.pack(side = 'bottom', fill = 'x')
        self.outputTextY.pack(side = 'right', fill = 'y')
        self.outputText.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1,fill = 'both')

        self.IOPanned.add(self.entryTextConvert)
        self.IOPanned.add(self.outputText)

        self.convertGrid1 = tk.Frame(self.convertHolderButton)
        self.convertGrid1.pack(fill = 'x', side = 'top', anchor = 'nw')
        self.convertGrid2 = tk.Frame(self.convertHolderButton)
        self.convertGrid2.pack(fill = 'x', side = 'top', anchor = 'nw')
        self.convertGrid3 = tk.Frame(self.convertHolderButton)
        self.convertGrid3.pack(fill = 'x', side = 'bottom', anchor = 'sw')

        self.entryTableLabel = tk.Label(self.convertGrid1, text = "Nome da tabela")
        self.entryTableLabel.pack(side = 'left', anchor = 'nw', pady = 5)
        self.entryTableName = tk.Entry(self.convertGrid1)
        self.entryTableName.pack(side = 'left', anchor = 'nw', padx = 5, pady = 5, expand = 1,fill = 'x')
        
        self.entryTextOutButton = tk.Checkbutton(self.convertGrid2, text = "Projetar Tabela", variable=self.controlVarOutC)
        self.entryTextOutButton.pack(side = 'top', anchor='w', expand=0)

        self.entryTextCreateSchemaButton = tk.Checkbutton(self.convertGrid2, text = "Criar Create Table", variable=self.controlVarSchemaC)
        self.entryTextCreateSchemaButton.pack(side = 'top', anchor='w', expand=0)

        self.entryTextInsertButton = tk.Checkbutton(self.convertGrid2, text = "Criar Insert Into", variable=self.controlVarInsertC)
        self.entryTextInsertButton.pack(side = 'top', anchor='w', expand=0)

        self.convertButton = ttk.Button(self.convertGrid3, text="Converter")
        self.convertButton.pack(side = 'bottom', anchor = 'se', padx = 5, pady = 5, fill = 'x')
    
    def createCreateTab(self):
        self.createPanned = tk.PanedWindow(self.createTable, orient='horizontal', handlesize=16)
        self.createPanned.pack(fill = 'both', expand=1, padx = 5, pady = 5)
        
        self.createHolderIO = tk.Frame(self.createTable)
        self.createHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')
        self.createHolderButton = tk.Frame(self.createTable)
        self.createHolderButton.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')

        self.createPanned.add(self.createHolderIO)
        self.createPanned.add(self.createHolderButton)

        self.entryTextCreate = tkST.ScrolledText(self.createHolderIO, tabs = ('1c'), width = 75, height = 10, undo=True, autoseparators=True)
        self.entryTextCreate.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.entryTextCreateInsertButton = tk.Checkbutton(self.createHolderButton, text = "Criar Insert Into", variable=self.controlVarInsertI)
        self.entryTextCreateInsertButton.pack(side = 'top', anchor='nw', expand=0)

        self.createButton = ttk.Button(self.createHolderButton, text="Criar")
        self.createButton.pack(side = 'bottom', anchor = 'se', padx = 5, pady = 5, fill = 'x')
    def createInsertTab(self):
        self.insertHolderIO = ttk.Frame(self.insertInto)
        self.insertHolderIO.pack(side = 'top', anchor = 'n', expand = 1, fill = 'both')

        self.entryTextInsert = tkST.ScrolledText(self.insertHolderIO, tabs = ('1c'), width = 75, height = 10, undo=True, autoseparators=True)
        self.entryTextInsert.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.insertButton = ttk.Button(self.insertInto, text="Inserir")
        self.insertButton.pack(side = 'bottom', anchor = 'ne', padx = 5, pady = 5, fill = 'x')
    def createQuery(self):
        self.queryButton = ttk.Button(self.queryTab, text="Consultar")
        self.queryButton.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, fill = 'x')

        self.queryHolderIO = ttk.Frame(self.queryTab)
        self.queryHolderIO.pack(side = 'left', anchor = 'n', expand = 1, fill = 'both')
        self.queryPanned = tk.PanedWindow(self.queryHolderIO, orient='vertical', handlesize=16)
        self.queryPanned.pack(fill = 'both', expand=1, padx = 5, pady = 5)

        self.queryEntryText = tkST.ScrolledText(self.queryPanned, tabs = ('1c'), width = 75, height = 10, undo=True, autoseparators=True)
        self.queryEntryText.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1, fill = 'both')

        self.outputQuery = ttk.Treeview(self.queryPanned)
        self.outputQueryY = ttk.Scrollbar(self.outputQuery, orient = 'vertical', command = self.outputQuery.yview)
        self.outputQueryX = ttk.Scrollbar(self.outputQuery, orient = 'horizontal', command = self.outputQuery.xview)

        self.outputQuery.config(xscrollcommand=self.outputQueryX.set, yscrollcommand=self.outputQueryY.set)
        self.outputQueryX.pack(side = 'bottom', fill = 'x')
        self.outputQueryY.pack(side = 'right', fill = 'y')
        self.outputQuery.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, expand = 1,fill = 'both')

        self.queryPanned.add(self.queryEntryText)
        self.queryPanned.add(self.outputQuery)

    def configButtons(self):
        self.convertButton.config(command=
                                        lambda: 
                                            self.SQL.converterDictParaDT(self.entryTextConvert.get('1.0','end'),
                                            self.entryTableName.get(),
                                            {"outputText": self.outputText,
                                            "createText" : self.entryTextCreate, 
                                            "insertText" : self.entryTextInsert},
                                            {"outC" : self.controlVarOutC.get(), 
                                            "schemaC" : self.controlVarSchemaC.get(),
                                            "insertC" : self.controlVarInsertC.get()}
                                            )
                                )
        self.createButton.config(command=
                                    lambda: 
                                        self.SQL.criarTabela(self.entryTextCreate.get("1.0","end"),
                                        self.entryTextInsert, self.controlVarInsertI.get()
                                        )
                                )
        self.insertButton.config(command=
                                    lambda: 
                                        self.SQL.insertInto(self.entryTextInsert.get("1.0","end")))
        self.queryButton.config(command=
                                    lambda: 
                                        self.SQL.queryDB(self.queryEntryText.get("1.0","end"),
                                        self.outputQuery
                                        )
                                )

if __name__ == "__main__":
    SQLConnection = SQL()

    Root(SQLConnection)
'''
{
	"tab": '1c', 
	"bg": 'SystemWindow', 
	"fg": 'black',
	"selectbackground": '#dddddd', 
	"selectforeground": 'black', 
	"insertbackground": 'black'
}
select *
from TINF_INFTAB as t1
join TINF_INFSIG as t2
on t1.TABI_COD = t2.SIGI_COD
order by t1.TABI_COD;
'''

    
import tkinter as tk
from tkinter import ttk
import tkinter.scrolledtext as tkST
from tkinter.messagebox import showerror


class App(tk.Tk):
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
        self.queryHolderIO = ttk.Frame(self.queryTab)
        self.queryHolderIO.pack(side = 'top', anchor = 'n', expand = 1, fill = 'both')
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

        self.queryButton = ttk.Button(self.queryTab, text="Consultar")
        self.queryButton.pack(side = 'top', anchor = 'nw', padx = 5, pady = 5, fill = 'x')

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
    showerror("Erro", "Por favor execute \"main.py\"")
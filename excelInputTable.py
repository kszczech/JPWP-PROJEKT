import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import Automat

class tkExcelTable:
    def __init__(self, screen):
        self.screen = screen

        self.mode = tk.IntVar()
        self.mode.set(1) # if mode == 1: imie nazwisko else: email

        self.lastRow = 4
        self.rows = [1,2,3]

        self.tableInput = [] #data about column
        self.tableOutput = []  # data about column

        self.labelText = ["Imie", "Nazwisko", "Email"]
        self.customEntrys = []

        self.y1Input = 1
        self.y2Input = 100

        self.y1Output = 1
        self.y2Output = 100

        self.fileName = ""
        self.inputDir = ""
        self.outputDir = ""

        columnOutputName = tk.Label(self.screen,text="output excel").grid(row=0,column=1)
        columnInputName = tk.Label(self.screen,text="input excel").grid(row=0,column=2)
        columnEmpty = tk.Label(self.screen, text="").grid(row=0,column=3)

        fNameLabel = tk.Label(self.screen,text=self.labelText[0]).grid(row=1,column=0)
        lNameLabel = tk.Label(self.screen, text=self.labelText[1]).grid(row=2, column=0)
        emailLabel = tk.Label(self.screen, text=self.labelText[2]).grid(row=3, column=0)

        tk.Radiobutton(self.screen, text="po emailu", variable=self.mode, value=0).grid(row=1, column=4, columnspan=4)
        tk.Radiobutton(self.screen, text="po imieniu i nazwisku", variable=self.mode, value=1).grid(row=2, column=4, columnspan=4)

        numberInputLabel = tk.Label(self.screen, text="Zakres lini inputu").grid(row=3, column=4, columnspan=2, padx=10)
        numberOutputLabel = tk.Label(self.screen, text="Zakres lini outputu").grid(row=3, column=6, columnspan=2, padx=10)

        self.fromInputEntry = tk.Entry(self.screen, width=3,)
        self.toInputEntry = tk.Entry(self.screen, width=3)
        self.fromInputEntry.grid(row=4, column=4)
        self.toInputEntry.grid(row=4, column=5)
        self.fromOutputEntry = tk.Entry(self.screen, width=3)
        self.toOutputEntry = tk.Entry(self.screen, width=3)
        self.fromOutputEntry.grid(row=4, column=6)
        self.toOutputEntry.grid(row=4, column=7)

        tk.Label(self.screen, text="    ").grid(row=5, column=4, columnspan=4, padx=10)

        #TO DO
        self.inputDirBtn = tk.Button(self.screen, text="lokalizacja pliku szczegółowego", command=self.findDirInput)
        self.inputDirBtn.grid(row=5, column=4, columnspan=4)
        self.outputDirBtn = tk.Button(self.screen, text="lokalizacja pliku wyjściowego", command=self.findDirOutput)
        self.outputDirBtn.grid(row=6, column=4, columnspan=4)
        self.fileNameBtn = tk.Button(self.screen, text="lokalizacja pliku docelowego",command=self.savesDir)
        self.fileNameBtn.grid(row=7, column=4, columnspan=4)


        self.fNameEntryOutput = tk.Entry(self.screen)
        self.fNameEntryOutput.grid(row=1,column=1,padx=10,pady=10)
        self.lNameEntryOutput = tk.Entry(self.screen)
        self.lNameEntryOutput.grid(row=2, column=1, padx=10, pady=10)
        self.emailEntryOutput = tk.Entry(self.screen)
        self.emailEntryOutput.grid(row=3, column=1, padx=10, pady=10)

        self.fNameEntryInput = tk.Entry(self.screen)
        self.fNameEntryInput.grid(row=1, column=2,padx=10,pady=10)
        self.lNameEntryInput = tk.Entry(self.screen)
        self.lNameEntryInput.grid(row=2, column=2, padx=10, pady=10)
        self.emailEntryInput = tk.Entry(self.screen)
        self.emailEntryInput.grid(row=3, column=2, padx=10, pady=10)

        self.addButton = tk.Button(self.screen, text="Dodaj nową kolejna kolumne",command= self.addColumn)
        self.addButton.grid(row=self.lastRow, column=0,columnspan=3)
        self.closeButton = tk.Button(self.screen, text="Zamknij",command= self.close)
        self.closeButton.grid(row=self.lastRow+1, column=0)
        self.saveButton = tk.Button(self.screen, text="Zapisz", command=self.save)
        self.saveButton.grid(row=self.lastRow + 1, column=2)

    def findDirInput(self):
        self.inputDir = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        print(self.inputDir)


    def findDirOutput(self):
        self.outputDir = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        print(self.outputDir)

    def savesDir(self):
        self.fileName = filedialog.asksaveasfilename(filetypes=[("Excel files", ".xlsx .xls")])
        print(self.fileName)

    def addColumn(self):
        self.rows.append(self.lastRow)
        rowEntrys = []
        for i in range(3):
            rowEntrys.append(tk.Entry(self.screen))
        self.customEntrys.append(rowEntrys) #0 - custom name /// #1 output entry /// #2 input entry
        for i in range(3):
            self.customEntrys[-1][i].grid(row=self.lastRow, column=i,padx=10,pady=10)
        self.lastRow += 1
        self.addButton.grid(row=self.lastRow, column=0, columnspan=3)
        self.closeButton.grid(row=self.lastRow + 1, column=0)
        self.saveButton.grid(row=self.lastRow + 1, column=2)

    def close(self):
        pass
    def save(self):
        if self.inputDir == '':
            messagebox.showerror("Błąd lokalizacji", "Podaj lokalizacje inputu")
            self.inputDir = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        if self.outputDir == '':
            messagebox.showerror("Błąd lokalizacji", "Podaj lokalizacje outputu")
            self.outputDir = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
        if self.fileName == '':
            messagebox.showerror("Błąd lokalizacji", "Podaj lokalizacje pliku docelowego")
            self.fileName = filedialog.asksaveasfilename(filetypes=[("Excel files", ".xlsx .xls")])
        if (self.fromInputEntry.get() == '' or self.fromOutputEntry.get() == '' or self.toInputEntry.get() == '' or self.toOutputEntry.get() == '') or (int(self.fromOutputEntry.get()) > int(self.toInputEntry.get())) or (int(self.fromOutputEntry.get()) > int(self.toInputEntry.get())):
            messagebox.showerror("Błąd zakresu","Podaj odpowiedni zakres lini do przetworzenia")
        else:
            self.tableInput = []  # data about column
            self.tableOutput = []  # data about column
            if self.mode.get() == 1:
                self.tableInput.append(str(self.fNameEntryInput.get()).upper())
                self.tableInput.append(str(self.lNameEntryInput.get()).upper())
                self.tableInput.append(str(self.emailEntryInput.get()).upper())

                self.tableOutput.append(str(self.fNameEntryOutput.get()).upper())
                self.tableOutput.append(str(self.lNameEntryOutput.get()).upper())
                self.tableOutput.append(str(self.emailEntryOutput.get()).upper())

                if len(self.customEntrys) == 0:
                    pass
                else:
                    for column in self.customEntrys:
                        if column[1].get() == '' or column[2].get() == '':
                            pass
                        else:
                            self.tableInput.append(str(column[2].get()).upper())
                            self.tableOutput.append(str(column[1].get()).upper())

                self.y1Input = int(self.fromInputEntry.get())
                self.y2Input = int(self.toInputEntry.get())

                self.y1Output = int(self.fromOutputEntry.get())
                self.y2Output = int(self.toOutputEntry.get())

                Automat.fill(self.tableInput, self.tableOutput, self.inputDir, self.outputDir, self.fileName,
                             self.y1Input, self.y2Input, self.y1Output, self.y2Output)

                print(self.tableInput)
                print(self.tableOutput)


import tkinter as tk
import excelInputTable as t


root = tk.Tk()
root.title("toturiale")

def clkMerge():
    mergeScreen = tk.Toplevel()
    #mergeScreen.geometry("700x900")

    tabela = t.tkExcelTable(mergeScreen)

mergeButton = tk.Button(root,text="MERGE",font="Kartika",command=clkMerge).pack()
autobusyButton = tk.Button(root,text="AUTOBUSY" ,font="Kartika").pack()
pokojeButton = tk.Button(root,text="POKOJE",font="Kartika").pack()



root.mainloop()
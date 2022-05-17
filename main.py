import tkinter as tk
import excelInputTable as t
from tkinter import ttk
import gui_autobusy



root = tk.Tk()
root.title("toturiale")
root.configure(bg="#141414")

def clkMerge():
    mergeScreen = tk.Toplevel()
    #mergeScreen.geometry("700x900")
    tabela = t.tkExcelTable(mergeScreen)

def clkBuses():
    gui_autobusy.display()


mergeButton = tk.Button(root,text="MERGE",font="Kartika",command=clkMerge, width=25).pack(pady=10, padx=20)
autobusyButton = tk.Button(root,text="AUTOBUSY" ,font="Kartika", width=25,command=clkBuses).pack(pady=10, padx=20)
pokojeButton = tk.Button(root,text="POKOJE",font="Kartika", width=25).pack(pady=10, padx=20)



root.mainloop()
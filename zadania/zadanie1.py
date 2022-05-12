import tkinter as tk


root = tk.Tk()
root.title("toturiale")
root.configure(bg="#141414")

def clkMerge():
    mergeScreen = tk.Toplevel()

mergeButton = tk.Button(root,text="MERGE",font="Kartika",command=clkMerge, width=25).pack(pady=10, padx=20)
autobusyButton = tk.Button(root,text="AUTOBUSY" ,font="Kartika", width=25).pack(pady=10, padx=20)
pokojeButton = tk.Button(root,text="POKOJE",font="Kartika", width=25).pack(pady=10, padx=20)
exitButton = tk.Button(root).pack()



root.mainloop()
import tkinter as tk

root = tk.Tk()
root.title("zadanie2")

i = 3

Entrys = tk.Entry(root,width=30)
def click():
    global i


Label1 = tk.Label(root, text="Label1")
Label2 = tk.Label(root, text="Label2")
Button1 = tk.Button(root, text="przycisk1", command=click)


root.mainloop()
import tkinter as tk

def click(r):
    if r.get() == 1:
        tk.Label(root, text="klik",bg="cyan", pady=30, padx=30).grid(row=4)
    elif r.get() == 2:
        tk.Label(root, text="klik", bg="green", pady=30, padx=30).grid(row=4)
    elif r.get() == 3:
        tk.Label(root, text="klik", bg="red", pady=30, padx=30).grid(row=4)

root = tk.Tk()
root.title("Prezentacja")

r = tk.IntVar()
r.set(2)
click(r)

tk.Radiobutton(root, text="Opcja 1", variable=r, value=1, command=lambda: click(r)).grid(row=0, padx=100)
tk.Radiobutton(root, text="Opcja 2", variable=r, value=2, command=lambda: click(r)).grid(row=1, padx=100)
tk.Radiobutton(root, text="Opcja 3", variable=r, value=3, command=lambda: click(r)).grid(row=2, padx=100)

root.mainloop()


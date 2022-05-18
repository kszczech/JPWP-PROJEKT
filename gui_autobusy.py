from tkinter import *
from tkinter import filedialog
from Autobusy_main import *
from Bus import Bus



def input_funkcja(root):
    root = root
    root.filename = filedialog.askopenfilename(initialdir="c:/pdw",
                                           title="Select a xlsx file",
                                           filetypes=(("xlsx files", "*.xlsx"),("all files","*.*")))
    global wb
    wb = pd.read_excel(root.filename)
    print(wb)
    return wb


def output_funkcja(root,buses):
    global wb
    global col
    root = root
    root.filename = filedialog.askopenfilename(filetypes=[("Excel files", ".xlsx .xls")])
    buses = dystrybuowanie_autobusow(wb, buses, col)
    zapisz_do_arkusza(buses, root.filename)



def clicked(r):
    global col
    if r == 1:
        col = 'Zabawometr'
    else:
        col = 'Kierunek'
    return col

def clicked_but(dymy):
    print(dymy)
    global col
    if dymy == 1:
        col = 'Zabawometr'
    elif dymy == 2:
        col = 'Kierunek'
    return col

def display():

    root = Tk()
    root.title("Przydzielanie osób do autobusów")
    #root.geometry('400x400')

    global col
    x = 30
    y = x - 1
    z = x - 2
    q = x - 0
    b1 = Bus("b1", x, y)
    b2 = Bus("b2", x, z)
    b3 = Bus("b3", x, q)
    buses = [b1, b2, b3]
    global wb


    r = IntVar()
    r.set(1)




    input = Button(root, text="Input file", padx= 60, pady=30, command=lambda : input_funkcja(root))
    output = Button(root, text="Output file", padx= 60, pady=30, command=lambda :output_funkcja(root,buses))
    zabawa = Radiobutton(root, text="Zabawometr", variable=r, value=1, command=lambda: clicked_but(r.get()))
    kierunki = Radiobutton(root, text="Kierunek", variable=r,  value=2,command=lambda: clicked_but(r.get()))


    input.grid(row=1, column=0)
    output.grid(row=1, column=1)
    zabawa.grid(row=0, column=0)
    kierunki.grid(row=0, column=1)



    root.mainloop()








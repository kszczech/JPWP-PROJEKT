from tkinter import *
from tkinter import filedialog
from autobusy_main import *
from bus import Bus


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


def clicked_but(colname):
    global col
    col = colname
    print(colname)
    return col

def display():

    root = Tk()
    root.title("Przydzielanie osób do autobusów")


    # stworz autobusy x => liczba miejsc
    x = 50
    # b1 = Bus("nazwa_autobusu", [wszystkie_miejsca], [wolne_miejsca])
    # tworzymy ile chcemy
    b1 = Bus("b1", x, x)
    b2 = Bus("b2", x, x)
    b3 = Bus("b3", x, x)
    b4 = Bus("b4", x, x)
    b5 = Bus("b5", x, x)
    # dodajemy do tablicy buses po przecinku
    buses = [b1, b2, b3, b4, b5]
    global wb



    input = Button(root, text="Input file", padx= 60, pady=30, command=lambda : input_funkcja(root))
    output = Button(root, text="Output file", padx= 60, pady=30, command=lambda :output_funkcja(root,buses))
    zabawa = Radiobutton(root, text="Zabawometr",  value=1, command=lambda: clicked_but('Zabawometr'))
    kierunki = Radiobutton(root, text="Kierunek",   value=2,command=lambda: clicked_but('Kierunek'))
    input.grid(row=1, column=0)
    output.grid(row=1, column=1)
    zabawa.grid(row=0, column=0)
    kierunki.grid(row=0, column=1)



    root.mainloop()








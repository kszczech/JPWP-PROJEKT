import pandas as pd
from Bus import Bus


# sortowanie listy po zabawometrze

def zabawometr(data):
    data.sort_values('Zabawometr', inplace=True, ascending=False)
    return data


# sortowanie listy po występowaniu kierunku

def kierunki(df):
    df['Frequency'] = df.groupby('Kierunek')['Kierunek'].transform('count')
    df.sort_values('Frequency', inplace=True, ascending=False)
    df.drop(columns=['Frequency'], inplace=True)
    return df


# Sortowanie listy autobusów wg ilości wolnych miejsc malejąco

def sortowanie_autobusow(buses):
    buses.sort(key=lambda x: x.empty_seat, reverse=True)
    return buses

# Sortowanie podrozujacych

def sortowanie_podrozujacych(wb, col):
    if col == 'Kierunek':
        return kierunki(wb)
    elif col == 'Zabawometr':
        return zabawometr(wb)

# usadowienie osob w autobusie

def wpakowanie_do_autobusu(bus, wb, tcount):
    travs = wb.iloc[:tcount]
    travlst = travs.values.tolist()
    bus.list.extend(travlst)
    bus.empty_seat -= tcount
    wb.drop(index=wb.index[:tcount], inplace=True)
    return bus

# wyznaczenie liczby podroznych

def wyznacz_liczbe_podrozujacych(wb, col):
    if col == "Kierunek":
        firstval = wb[col].iloc[0]                        # jaka wartosc w pierwszym rzedzie
        tcount = sum([x == firstval for x in wb[col]])    # jesli po kierunku, to zliczamy ile osob jest na konkretnym
        return tcount
    elif col == "Zabawometr":                             # jesli po zabawometrze to zwyczajnie dlugosc listy
        return len(wb)


def dystrybuowanie_autobusow(wb, buses, col):
    buses = sortowanie_autobusow(buses)
    while buses[0].empty_seat > 0 and len(wb) > 0:  # iterowanie po autobusach
        while True:  # iterowanie po grupach
            empty = buses[0].empty_seat
            wb = sortowanie_podrozujacych(wb, col)
            tcount = wyznacz_liczbe_podrozujacych(wb, col)
            if empty <= tcount:
                tcount = empty
                buses[0] = wpakowanie_do_autobusu(buses[0], wb, tcount)
                buses = sortowanie_autobusow(buses)
                break
            else:
                buses[0] = wpakowanie_do_autobusu(buses[0], wb, tcount)
                buses = sortowanie_autobusow(buses)
                if len(wb) == 0:  # czy nie ma już ludzi
                    break
            buses = sortowanie_autobusow(buses)
    return buses


def zapisz_do_arkusza(buses, file_name):
    bdfs = []
    for bus in buses:
        bdf = pd.DataFrame(bus.list, columns=['Imie', 'Nazwisko', 'Kierunek', 'Zabawometr'])
        bdf['Autobus'] = bus.name
        bdfs.append(bdf)
    df = pd.concat(bdfs)
    print(df)
    #df.to_excel(file_name, index=False)



def main():
    wb = pd.read_excel('projekt.xlsx')
    # TODO: input kierunki/zabawometr
    col = 'Kierunek'  # 'Zabawometr'

    # autobusy

    # x = int(input("miejsca w busie: "))
    x = 25
    y = x - 1
    z = x - 2
    q = x - 0
    b1 = Bus("b1", x, y)
    b2 = Bus("b2", x, z)
    b3 = Bus("b3", x, q)
    buses = [b1, b2, b3]

    buses = dystrybuowanie_autobusow(wb, buses, col)

    #print(b1)
    #print(b2)
    #print(b3)

    zapisz_do_arkusza(buses, 'wyniki.xlsx')


if __name__ == "__main__":
    main()





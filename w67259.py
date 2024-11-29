"""
    Projekt z przedmiotu LAB Języki i Paradygmaty Programowania

    Hubert Michna, w67259, 5IIZ/2022-GPL03, Listopad 2024
"""

import tkinter as GUI
import tkinter.ttk as GUI_2
from tkinter import messagebox as MESSAGEBOX # .showinfo(), .showerror()
from functools import partial as PARTIAL
import webbrowser as WEBROWSER # .open()
import re as RE

#! Zmienne Globalne
Liczby = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
#0123456789abcdefghijklmnopqrstuvwxyz

#! Funkcje
def WIP_Debug_1():
    """
        Funkcja do celów testowych.
    """
    print("--- WIP ---")

def WIP_Debug_2(Tekst):
    """
        Funkcja do celów testowych.
    """
    print(f"--- {Tekst} ---")

def WIP_Debug_3():
    """
        Funkcja do celów testowych.
    """
    print(Ustawienia)

def O_Programie():
    """
        Wyświetla komunikat o błędzie.
    """
    MESSAGEBOX.showinfo("O Programie", "Ten program został przygotowany w ramach projektu z przedmiotu przedmiotu LAB 'Języki i Paradygmaty Programowania'.\n\nAutor: Hubert Michna, w67259, 5IIZ/2022-GPL03, Listopad 2024")

def Pomoc():
    """
        Wyświetla komunikat z informacją o programie
    """
    MESSAGEBOX.showinfo("Pomoc", "Ten program umożliwia zamianę podanej liczby o podstawie z przedziału <2; 36> na inne podstawy z takiego samego przedziału.\n\nInput: Liczba która ma zostać zamieniona.\n\nPodstawa: Podstawa systemu liczbowego podanej liczby; <2; 36>\n\nDocelowe Systemy Liczbowe: Na jakie systemy liczbowe ma zostać zamieniona podana liczba. Można podać wiele wartości oddzielonych przecinkami. Każda liczba musi być z przedziału <2; 36>.")

def Okno_Na_Wierzchu(Event = ""):
    """
        Ustawia żeby okno nie znajdowało/znajdowało się na wierzchu.
    """
    Window.attributes("-topmost", bool(Ustawienia["Okno Na Wierzchu"].get()))
    Window.update()

def Wstępna_Walidacja():
    """
        Walidacja danych wejściowych podanych przez użytkownika.
    """
    Komunikaty = ""

    #? Dane Wejściowe
    Input = Entry_1.get().replace(" ", "")
    System = Entry_2.get().replace(" ", "")
    Docelowe_Systemy = Entry_3.get().replace(" ", "").split(",")

    #? Jeśli nie podano liczby
    if Input == "":
        Komunikaty += "Podaj liczbę.\n\n"

    #? Jeśli nie podano podstawy
    if System == "":
        Komunikaty += "Podaj podstawę systemu liczbowego dla podanej liczby.\n\n"

    #? Jeśli podano błędną podstawę
    if RE.match(r"^\d+$", System):
        if not 2 <= int(System) <= 36:
            Komunikaty += "Nie można wykonać obliczeń przy takiej podstawie systemu liczbowego. Możliwe podstawy to: <2; 36>.\n\n"

        else:
            #? Jeśli liczba zawiera odpowiednie cyfry
            #print(Liczby[0:int(System)])
            for x in range(len(Input)):
                if Input[x].lower() not in Liczby[0:int(System)]:
                    Komunikaty += f"Liczba zawiera niepoprawną cyfrę ({Input[x]}) pozycja: {x}\n\n"
    else:
        Komunikaty += "Podaj poprawną podstawę systemu liczbowego dla podanej liczby.\n\n"

    #? Jeśli podano złe docelowe systemy liczbowe
    for x in range(len(Docelowe_Systemy)):
        if RE.match(r"^\d+$", Docelowe_Systemy[x]):
            if not 2 <= int(Docelowe_Systemy[x]) <= 36:
                Komunikaty += f"Nie można wykonać obliczeń dla takiej podstawy systemu liczbowego ({Docelowe_Systemy[x]}). Możliwe podstawy to: <2; 36>.\n\n"
        else:
            Komunikaty += f"Niepoprawny docelowy system liczbowy: '{Docelowe_Systemy[x]}'.\n\n"

    #? Jeśli są jakieś komunikaty do wyświetlenia
    if len(Komunikaty) != 0:
        MESSAGEBOX.showerror("Błąd", Komunikaty[:-2])
        return False
    return True

def Przeliczanie(Event = ""):
    """
        Główna funkcja. Wczytuje dane wejściowe, zamienia podaną liczbę najpierw na system dziesiętny a potem na docelowe systemy liczbowe.
    """
    if not Wstępna_Walidacja():
        return

    print("\n--- Przeliczanie: ---")

    Wynik_Base10 = 0
    Input = Entry_1.get().replace(" ", "")
    System = int(Entry_2.get().replace(" ", ""))
    Docelowe_Systemy = Entry_3.get().replace(" ", "").split(",")

    for x in range(len(Docelowe_Systemy)):
        Docelowe_Systemy[x] = int(Docelowe_Systemy[x])

    WIP_Debug_2(f"Input: {Input}")
    WIP_Debug_2(f"System: {System}")
    WIP_Debug_2(f"Docelowe_Systemy: {Docelowe_Systemy}")

    #! Usunięcie elementów z TreeView
    for x in TreeView.get_children():
        TreeView.delete(x)

    #! Przeliczanie podanej liczby na base10
    if System != 10:
        for x in range(len(str(Input))):
            Wynik_Base10 += Liczby.index((str(Input)[x].lower())) * (System ** (len(str(Input)) - x - 1))
            print(f"{Liczby.index(str(Input)[x].lower())} * {System ** (len(str(Input)) - x-1)}")

    print(f"{Input} ({System}) = {Wynik_Base10} (10)\n\t===")

    #! Sortowanie (Ustawienia)
    if Ustawienia["Sortowanie"].get() == 1:
        Docelowe_Systemy.sort()
    elif Ustawienia["Sortowanie"].get() == 2:
        Docelowe_Systemy.sort(reverse=True)

    #! Przeliczanie podanej liczby na inne systemy liczbowe
    for x in range(len(Docelowe_Systemy)):
        if Wynik_Base10 != 0:

            Reszta = ""
            Czesc_Calkowita = Wynik_Base10
            while True:
                if Czesc_Calkowita <= 0:
                    Reszta = Reszta[::-1] # Odwraca string
                    break
                else:
                    Reszta += str(Liczby[Czesc_Calkowita % int(Docelowe_Systemy[x])])
                    Czesc_Calkowita = Czesc_Calkowita // int(Docelowe_Systemy[x])

            if Ustawienia["Duże Litery"].get():
                Reszta = Reszta.upper()
            else:
                Reszta = Reszta.lower()

            TreeView.insert("", GUI.END, values=(Reszta, Docelowe_Systemy[x]))

        print(f"{Reszta} ({Docelowe_Systemy[x]})")

    print("--- END Przeliczanie ---\n")

#! Main
if __name__ == "__main__":
    #! Ogólne/Ustawienia
    Window = GUI.Tk()
    Window.title("w67259| Projekt - Paradygmaty i Języki Programowania")
    Window.minsize(400, 200)
    Window.geometry("475x250+100+100")

    #? Ustawienia
    Ustawienia = {
        "Duże Litery": GUI.BooleanVar(None, 1),
        "Okno Na Wierzchu": GUI.BooleanVar(),
        "Sortowanie": GUI.IntVar(None, 1),

        "Input - Domyślna Wartość": "123",
        "System - Domyślna Wartość": "16",
        "Systemy Docelowe - Domyślna Wartość": "8, 2, 10, 16"
    }

    #! Elementy GUI
        #! Frame - Ogólne
    Frame_Top = GUI.Frame(Window)
    Frame_Left = GUI.Frame(Window)
    Frame_Right = GUI.Frame(Window)
    Frame_Bottom = GUI.Frame(Window)

    Frame_Top.grid(row=0, column=0, columnspan=2)
    Frame_Left.grid(row=1, column=0, sticky=GUI.NS, ipadx=5, ipady=5)
    Frame_Right.grid(row=1, column=1, sticky=GUI.NSEW, ipadx=5, ipady=5)
    Frame_Bottom.grid(row=2, column=0, columnspan=2, sticky=GUI.EW)

    Window.rowconfigure(Frame_Top, weight=0)
    Window.rowconfigure(Frame_Left, weight=1)
    Window.rowconfigure(Frame_Right, weight=1)
    Window.columnconfigure(Frame_Right, weight=1)
    Window.rowconfigure(Frame_Bottom, weight=0)

    Frame_Right.rowconfigure(1, weight=1)
    Frame_Right.columnconfigure(0, weight=1)
    Frame_Right.columnconfigure(1, weight=0)

        #! Frame - Top
    Label_1 = GUI.Label(Frame_Top, text="Kalkulator Systemów Liczbowych", font=("Calibri 12 bold"))
    Label_1.grid(row=0, column=0, sticky=GUI.EW)

        #! Frame - Left
    Label_2 = GUI.Label(Frame_Left, text="Input:")
    Label_2.grid(row=1, column=0)

    Label_3 = GUI.Label(Frame_Left, text="Podstawa:")
    Label_3.grid(row=1, column=1)

    Entry_1 = GUI.Entry(Frame_Left)
    Entry_1.grid(row=2, column=0, sticky=GUI.EW)

    Entry_2 = GUI.Entry(Frame_Left)
    Entry_2.grid(row=2, column=1, sticky=GUI.EW)

    Label_4 = GUI.Label(Frame_Left, text="Docelowe Systemy Liczbowe:")
    Label_4.grid(row=3, column=0, columnspan=2)

    Entry_3 = GUI.Entry(Frame_Left)
    Entry_3.grid(row=4, column=0, columnspan=2, sticky=GUI.EW)

    Button_1 = GUI.Button(Frame_Left, text="Policz", command=Przeliczanie)
    Button_1.grid(row=5, column=0, columnspan=2)

        #! Frame - Right
    Label_5 = GUI.Label(Frame_Right, text="Output")
    Label_5.grid(row=0, column=0)

    TreeView = GUI_2.Treeview(Frame_Right, columns=("Liczba", "System"), show="headings", height=10)
    TreeView.grid(row=1, column=0, sticky=GUI.NSEW)
    TreeView.column("Liczba", width=100)
    TreeView.heading("Liczba", text="Liczba")
    TreeView.column("System", width=50, stretch=False)
    TreeView.heading("System", text="System")

        #! Frame - Bottom
    Label_6 = GUI.Label(Frame_Bottom, text="By Hubert Michna, w67259, Listopad 2024", fg="#595959")
    Label_6.grid(row=0, column=0)

        #! Scroll (Frame - Right)
    Scrollbar =  GUI_2.Scrollbar(Frame_Right, command=TreeView.yview)
    Scrollbar.grid(row=1, column=1, sticky=GUI.NS)
    TreeView.configure(yscrollcommand=Scrollbar.set)

    #! Menu
    Menu = GUI.Menu(Window)
    Window.config(menu=Menu)
        #? "Plik"
    Menu_Plik = GUI.Menu(Menu, tearoff=False)
    Menu_Plik.add_command(label="O Programie", command=O_Programie)
    Menu_Plik.add_command(label="Pomoc", command=Pomoc)
    Menu_Plik.add_separator()
    Menu_Plik.add_command(label="Zakończ", command=Window.destroy)

        #? Ustawienia
    Menu_Ustawienia = GUI.Menu(Menu, tearoff=False)
    Menu_Ustawienia.add_checkbutton(label="Duże Litery", onvalue=1, offvalue=0, variable=Ustawienia["Duże Litery"])
    Menu_Ustawienia_Sortowanie = GUI.Menu(Menu_Plik, tearoff=0)
    Menu_Ustawienia_Sortowanie.add_radiobutton(label="Brak Sortowania", variable=Ustawienia["Sortowanie"], value=0)
    Menu_Ustawienia_Sortowanie.add_radiobutton(label="Sortowanie Docelowych Systemów (asc)", variable=Ustawienia["Sortowanie"], value=1)
    Menu_Ustawienia_Sortowanie.add_radiobutton(label="Sortowanie Docelowych Systemów (desc)", variable=Ustawienia["Sortowanie"], value=2)
    Menu_Ustawienia.add_cascade(label="Sortowanie", menu=Menu_Ustawienia_Sortowanie)
    Menu_Ustawienia.add_checkbutton(label="Okno Na Wierzchu", command=Okno_Na_Wierzchu, onvalue=1, offvalue=0, variable=Ustawienia["Okno Na Wierzchu"])

        #? Linki
    Menu_Linki = GUI.Menu(Menu, tearoff=False)
    Menu_Linki.add_command(label="GitHub - Repozytorium", command=PARTIAL(WEBROWSER.open, "https://github.com/Hubsik456/LAB_Jezyki_i_Paradygmaty_Programowania/"))
    Menu_Linki.add_separator()
    Menu_Linki.add_command(label="rapidtables.com", command=PARTIAL(WEBROWSER.open, "https://www.rapidtables.com/convert/number/base-converter.html"))
    Menu_Linki.add_command(label="exploringbinary.com", command=PARTIAL(WEBROWSER.open, "https://www.exploringbinary.com/base-converter/"))

        #? Umieszczanie Elementów
    Menu.add_cascade(label="Plik?", menu=Menu_Plik, underline=0)
    Menu.add_cascade(label="Ustawienia", menu=Menu_Ustawienia, underline=0)
    Menu.add_cascade(label="Linki", menu=Menu_Linki, underline=0)

    #! Binds/Eventy
    Window.bind("<Return>", Przeliczanie)

    #! Domyślne Wartości
    Entry_1.insert(GUI.END, Ustawienia["Input - Domyślna Wartość"])
    Entry_2.insert(GUI.END, Ustawienia["System - Domyślna Wartość"])
    Entry_3.insert(GUI.END, Ustawienia["Systemy Docelowe - Domyślna Wartość"])

    #! End
    Window.mainloop()
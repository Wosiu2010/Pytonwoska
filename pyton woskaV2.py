import time
pieniadze = 1000
login = "Wosiu"
loginU = 0
haslo = "Kupa1234"
hasloU = 0
opcja = 0
ilosc = 0
opcja2 = 0
konto = 0
kontobilosc = 0
kontol = 0
kontob = 0
blue = '\033[94m'
yellow = '\033[93m'
green = '\033[92m'




while loginU != login:
    loginU = input(blue + """Podaj login:
""" + yellow)
    time.sleep(0.5)
while hasloU != haslo:
    hasloU = input(blue + """Podaj Haslo:
""" + yellow)
    time.sleep(0.5)
print(blue + """Witaj W banku""",green + login
)
time.sleep(0.5)


while login == "Wosiu":
    opcja = input(yellow + """
Wybierz jedną z opcji: 1. Stan Konta 2. Wplac 3. Wyplac 4. Przelew
""" + green)
    time.sleep(0.5)
    if opcja == "1":
        opcja2 = input(yellow + """Wybierz jedną z opcji: 1. Stan Konta 2. Stan wybranego konta
""" + green)
        if opcja2 == "1":
            time.sleep(0.5)
            print(blue + "Kwota:",pieniadze,"zł")
        elif opcja2 == "2":
            time.sleep(1)
            kontol = int(input(yellow + """Wpisz numer konta:
""" + green))
            if konto == kontol:
                time.sleep(0.5)
                print(blue + "Kwota:",kontob,"zł")
            elif konto != kontol:
                time.sleep(0.5)
                print(yellow + """Nie znaleziono konta
""")
    elif opcja == "2":
        ilosc = int(input(yellow + """Ile chcesz wplacic:
""" + green))
        time.sleep(0.5)
        pieniadze+=ilosc
    elif opcja == "3":
        ilosc = int(input(yellow + """Ile chcesz wyplacic:
""" + green))
        time.sleep(0.5)
        pieniadze-=ilosc
    elif opcja == "4":
        konto = int(input(yellow + """Wpisz numer konta:
""" + green))
        time.sleep(0.5)
        kontobilosc = int(input(yellow + """Ile chcesz wplacic:
""" + green))
        time.sleep(0.5)
        kontob+=kontobilosc
        pieniadze-=kontobilosc
        

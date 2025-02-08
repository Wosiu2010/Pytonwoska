pieniadze = 0
login = "Artem"
loginU = 0
haslo = "QWER1234"
hasloU = 0
opcja = 0
ilosc = 0
opcja2 = 0
konto = 0
kontobilosc = 0
kontol = 0
kontob = 0




while loginU != login:
    loginU = input("Podaj login: ") 
while hasloU != haslo:
    hasloU = input("Podaj Haslo: ")
print("Witaj W banku",login)







while login == "Artem":
    opcja = input("Wybierz jedną z opcji: 1. Stan Konta 2. Wplac 3. Wyplac 4. Transakcje")






    if opcja == "1":
        opcja2 = input("Wybierz jedną z opcji: 1. Stan Konta 2. Stan wybranego konta")
        if opcja2 == "1":
            print("Kwota:",pieniadze,"zł")
        elif opcja2 == "2":
            kontol = int(input("Wpisz numer konta: "))
            if konto == kontol:
                print("Kwota:",kontob,"zł")
            elif konto != kontol:
                print("Nie znaleziono konta")


     
    elif opcja == "2":
        ilosc = int(input("Ile chcesz wplacic: "))
        pieniadze+=ilosc

        

    elif opcja == "3":
        ilosc = int(input("Ile chcesz wyplacic: "))
        pieniadze-=ilosc

        

    elif opcja == "4":
        konto = int(input("Wpisz numer konta: "))
        kontobilosc = int(input("Ile chcesz wplacic: "))
        kontob+=kontobilosc
        pieniadze-=kontobilosc
        

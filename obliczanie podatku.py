podatek1 = 10 / 100
podatek2 = 20 / 100
podatek3 = 30 / 100


def obliczpodatek(zarobki):
    if (zarobki < 2000):
        podatek = podatek1;
    elif (zarobki >= 2000 and zarobki < 5000):
        podatek = podatek2;
    else:
        podatek = podatek3;
    return podatek * zarobki

zarobki = int(input("podaj wysokosc zarobkow: "))
wysokoscpodatku = obliczpodatek(zarobki)
print("wysokosc twojego podatku to: ", wysokoscpodatku)

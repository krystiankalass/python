import random
import sys

gramy = "tak"

podane = []
wylosowane = []

while gramy == "tak":
    for i in range(6):
        podane.append(int(input("podaj liczbe numer " + str(i + 1) + ': ')))
        wylosowane.append(random.randint(1, 50))
    trafione = 0
    for z in podane:
        for j in wylosowane:
            if z == j:
                trafione = trafione + 1
    print("twoj wynik to: " + str(trafione))
    print("wylosowane liczby:")
    for i in wylosowane:
        print(i)
    podane.clear()
    wylosowane.clear()
    gramy = input('czy chcesz zagrac jeszcze raz? (tak/nie) ')
if gramy == "nie":
    sys.exit()

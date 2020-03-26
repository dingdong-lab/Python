import random

#1
lista1 = [1/x for x in range(1,11)]
lista2 = [2**x for x in range(0,11)]
lista3 = [x for x in lista2 if x%4 == 0]

#2
macierz = [[random.randint(1,4) for y in range(4)] for x in range(4)]
przekatna = [(macierz[x])[x] for x in range(4)]

#3 
produkty1 = {"jaja":"sztuki", "ciastka":"sztuki", "woda":"litry", "mięso":"kilogramy", "mleko":"litry"}
produkty2 = [x[0] for x in produkty1.items() if x[1] == "sztuki"]

#4
def monotonicznosc(funkcja):
    a = float(funkcja.split()[2])
    if a > 0:
        print("rosnąca")
    elif a < 0:
        print("malejąca")
    else:
        print("stała")

#5

def relacja(funkcja1, funkcja2):
    a = float(funkcja1.split()[2])
    b = float(funkcja2.split()[2])
    c = a/b
    if c == 1:
        print("równoległe")
    elif c == -1:
        print("prostopadłe")

#6
def promien(funkcja):
    r = float(funkcja.split('=')[1])
    return r**(1/2)

#7
def pitagoras(a = 3, b = 4):
    return (a*a+b*b)**(1/2)

#8
def suma_aryt(a1 = 1, r = 1, ile = 10):
    return (2*a1 + r*(ile-1))/2 *ile

#9
def iloczyn(*liczby):
    if len(liczby) == 0:
        return 0
    
    wynik = 1
    for x in liczby:
        wynik *= x
    return wynik

#10
def zlicz_zakupy(** zakupy):
    if len(zakupy) == 0:
        return 0

    wynik = 0
    for x in zakupy:
        wynik += zakupy[x]
    return wynik

#11
import zespolone.arytmetyka
import zespolone.rozdziel

print(zespolone.rozdziel.rzeczywista(), zespolone.rozdziel.urojona())
print(zespolone.arytmetyka.dodaj(5 + 2j, 10 + 3j))
print(zespolone.arytmetyka.odejmij(5 + 2j, 10 + 3j))

#12
import ciagi.arytmetyczny
import ciagi.geometryczny

print(ciagi.arytmetyczny.suma())
print(ciagi.geometryczny.suma())
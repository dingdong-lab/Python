#zad 1
class materiał:
    def __init__(self, rodzaj, dlugosc, szerokosc):
        self.rodzaj = rodzaj 
        self.dlugosc = dlugosc 
        self.szerokosc = szerokosc 

    def wyswietl_nazwe(self):
        print(self.rodzaj)

class ubrania(materiał):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar 
        self.kolor = kolor 
        self.dla_kogo = dla_kogo

    def wyswietl_dane(self):
        print("rozmiar:{:s} kolor:{:s} dla kogo:{:s}".format(self.rozmiar,self.kolor,self.dla_kogo))

class sweter(ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra

    def wyswietl_nazwe(self):
        print("rodzaj swetra:{:s}".format(self.rodzaj_swetra))

bawełna = materiał("bawełna", 2, 2)
bawełna.wyswietl_nazwe()

koszulka = ubrania("M", "biały", "ciebie")
koszulka.wyswietl_dane()

sweterek = sweter("golf")
sweterek.wyswietl_nazwe()

#zad 2
class kwadrat:
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        nowy = kwadrat(self.x+other.x)
        return nowy

kwadrat1 = kwadrat(2)
kwadrat2 = kwadrat(5)
kwadrat3 = kwadrat1+kwadrat2
print(kwadrat3.x)

#zad 3
class kwadratb(kwadrat):
    def __ge__(self, other):
        return self.x >= other.x 
    
    def __gt__(self, other):
        return self.x > other.x 

    def __le__(self, other):
        return self.x <= other.x 

    def __lt__(self, other):
        return self.x < other.x 

kwadratb1 = kwadratb(2)
kwadratb2 = kwadratb(5)

print("ge{} gt{} le{} lt{}".format((kwadratb1>= kwadratb2), (kwadratb1> kwadratb2), (kwadratb1<= kwadratb2), (kwadratb1< kwadratb2)))

#zad 4
class Point:
    counter = []

    def __init__(self, x=0, y=0):
        """Konstuktor punktu."""
        self.x = x
        self.y = y

    def update(self, n):
        self.counter.append(n)    

punkt1 = Point(2,2)
punkt2 = Point(3,4)
punkt3 = Point(15,12)
punkt4 = Point(0,-1)

print(punkt1.counter, punkt2.counter, punkt3.counter, punkt4.counter, sep =' ')
punkt1.counter.append(punkt1.x)
punkt2.counter.append(punkt2.x)
punkt3.counter.append(punkt3.x)
punkt4.counter.append(punkt4.x)
print(punkt1.counter, punkt2.counter, punkt3.counter, punkt4.counter, sep =' ')

#zad 5
class Osoba:

    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def przedstaw_sie(self):
        return "{} {}".format(self.imie, self.nazwisko)


class Pracownik(Osoba):

    def __init__(self, imie, nazwisko, pensja):
        Osoba.__init__(self, imie, nazwisko)
        # lub
        # super().__init__(imie, nazwisko)
        self.pensja = pensja

    def przedstaw_sie(self):
        return "{} {} i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)


class Menadzer(Pracownik):

    def przedstaw_sie(self):
        return "{} {}, jestem menadżerem i zarabiam {}".format(self.imie, self.nazwisko, self.pensja)

Pracownik1 = Pracownik("Adam", "Kowalski", 2500)
Menadzer1 = Menadzer("Janusz", "Nowacki", 10000)

print("instancja pracownik1")
print("osoba:",isinstance(Pracownik1, Osoba))
print("pracownik:",isinstance(Pracownik1, Pracownik))
print("menadzer:",isinstance(Pracownik1, Menadzer))

print("instancja menadzer1")
print("osoba:",isinstance(Menadzer1, Osoba))
print("pracownik:",isinstance(Menadzer1, Pracownik))
print("menadzer:",isinstance(Menadzer1, Menadzer))

print("subklasa pracownik")
print("osoba:",issubclass(Pracownik, Osoba))
print("pracownik:",issubclass(Pracownik, Pracownik))
print("menadzer:",issubclass(Pracownik, Menadzer))

print("subklasa menadzer")
print("osoba:",issubclass(Menadzer, Osoba))
print("pracownik:",issubclass(Menadzer, Pracownik))
print("menadzer:",issubclass(Menadzer, Menadzer))

#zad 6
class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

lista1 = [1,2,3]
lista2 = [2, 3.14, True, "Test"]
string1 = "Hello World"

iteracja = Wspak(lista1)
print(iteracja)
print(next(iteracja))
iteracja = Wspak(lista2)
print(next(iteracja))
print(next(iteracja))
print(next(iteracja))
iteracja = Wspak(string1)
print(next(iteracja))
print(next(iteracja))
print(next(iteracja))

#zad 7
class parzyste:
    def __init__(self, data):
        self.data = data
        self.index = -2

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        self.index = self.index + 2
        return self.data[self.index]

iteracja = parzyste(string1)

print(string1)
print(next(iteracja))
print(next(iteracja))
print(next(iteracja))

#zad 8
def istnieje_w(element, lista):
    for x in lista:
        if element == x:
            return True
    return False 

class samogłoski:
    lista = ['a','e','i','o','u','y']

    def __init__(self, data):
        self.data = data
        self.index = 0
        self.is_string = isinstance(data, str)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.data):
            raise StopIteration
        if self.is_string == True:
            while istnieje_w(self.data[self.index], self.lista) == False:
                self.index += 1
                if self.index == len(self.data):
                    raise StopIteration
            self.index += 1
            return self.data[self.index-1]
        else:
            raise StopIteration

string2 = "testa"
iterator = samogłoski(string2)
print(next(iterator))
print(next(iterator))

#zad 9

def even(data):
    for index in range(0, len(data), 2):
        yield data[index]

gen = even("Parzyste")
print(next(gen))
print(next(gen))
print(next(gen))

#zad 10
import itertools

kombinacje = itertools.combinations({1,2,3,4,5,6,7,8,9,10}, 3)
for x in kombinacje:
    print(x) 

#zad 11
def fibonacci():
    a = 0 
    b = 1
    temp = 0
    while True:
        yield a
        temp = b
        b = a + b
        a = temp

gen = fibonacci()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))

#zad 12
def miesiace():
    lista = ['styczen','luty','marzec','kwiecien','maj','czerwiec','lipiec','sierpien',
            'wrzesien', 'pazdziernik', 'listopad', 'grudzien']
    index = 0
    while True:
        yield lista[index]
        index += 1
        if index == 12:
            index = 0

gen = miesiace()
print(next(gen))
for x in range(15):
    print(next(gen))
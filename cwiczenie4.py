#zad 1
with open("4zad1.txt", "w") as plik:
    lista1 = [x for x in range(0,257,4)]
    plik.writelines(str(lista1))

#zad 2
with open("4zad1.txt", "r") as plik:
    string1 = plik.readline()
    print(string1) 

#zad 3
with open("4zad3.txt", "w+") as plik:
    plik.writelines("Hello World\n")
    plik.writelines("Hello Python\n")
    plik.writelines("Hello Wizualizacja Danych\n")
with open("4zad3.txt", "r+") as plik:
    for linia in plik:
        print(linia, end='\n')

#zad 4
class NaZakupy:
    def __init__(self, a, b, c, d):
        self.nazwa_produktu = a
        self.ilosc = b
        self.jednostka_miary = c
        self.cena_jed = d
    
    def wyswietl_produkt(self):
        print("nazwa:", self.nazwa_produktu)
        print("ilosc:", self.ilosc)
        print("miara:", self.jednostka_miary)
        print("cena:", self.cena_jed, "/", self.jednostka_miary)

    def ile_produktu(self):
        print(self.ilosc, self.jednostka_miary)

    def ile_kosztuje(self):
        print(self.ilosc*self.cena_jed, "zł")

ziemniaki = NaZakupy("ziemniaki", 3, "kg", 1)
ziemniaki.wyswietl_produkt()
ziemniaki.ile_produktu()
ziemniaki.ile_kosztuje()

#zad 5
class ciag_aryt:

    def __init__(self):
        self.elementy = []
        self.suma = 0
        self.a1 = 0
        self.r = 0
        self.n = 0

    def pobierz_elementy(self, *elementy):
        self.elementy = elementy

    def pobierz_parametry(self, a1, r, n):
        self.n = n
        self.a1 = a1 
        self.r = r

    def policz_sume(self):
        self.suma = 0
        for x in self.elementy:
            self.suma += x

    def policz_elementy(self):
        self.elementy = [self.a1+(self.r*x) for x in range(self.n)]

    def wyswietl_dane(self):
        print(self.elementy)

ciag = ciag_aryt()
ciag.pobierz_elementy(1, 3 , 5)
ciag.wyswietl_dane()
ciag.pobierz_parametry(1,3,3)
ciag.policz_elementy()
ciag.wyswietl_dane()

#zad 6
class slowa:
    
    def __init__(self):
        self.slowo1 = "tama"
        self.slowo2 = "mata"

    def sprawdz_czy_palindrom(self):
        slowo1 = [self.slowo1[x] for x in range(len(self.slowo1))]
        slowo1_rev = slowo1.copy()
        slowo1_rev.reverse()
        print(slowo1)
        print(slowo1_rev)
        if slowo1 == slowo1_rev:
            print("Tak")
        else:
            print("Nie")
        
    def sprawdz_czy_metagramy(self):
        jest = True 
        ok = False
        if len(self.slowo1) != len(self.slowo2):
            print("Nie")
            return
        for x in range(len(self.slowo1)):
            if ok == False:
                if self.slowo1[x] != self.slowo2[x]:
                    ok = True
            else:
                if self.slowo1[x] != self.slowo2[x]:
                    jest = False 
        if jest == True and ok == True: 
            print("Tak")
        else:
            print("Nie")

    def sprawdz_czy_anagramy(self):
        lista1 = [self.slowo1[x] for x in range(len(self.slowo1))]
        lista2 = [self.slowo2[x] for x in range(len(self.slowo2))]

        for x in lista1:
            ok = False 
            for y in lista2:
                if x == y:
                    ok = True
            if ok == False:
                print("Nie")
                return 

        for x in lista2:
            ok = False 
            for y in lista1:
                if x == y:
                    ok = True
            if ok == False:
                print("Nie")
                return
        
        print("Tak")


        
slownik = slowa() 
slownik.sprawdz_czy_palindrom()
slownik.sprawdz_czy_metagramy()
slownik.sprawdz_czy_anagramy()

#zad 7
class robaczek:
    def __init__(self, x, y, kroki):
        self.x = x 
        self.y = y 
        self.kroki = kroki

    def __del__(self):
        print("Robaczek umarł na pozycji %(x1)d %(y1)d" %{'x1':self.x, 'y1':self.y})
    
    def idz_w_gore(self, ile_krokow):
        self.y += self.kroki * ile_krokow

    def idz_w_dol(self, ile_krokow):
        self.y -= self.kroki * ile_krokow

    def idz_w_lewo(self, ile_krokow):
        self.x -= self.kroki * ile_krokow

    def idz_w_prawo(self, ile_krokow):
        self.x += self.kroki * ile_krokow

    def pokaz_gdzie_jestes(self):
        print("x %(x1)d y %(y1)d" %{'x1':self.x, 'y1':self.y})

robaczek1 = robaczek(100, 100, 2)
robaczek1.idz_w_dol(20)
robaczek1.idz_w_gore(20)
robaczek1.idz_w_lewo(20)
robaczek1.idz_w_prawo(20)
robaczek1.pokaz_gdzie_jestes()


    
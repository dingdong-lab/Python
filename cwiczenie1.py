import math

#1
int1 = 5
int2 = 7
float1 = 3.14
float2 = 1.71
string1 = 'hello'
string2 = 'world'
complex1 = 3 + 14j
complex2 = 1 + 71j

print(int1, int2, float1, float2, string1, string2, complex1, complex2, sep=' ')

#2
suma = int1+int2
roznica = int2-int1
iloczyn = float1*float2
iloraz = float1/float2
iloraz_calk = float1//float2
reszta = int2%int1
potega = int2**int1

#3
suma += int1
roznica -= int2
iloczyn *= float1
iloraz /= float2
iloraz_calk //= float1
reszta %= int2
potega **=int1

#4
print(math.e**10, math.log(5+math.sin(8)**2)**(1/6), math.floor(3.55), math.ceil(4.8), sep='\n')

#5
imie = 'ADRIAN'
nazwisko = 'ŁĘTEK'
print(imie.capitalize()+' '+nazwisko.capitalize())

#6
piosenka = "Nawalam węgorza na na na na na na"
print(piosenka.count('na'))

#7
indeksy = "czesc"
print(indeksy[0], indeksy[4])

#8
print(piosenka.split())

#9
string3 = "Zapis zmiennoprzecinkowy i szesnastkowy:"
float3 = 3.14
int3 = 0x25
print('%(z1)s%(z2)f %(z3)x' %{'z1':string3, 'z2':float3, 'z3':int3})

#10
filmy = ['Haker', 'Psy', 'Matrix', 'Pokot']
filmy.sort()
print(filmy)

#11
x1 = 0
x2 = math.pi/6
x3 = math.pi/4
x4 = math.pi/3
x5 = math.pi/2

sinl = [math.sin(x1), math.sin(x2), math.sin(x3), math.sin(x4), math.sin(x5)]
cosl = [math.cos(x1), math.cos(x2), math.cos(x3), math.cos(x4), math.cos(x5)]
tanl = [math.tan(x1), math.tan(x2), math.tan(x3), math.tan(x4), math.tan(x5)]

print(sinl, cosl, tanl, sep='\n')

#12
zdanie = "Hello first time in python world"
podzielone = zdanie.split()
print(podzielone)

#13
slownik = {'gruby':'Olek Olszewski', 'retard':'Michał Maksymow', 'krótki':'Hubert Lenkiewiecz', 'glowica':'Piotr Martyniuk',
           'Janusz':'Jan Matwiejczuk', 'Jerry':'Michał Małkowski', 'Jasierz':'Michał Jaśniewski', 'Domino':'Damian Sala',
           'karatekid':'Wojciech Szałachowski', 'majkel':'Michał Turczynowicz'}

print(slownik['gruby'], slownik['Janusz'], slownik['majkel'])

#14
skroty = {'k':'ok', 'nw':'nie wiem', 'btw':'przy okazji', 'gz':'gratulacje', 'lol':'śmieszne'}
kopia = skroty.copy()

#15
rzymskie = {1:'I', 5:'V', 10:'X', 50:'L', 100:'C', 500:'D', 1000:'M'}

#16
gry = {"EU4":"europa universalis IV", "CK2":"Crusader Kings II", "V2":"Victoria 2", "HOI4":"Hearts of Iron IV"}
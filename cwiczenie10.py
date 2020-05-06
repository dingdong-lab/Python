import matplotlib.pyplot as plt
import numpy as np
import math 
import pandas as pd
import random

#zad 1
#lista1 = [1/x for x in range(1,21)]
#lista2 = [x for x in range(1,21)]
#plt.plot(lista2, lista1, label='x^-1')

#plt.axis([1, 20, 0, 1])

#plt.xlabel('x')
#plt.ylabel('f(x)')

#plt.legend()

#plt.show()

#zad 2
#lista3 = [1/x for x in range(1,20)]
#lista4 = [x for x in range(1,20)]
#plt.plot(lista3, lista4, marker='>', ls='dotted' ,c='green', label='1/x')


#plt.axis([0, 20, 0, 1])

#plt.xlabel('x')
#plt.ylabel('f(x)')

#plt.title("Wykres funkcji f(x) dla x[1, 20]")

#plt.legend()

#plt.show()

#zad 3
#lista5 = [x/10 for x in range(1,301)]
#lista6 = [math.sin(x) for x in lista5]
#lista7 = [math.cos(x) for x in lista5]

#print(lista5)

#plt.plot(lista5, lista6, label='sin x')
#plt.plot(lista5, lista7, label='cos x')

#plt.xlabel('x')
#plt.ylabel('f(x)')

#plt.legend()

#plt.show()

#zad 4
#lista8 = [x/10 for x in range(1,301)]
#lista9 = [math.sin(x) for x in lista8]
#lista10 = [math.cos(x)+2 for x in lista8]
#lista11 = [-math.sin(x) for x in lista8]

#plt.plot(lista8, lista9, label='sin x')
#plt.plot(lista8, lista10, label='cos x')
#plt.plot(lista8, lista11, label='-sin x')

#plt.xlabel('x')
#plt.ylabel('f(x)')

#plt.legend()

#plt.show()

#zad 5
dane = pd.read_csv('iris.data', sep=',', names=['sepal length',  'sepal width',  'petal length', 'petal width', 'class'])
sepal_l = dane['sepal length']
sepal_w = dane['sepal width']
sepal_d = [abs(sepal_l[i]-sepal_w[i])*25 for i in range(0,len(sepal_l))]
klasa = [ str(x) for x in dane['class']]
klasa_c = []
for x in klasa:
    if x == 'Iris-setosa':
        klasa_c.append('red')
    elif x == 'Iris-versicolor':
        klasa_c.append('blue')
    else:
        klasa_c.append('green')
        
#plt.scatter(sepal_l, sepal_w, c=klasa_c, s=sepal_d)
#plt.show()

#zad 6
plik = pd.ExcelFile('imiona.xlsx')
dane2 = pd.read_excel(plik)

lista = []
for x in dane2['Imie']:
    if x[-1] == 'A':
        lista.append('kobieta')
    else:
        lista.append('mężczyzna')
dane2['Plec'] = lista
seria1 = dane2.groupby(['Plec']).agg({'Liczba':['sum']})



lista = seria1[('Liczba', 'sum')].to_list()

#plt.subplot(1, 3, 1)
#plt.bar(['K', 'M'], lista)
#plt.ylabel('Ilość narodzin')
#plt.xlabel('Płeć')

lista1 = dane2['Rok'].unique()
maks1 = dane2[dane2['Plec'] == 'kobieta'].groupby(['Rok']).agg({'Liczba':['sum']})
maks2 = dane2[dane2['Plec'] == 'mężczyzna'].groupby(['Rok']).agg({'Liczba':['sum']})
lista2 = maks1[('Liczba', 'sum')].to_list()
lista3 = maks2[('Liczba', 'sum')].to_list()

#plt.subplot(1, 3, 2)
#plt.plot(lista1, lista2, c='black', label='kobiety')
#plt.plot(lista1, lista3, c='yellow', label='mężczyźni')
#plt.legend()
#plt.ylabel('Ilość narodzin')
#plt.xlabel('Rok')

#plt.subplot(1, 3, 3)
#maks1 = dane2.groupby(['Rok']).agg({'Liczba':['sum']})
#lista2 = maks1[('Liczba', 'sum')].to_list()
#plt.bar(lista1, lista2, color=(0.2, 0.4, 0.6, 0.6))
#plt.ylabel('Ilość narodzin')
#plt.xlabel('Rok')
#plt.show()

#zad 7
#plt.subplot(1, 3, 1)
#plt.bar([''], lista[0], label='kobieta')
#plt.bar([''], lista[1], label='mężczyzna', bottom=lista[0])
#plt.ylabel('Ilość narodzin')
#plt.xlabel('Płeć')
#plt.legend()

#plt.show()

#zad 8
def losuj(n):
    lista = []
    for x in range(n):
        lista.append(random.randint(1,6)+random.randint(1,6))
    return lista

#plt.hist(losuj(100), bins=11, facecolor='g', alpha=0.75, density=True)
#plt.xlabel('Sumy rzutów dwoma kostkami')
#plt.ylabel('Prawdopodobieństwo')
#plt.title('Histogram')

#plt.grid(True)
#plt.show()

#zad 9
dane3 = pd.read_csv('zamowienia.csv', delimiter=';')
dane4 = dane3.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']})
explode= [0.1 for x in range(len(dane4.index))]
plt.pie(dane4, labels=dane4.index, shadow=True, explode=explode, autopct=lambda pct: "{:.1f}%".format(pct), textprops=dict(color="black"))


plt.legend(title='Zawodnicy')
plt.show()

#zad 10
lista1 = [1/x for x in range(1,21)]
lista2 = [x for x in range(1,21)]

plt.annotate('funkcja 1/x',
            xy=(80, 60), xycoords='figure points')

plt.plot(lista2, lista1, label='x^-1')

plt.axis([1, 20, 0, 1])

plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend()

plt.show()

lista5 = [x/10 for x in range(1,301)]
lista6 = [math.sin(x) for x in lista5]
lista7 = [math.cos(x) for x in lista5]

arrow_properties = dict(
    facecolor="black", width=0.5,
    headwidth=4, shrink=0.1)

plt.annotate(
    "maximum", xy=(1.45, 1),
    xytext=(4, 1.2),
    arrowprops=arrow_properties)

plt.annotate(
    "minimum", xy=(3.11, -1),
    xytext=(6, -1.2),
    arrowprops=arrow_properties)

plt.plot(lista5, lista6, label='sin x')
plt.plot(lista5, lista7, label='cos x')

plt.xlabel('x')
plt.ylabel('f(x)')

plt.legend()

plt.show()

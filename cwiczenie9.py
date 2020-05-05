import pandas as pd
import matplotlib.pyplot as plt

#1
plik = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(plik)

#grupa = dane.groupby(['Rok']).agg({'Liczba':['sum']})
#grupa.plot()
#plt.show()

#2
lista = []
for x in dane['Imie']:
    if x[-1] == 'A':
        lista.append('kobieta')
    else:
        lista.append('mężczyzna')
dane['Plec'] = lista

#grupa2 = dane.groupby(['Plec']).agg({'Liczba':['sum']})
#grupa2.plot.bar()
#plt.show()

#3
top = dane['Rok'].max()
#grupa3 = dane[dane['Rok'] > top-5].groupby(['Plec']).agg({'Liczba':['sum']})
#grupa3.plot.pie(subplots = True,autopct='%.2f %%')
#plt.show()

#4
dane2 = pd.read_csv('iris.data', sep=',', names=['sepal length in cm',  'sepal width in cm',  'petal length in cm', 'petal width in cm', 'class'])
grupa4 = dane2.copy()
grupa4['class'] = grupa4['class'].astype('|S')
grupa4.drop('petal length in cm', axis=1, inplace=True)
grupa4.drop('petal width in cm', axis=1, inplace=True)

grupa4[grupa4['class']==b'Iris-setosa'].plot.scatter(x='sepal length in cm', y='sepal width in cm', c='black', label='Iris Setosa')
grupa4[grupa4['class']==b'Iris-versicolor'].plot.scatter(x='sepal length in cm', y='sepal width in cm', c='red', label='Iris Versicolour')
grupa4[grupa4['class']==b'Iris-virginica'].plot.scatter(x='sepal length in cm', y='sepal width in cm', c='blue', label='Iris Virginica')

plt.show()

#5
dane3 = pd.read_csv('zamowienia.csv', delimiter=';')
grupa5 = dane3.groupby(['Sprzedawca']).agg({'idZamowienia':['sum']})

#grupa5.plot.bar()
#plt.show()


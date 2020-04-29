import pandas as pd 
import numpy as np 

#zad1

plik = pd.ExcelFile('imiona.xlsx')
dane = pd.read_excel(plik)
#print(dane)

#zad2
#1
#print(dane[dane['Liczba'] > 1000]) 
#2
#print(dane[dane['Imie'] == 'ADRIAN']) 
#3
#print(dane['Liczba'].sum() ) 
#4
#print(dane[(dane['Rok'] >= 2000) & (dane['Rok'] <= 2005)]['Liczba'].sum()) 
#5
lista = []
for x in dane['Imie']:
    if x[-1] == 'A':
        lista.append(1)
    else:
        lista.append(0)
dane['Plec'] = lista
#print(dane[dane['Plec'] == 1]['Liczba'].sum(), dane[dane['Plec'] == 0]['Liczba'].sum())

#6
maks = dane[dane['Plec'] == 1].groupby(['Rok']).agg({'Liczba':['max']})
#print(type(maks.iloc[1][0]))
#for x in range(len(maks)):
    #print(dane[(dane['Plec'] == 1) & (dane['Rok'] == (2000+x)) & (dane['Liczba'] == maks.iloc[x][0])])

#7
maks = dane[dane['Plec'] == 1].groupby('Imie')[['Liczba']].sum()
#print(maks.sort_values(by='Liczba', axis=0, ascending=False).iloc[[0],[0]])
maks = dane[dane['Plec'] == 0].groupby('Imie')[['Liczba']].sum()
#print(maks.sort_values(by='Liczba', axis=0, ascending=False).iloc[[0],[0]])

#zad 3
dane2 = pd.read_csv('zamowienia.csv', sep=';')
print(dane2.info())

#1
#print(dane2['Sprzedawca'].unique())
#2
#print(dane2.nlargest(5, 'Utarg'))
#3
#print(dane2.groupby(['Sprzedawca']).agg({'idZamowienia':['count']}))
#4
#print(dane2.groupby(['Kraj']).agg({'idZamowienia':['sum']}))
#5
dane2['Data zamowienia'] = pd.to_datetime(dane2['Data zamowienia'])
#print(dane2[(dane2['Kraj'] == 'Polska') & (dane2['Data zamowienia'].dt.year == 2005)].groupby(['Sprzedawca']).agg({'idZamowienia':['sum']}))
#6
#print(dane2[(dane2['Data zamowienia'].dt.year == 2004)].agg({'Utarg':['mean']}))
#7
dane2[dane2['Data zamowienia'].dt.year == 2004].to_csv('zamówienia_2004.csv', sep=';')
dane2[dane2['Data zamowienia'].dt.year == 2005].to_csv('zamówienia_2005.csv', sep=';')

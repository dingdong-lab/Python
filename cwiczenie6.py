import numpy as np

#zad 1
a = np.arange(2,82,2)

#zad 2
a = np.array([x**0.5 for x in range(1,101)])
b = a.astype('int64')

#zad 3

def inicjalizuj(n):
    return np.array([[x+n*y for x in range(1,n+1)] for y in range(n)])

#zad 4

def potegi(podstawa, n):
    return np.logspace(1.0, n, num=n, base = podstawa, dtype=int)

#zad 5

def wektor(n):
    a = np.arange(n, 0, -1)
    macierz = np.diag([x for x in a])
    return macierz

#zad 6

slowo1 = 'kuter'
slowo2 = 'kajak'
dlugosc = len(slowo1)

macierz2 = np.diag([x for x in slowo1])
for x in range(dlugosc):
    macierz2[x, 0] = slowo2[x]
    macierz2[0, x] = slowo2[dlugosc-1-x]

print(macierz2)

#zad 7 

def dwojki(n):
    macierz3 = np.zeros((n,n))
    for x in range(n):
        for y in range(n):
            if x+y < n:
                macierz3[x, x+y] = 2*(y+1)
                macierz3[x+y, x] = 2*(y+1)
            if x-y >= n:
                macierz3[x-y, x] = 2*(y+1)
                macierz3[x, x-y] = 2*(y+1)

    return macierz3

#zad 8

mat = np.arange(36)
print(len(mat))
# teraz zmienimy kształt tablicy jednowymiarowej na macierz 5x5
mat = mat.reshape((6,6))

def ciecie(tablica, kierunek):
    if kierunek == 'poziom':
        if len(tablica[:,0]) > 1:
            tablica = tablica[0:(len(tablica[:,0])+1)//2]
            return tablica
        else:
            print("tablica zbyt niska")
            Exception
    if kierunek == 'pion':
        if len(tablica[0,:]) > 1:
            tablica = tablica[:,0:(len(tablica[0,:])+1)//2]
            return tablica
        else:
            print("tablica zbyt wąska")
            Exception
    
mat = ciecie(mat, 'poziom')
print(mat)
mat = ciecie(mat, 'pion')

print(mat)

#zad 9
mat = np.arange(25)
mat[0] = 0
mat[1] = 1
for x in range(2,25):
    mat[x] = mat[x-1]+mat[x-2]

mat = mat.reshape((5,5))
print(mat)

        




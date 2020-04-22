import numpy as np
import random
import math

#zad 1
macierz1 = np.array([6, 25, 83])
macierz2 = np.array([-8, 11, 4])

macierz2*=3
macierz1*=3
print(macierz1, macierz2)

#zad 2
macierz3 = np.array([random.randint(1, 100) for x in range(9)]).reshape(3,3)
macierz4 = np.array([random.randint(1, 100) for x in range(16)]).reshape(4,4)

print("macierz3 kolumna min:", macierz3.min(axis = 0))
print("macierz3 wiersz min:", macierz3.min(axis = 1))
print("macierz4 kolumna min:", macierz4.min(axis = 0))
print("macierz4 wiersz min:", macierz4.min(axis = 1))

#zad 3
print(macierz1.dot(macierz2))

#zad4
macierz5 = np.array([6, 25, 83]).reshape(1,3)
macierz6 = np.array([5.22, 3.67, 121.111], dtype=np.float32).reshape(1,3)

macierz5*=4
macierz6*=4 

print(macierz5, macierz6)

#zad 5
macierz7 = [[0, math.pi/6, math.pi/4], [math.pi/3, math.pi/2, math.pi]]
a= np.sin(macierz7)
print(a)

#zad 6
b = np.cos(macierz7)
print(b)

#zad 7
print(np.add(a,b))

#zad 8
macierz8 = np.array([random.randint(1, 100) for x in range(9)]).reshape(3,3)
for x in macierz8:
    print(x) 

#zad 9
macierz9 = np.array([random.randint(1, 100) for x in range(9)]).reshape(3,3)
for x in macierz9.flat:
    print(x, end=' ')
print() 

#zad 10
macierz10 = np.array([random.randint(1, 100) for x in range(81)]).reshape(9,9)
macierz10.reshape(3,27)
#możemy jeszcze zrobić reshape(27,3), reshape(1,81), reshape(81,1), ponieważ iloczyn wierszy i kolumn musi być 
# równy liczbie elementów czyli 81

#zad 11
macierz11 = np.array([random.randint(1, 100) for x in range(12)]).reshape(3,4)
for x in macierz11.flat:
    print(x, end=" ")
print()
macierz11 = macierz11.reshape(4,3)
for x in macierz11.flat:
    print(x, end=" ")
print()
macierz11 = macierz11.reshape(2,6)
for x in macierz11.flat:
    print(x, end=" ")
#wyświetla elementy w tej samej kolejności
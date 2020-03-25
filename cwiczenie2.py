import sys
import random

#1
zdanie = input()
print(zdanie.count(' '))

#2
linia = sys.stdin.readline()
sys.stdout.write(str(int(linia.split()[0])*int(linia.split()[1])))

#3
# <, >, ==, >=, <=, !=, is, in

#4
x = input()
if x < 0:
    x *= -1
print(x)

#5
a = input()
b = input()
c = input()
if (a > 0 and a <= 10) and (a > b or b > c):
    print("good")
else:
    print("bad")

#6
for x in range(0,125,5):
    print(x)

#7
    for x in range(1,5,1):
        kwadrat = input()
        print(kwadrat*kwadrat)

#8
lista = []
while True:
    element = int(input())
    lista.append(element)

#9
suma_cyfr = int(input())
suma = 0
while suma_cyfr > 0:
    suma += suma_cyfr%10
    suma /= 10

#10
wysokosc = int(input())
if wysokosc > 10:
    wysokosc = 10
for x in range(1, wysokosc+1):
    for y in range(1, x+1):
        print('A', end='')
    print()

#11
wysokosc = int(input())
if wysokosc < 3:
    wysokosc = 3
elif wysokosc > 9:
    wysokosc = 9

puste = wysokosc//2
pelne = 1
for x in range(0,wysokosc//2):
    for y in range(0, puste):
        print(' ', end='')
    for y in range(0,pelne):
        print('O', end='')
    print()
    puste -= 1
    pelne += 2

if wysokosc % 2 == 1:
    for x in range(0, wysokosc):
        print('O', end='')
    print()

puste = 1
pelne = wysokosc//2 +1
for x in range(0,wysokosc//2):
    for y in range(0, puste):
        print(' ', end='')
    for y in range(0,pelne):
        print('O', end='')
    print()
    puste += 1
    pelne -= 2

#12
for x in range(1,11):
    for y in range(1,11):
        print(x*y, end=' ')
    print()

#13

#14
x = input()
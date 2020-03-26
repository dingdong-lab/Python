import math

#14
x = int(input())
try:
    x = math.pow(x, 1/2)
except ValueError:
    print("Liczba pierwiastkowana nie może być ujemna")
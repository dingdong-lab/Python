#arytmetyka.py
def dodaj(a = 2 + 1j, b = 2 + 1j):
    return complex(a.real+b.real, a.imag+b.imag)

def odejmij(a = 2 + 1j, b = 2 + 1j):
    return complex(a.real-b.real, a.imag-b.imag)
def suma(a1 = 1, q = 1, ile = 10):
    if q != 1:
        return a1*((1-q**ile)/(1-q))
    else:
        return a1*ile
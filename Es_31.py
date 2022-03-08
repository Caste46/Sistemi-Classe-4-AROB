"""def somma_moltiplicazione(x, y):
    somma = x + y
    moltiplicazione = x * y
    #return somma, moltiplicazione
    return {"somma":somma, "moltiplicazione":moltiplicazione}

a = 10
b = 4
#s, m = somma_moltiplicazione(s, m)
#print(s)
print(somma_moltiplicazione(a, b))"""

def somma_moltiplicazione(x, y):
    somma = x + y
    moltiplicazione = x * y
    return somma, moltiplicazione

#lamda function
somma_moltiplicazione2 = lambda x, y: (x + y, x * y)

a = 10
b = 4
s, m = somma_moltiplicazione2(a, b)
print(s)



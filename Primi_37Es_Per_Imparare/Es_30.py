conta = 0

def isPrimo(num):
    div = 2
    k = 0
    while ((div <= num/2) & (k == 0)):
        if(num % div == 0):
            k = k + 1
        div = div + 1
    if(k == 0):
        ok = True
    else:
        ok = False

    return ok

lista = [k for k in range(2, 1003) if isPrimo(k)]
print(lista)


"""
dispari = [i for i in range(1000) if i % 2 != 0]
print(dispari)


nomi = ["marco", "valeria", "maria", "maddalena", "elia"]

nomi_m = [nome for nome in nomi if nome[0] == "m"]
print(nomi_m)
"""

"""
for c in range(2, 1000):
    if(isPrimo(c) == True):
        lista.append(c)

print(lista)
"""



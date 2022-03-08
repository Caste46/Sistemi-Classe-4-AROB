# 4)Calcola, mediante un opportuno programma in Python, quanti sono i
#  numeri primi minori di 1000. Per stabilire se il numero è primo crea 
# una funzione apposita che ritorni True se il numero è primo, False
# altrimenti.

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

for c in range(2, 1000):
    if(isPrimo(c) == True):
        conta = conta + 1

print(conta)
# 3)Scrivi un programma in Python in cui chiedi all’utente un numero
#  e comunichi se esso è primo oppure no. Per stabilire se il numero
# è primo crea una funzione apposita che ritorni True se il numero è
# primo, False altrimenti.

num = int(input("Inserisci un numero e vediamo se è primo: "))

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

if(isPrimo(num) == True):
    print(f"Il numero {num} è primo")
else: 
    print(f"Il numero {num} NON è primo")

#1)Crea un programma Python che permetta all'utente di inserire un numero
# qualunque di interi all'interno di una lista. Stampa la lista al termine
# dell'inserimento. 

k = int(input("Inserisci quanti numeri vuoi all'interno della lista: "))

lista = []

for indice  in range(k):
    num = int(input("Inserisci un numero: "))
    lista.append(num)

print(f"La lista ottenuta è {lista}")
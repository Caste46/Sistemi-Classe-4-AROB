# 2)Crea una funzione Python che data una lista di numeri, ritorni il suo
#  valore massimo e il suo valore minimo. 

lista = [3, 7, 5, 9, 0]

max = lista[0]
min = lista[0]
n = len(lista)

for k  in range(n):
    if(lista[k] > max):
        max = lista[k]


for i  in range(n):
    if(lista[i] < min):
        min = lista[i]

print(f"Il numero più alto è {max}")
print(f"Il numero più piccolo è {min}")
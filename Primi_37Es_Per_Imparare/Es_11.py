#le liste sono mutabili 

lista = [3,3.1415,"ciao"] #lista eterogenea
print(lista)

numeri_primi = [2,3,5,7,11,13]
print(lista[1:-1]) #indicizzazione con le stesse regole delle stringhe 

lista[1] = 2.645
print(lista)

numeri_primi.append(17)#append aggiunge un dato alla nostra stringa
print(numeri_primi)

print(f"La lunghezza della lista è {len(numeri_primi)}")

altri_numeri_primi = [19,23,29]
molti_numeri_primi = numeri_primi + altri_numeri_primi
print(molti_numeri_primi)

print(10000 * altri_numeri_primi)
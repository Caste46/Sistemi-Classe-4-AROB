"""
x = 123
x = "Ciao"

"""
#slicing

stringa = "Classe quarta A robotica"
print(f"Il primo carattere della stringa è {stringa[0]}")
print(f"L'ultimo carattere della stringa è {stringa[-1]}")

print("-")
print(stringa[3:9])#prende i caratteri dalla posizione 3 alla 9(escluso, fino all'8)
print("-")
print(stringa[6:])
print("-")
print(stringa[:-2])
print("-")
print(stringa[2:14:2])#il 2 finale si chiama gap, lo slicing prende tutte le lettere dalla 2 alla 13 saltando ogni 2 una lettere(una si una no)
print("-")
print(stringa[::-1])#legge la stringa al contrario
print("-")
print(stringa[::-2])

print("-----")
stringa_nuova = stringa[0:14] + "B" + stringa[15:]
print(stringa_nuova)
print("-")
print(f"LA STRINGA MODIFICATA E' : {stringa_nuova}")
print(print)
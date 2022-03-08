liste = ["ciao", "cocco", "studente", "io"]
max = liste[0]

for  lista in liste:
    if len(max) < len(lista):
        max = lista

print(f"La parola piu lunga è: {max}") 
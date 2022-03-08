rubrica = {"ale":380435, "matti":120786}
nome = input("Inserisci il nome: ")
print(rubrica[nome])
nuovo_amico = input("Inserisci il nome da aggiungere: ")
nuovo_telefono = input("Inserisci il numero: ")
rubrica[nuovo_amico] = nuovo_telefono
print(rubrica)
#ciclo for
classi = ["4arob", "3arob", "5brob", "4achi", "3ainf"]
indirizzi = {"rob":"Smart-robot", "chi":"chimica", "inf":"informatica"}


for indice, classe in enumerate(classi):
    indirizzo = indirizzi[classe[-3:]]
    print(f"Posizione {indice + 1} nella lista:")
    print(f"La classe {classe} è dell'indirizzo {indirizzo}", end = "\n\n")


//for numero in range(2,23):
        print(numero)
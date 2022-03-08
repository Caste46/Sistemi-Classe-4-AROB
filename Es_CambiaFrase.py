lettere = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'Z', ' ']
parola = input("Inserisci una parola da cambiare: ")
i = 0
for lettere in parola:
    parola[i] = parola[lettere[i + 3]]
    i += 1

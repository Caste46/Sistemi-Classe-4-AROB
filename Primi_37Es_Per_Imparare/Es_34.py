stringa = input("inserisci una parola: ")
isPalindromo = lambda stringa: (stringa == stringa[::-1])

if(isPalindromo == True):
    print("E' palindroma")
else:
    print("NON è palindroma ")
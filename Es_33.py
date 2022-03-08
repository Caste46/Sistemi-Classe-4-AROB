frase = input("inserisci una  frase : ")
controllo = lambda frase: (frase.isupper())
ok = controllo(frase[0])
if(ok == True):
    print("Inizia con la lettera maiuscola ")
else:
    print("Non inizia con la lettera maiuscola ")
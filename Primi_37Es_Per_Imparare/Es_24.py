operazione = int(input("Quale operazione vuoi effettuare?: "))

if operazione == 0:
    num1 = int(input("Inserisci un numero: "))
    num2 = int(input("Inserisci un numero: "))
    num = num1 + num2
    print(num)
elif operazione == 1:
    num1 = int(input("Inserisci un numero: "))
    num2 = int(input("Inserisci un numero: "))
    num = num1 - num2
    print(num)
elif operazione == 2:
    num1 = int(input("Inserisci un numero: "))
    num2 = int(input("Inserisci un numero: "))
    num = num1 * num2
    print(num)
elif operazione == 3:
    num1 = int(input("Inserisci un numero: "))
    num2 = int(input("Inserisci un numero: "))
    num = num1 / num2
    print(num)
else:
    print("Reinserisci il numero dell'operazione da fare")

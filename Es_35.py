
def isPalindroma(stringa):
    if(stringa == stringa[::-1]): #se la stringa originale è uguale a quella invertita allora è palindroma 
        return True
    else:
        return False

lista,listaMaiusole,listaPalindrome=["parola1","anna","reer","Parola2","Parola3"],[],[]

for parola in lista:
    if(isPalindroma(parola)):
        listaPalindrome.append(parola)
    
    if(parola[0].isupper()):
        listaMaiusole.append(parola)

print(f"Lista iniziale {lista} , Lista maiuscole  {listaMaiusole} , lista palindromi  {listaPalindrome}")
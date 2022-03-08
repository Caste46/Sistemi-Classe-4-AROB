f = open("./testo.txt", "w")

def isPrimo(num):
    div,count=2,0

    while div<=num/2 and count==0:
        if num%div==0:
            count+=1
        else:
            div+=1
    if count==0:
       return True 
    else:
       return False

conta = 0
num = 2

while(conta < 100):
    if(isPrimo(num)):
        f.write(f"{num} \n")
        conta += 1
    num += 1

f.close()
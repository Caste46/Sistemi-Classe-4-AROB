def bin2dec(stringa):
    somma = 0
    for indice,carattere in enumerate(stringa[::-1]):
        somma += int(carattere) * (2**indice)
    return somma

def dec2bin(numero,nbit):
    bina = bin(int(numero))[2:]
    bina = "0" * (nbit-len(bina))+bina
    return bina

def IP_dec2bin(IP_dec):
    bin = ""
    ip = IP_dec.split(".")
    for k in range(4):
        bin += ((dec2bin(int(ip[k]),8))) 
    return bin[:]

def IP_bin2dec(ip):
    dec, nBit = "", 8
    for k in range(0, 32, 8):
        dec += str(bin2dec(ip[k:k + nBit])) + "."
    return dec[:-1]

def controllo(rete, sm):
    ok = False
    reteBin = IP_dec2bin(rete)
    print(reteBin)
    i = 32 - int(sm)
    for k in range(i):
        if(int(reteBin[int(sm) + k]) == '1'):
            ok = True
    return ok

def main():
   
    rete = str(input("Inserisci l'IP di rete: "))
    sm = str(input("Inserisci la subnet mask (es /22): "))[1:]

    if(controllo(rete, sm) == False):
        print(f"L'IP di rete {rete} è corretto")  
    else: 
        print(f"L'IP di rete {rete} NON è corretto") 

if __name__ =="__main__":
    main()
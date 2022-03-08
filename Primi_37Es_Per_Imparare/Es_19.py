n1 = input("Inserisci il primo numero ")
n2 = input("Inserisci il secondo numero ")
x=[]

n1=float(n1)
n2=float(n2)

x.append(n1**2 + n2**2)
x.append((n1+ n2)**2)
x.append(n1**2 - n2**2)
x.append((n1-n2)**2)

print(x)
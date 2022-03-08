def push(pila, elemento):
    pila.append(elemento)

def pop(pila):
    if(len(pila) != 0):
        return pila.pop()
    else:
        return None

pila = []
pila2 = []
num = int(input("Quanti caratteri vuoi inserire: "))

for k in range(num):
    char =  str(input("Inserisci un carattere: "))
    pila.append(char)

for j in range(num):
    a = pop(pila)
    pila2.append(a)

print(pila)
print(pila2)
def enqueue(coda, elemento):
    coda.append(elemento)

def dequeue(coda):
    if(len(coda) != 0):
        return coda.pop(0)
    else:
        return None
    

cliente1 = {"nome": "Mario Rossi", "id": "132435465"}
cliente2 = {"nome": "Beppe Bataia ", "id": "567887654"}
cliente3 = 3.1415
coda = []


enqueue(coda, cliente1)
enqueue(coda, cliente2)
enqueue(coda, cliente3)
print(coda)

import PileCode as pc #alias cioè sinonimo

def main():
    r = 's'
    c = pc.Coda()
    c1 = pc.Coda()
    p = pc.Pila()
    conta = 0
    
    while(r == 's'):
        num = int(input("Inserisci un elemento nella coda: "))
        c.enqueue(num)
        r = input("Vuoi ancora mettere degli elementi nella coda? ")
        conta = conta + 1
    
    for _ in range(conta):
        n = c.dequeue()
        p.push(n)
    
    for _ in range(conta):
        a = p.pop()
        c1.enqueue(a)

    p.print()
    c1.print()

if __name__ =="__main__":
    main()

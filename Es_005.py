class Coda():
    def __init__(self):
        self.coda = []

    def enqueue(self, elemento):
        self.coda.append(elemento)

    def dequeue(self):
        if(len(self.coda) != 0):
            return self.coda.pop(0)
        else:
            return None

    def print(self):
        print(self.coda)

c1 = Coda()
c1.enqueue("Ciao")
c1.enqueue("come")
c1.enqueue("va")
c1.dequeue()
c1.print()
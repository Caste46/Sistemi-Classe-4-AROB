class Pila():
    def __init__(self):
        self.pila = []

    def push(self, elemento):
        self.pila.append(elemento)

    def pop(self, pila):
        if(len(self.pila) != 0):
            return self.pila.pop()
        else:
            return None

    def print(self):
        print(self.pila)

p1 = Pila() #istanza della classe pila 

p1.push("ciao")
p1.push("come")
p1.push("va")
p1.print()
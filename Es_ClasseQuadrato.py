class Quadrato():
    def init(self, lato):
        self.quadrato = []
        self.lato = lato

    def area(self, lato):
        return lato*lato
    
    def perimetro(self, lato):
        return lato*4
    
    def isFuori(self, lato):
        cordX = int(input("Inserisci una coordinata x: "))
        cordY = int(input("Inserisci una coordinata y: "))
        if(cordX > lato or cordY > lato):
            ok = False
        else: 
            ok = True

        return ok

def main():
   
    l = int(input("Inserisci la grandezza del lato: "))
    q = Quadrato()

    q.perimetro(l)
    q.area(l)
   
    if(q.isFuori(l) == False):
        print("Il punto è fuori dal quadrato")
    else:
        print("Il punto è dentro dal quadrato")

if __name__ =="__main__":
    main()
         


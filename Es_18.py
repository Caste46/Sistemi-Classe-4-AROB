import math
a = float(input("Inserisci la prima coordinata: "))
b = float(input("Inserisci la seconda coordinata: "))

a2 = float(input("Inserisci la prima coordinata: "))
b2 = float(input("Inserisci la seconda coordinata: "))

coordinateA = (a, a2)
coordinateB = (b, b2)

ipotenusa = math.sqrt((coordinateA[0]-coordinateA[1])**2 + (coordinateB[0]-coordinateB[1])**2)
print(ipotenusa)
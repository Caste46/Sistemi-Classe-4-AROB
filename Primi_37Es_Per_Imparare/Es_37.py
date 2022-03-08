a, b = 0, 0
tavola_pitagorica = [ (a*b) for a in range(11) for b in range (11) ]# list comprension
indice1 = 0
indice2 = 11
for _ in range(11):
    print(tavola_pitagorica[indice1 : indice2])
    indice2 += 11
    indice1 += 11


"""
altro modo per risolverlo con una lista di liste
tavola = [[x * y for x in range(11)] for y in range(11)]
print(tavola)
"""
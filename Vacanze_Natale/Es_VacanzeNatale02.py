lista = ["zero", "uno", "due", "tre"]
dict = {}

for k , elemento in enumerate(lista):
    dict[k] = elemento
print(dict)

#dictionary comprension:
#dizionario = {x: elemento for x, elemento in enumarete(lista)}
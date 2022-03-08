stringa = "Castellano"

print(f"La lettera iniziale è {stringa[0]}")
print(f"La lettera finale è {stringa[-1]}")

print(f"{stringa[1:-1]}")

print(stringa[::2])

print(stringa[::-1])

nuova_parola = stringa[:2] + "?" + stringa[4:]

print(nuova_parola)


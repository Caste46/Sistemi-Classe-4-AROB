def fattoriale(n):
    if n== 0:
        return 1
    return n* fattoriale(n-1)

print(fattoriale(12))
def serieFibonacci(n):
    if n== 0 or n== 1:
        return 1
    Fibo= serieFibonacci(n-1)+serieFibonacci(n-2)
    return Fibo

for k in range(20):
    print(serieFibonacci(k))
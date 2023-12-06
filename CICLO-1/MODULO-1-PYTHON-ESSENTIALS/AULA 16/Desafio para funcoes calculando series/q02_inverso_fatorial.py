

def fatorial(N):
    fat = 1
    while N>=1:
        fat *=N
        N -= 1
    return fat

def fatorial_inverso(fat):
    return 1/fat

def soma_fatorial_inverso(N):
    soma = 0
    while N>=1:
        soma += fatorial_inverso(fatorial(N))
        N -= 1
    return soma

print(soma_fatorial_inverso(10))
print(soma_fatorial_inverso(20))

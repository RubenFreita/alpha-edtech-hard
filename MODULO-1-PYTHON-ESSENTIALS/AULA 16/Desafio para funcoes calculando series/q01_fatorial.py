

def fatorial(N):
    fat = 1
    while N>=1:
        fat *=N
        N -= 1
    return fat

print(fatorial(5))

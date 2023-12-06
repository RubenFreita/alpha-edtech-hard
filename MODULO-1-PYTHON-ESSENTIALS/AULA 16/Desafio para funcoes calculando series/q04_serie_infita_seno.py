
# x = 361

# x = x* (3.14/180)%(2*3.14)


def fatorial(N):
    fat = 1
    while N>=1:
        fat *=N
        N -= 1
    return fat

def calcula_termo(x, k):
    return (x**(2*k + 1))/fatorial(2*k+1)

def meu_seno(x):
    soma = 0
    flag = True
    for i in range(200):
        if flag == True:
            flag = False
            soma += calcula_termo(x, i)
        elif flag == False:
            flag = True
            soma -= calcula_termo(x, i)
    return round(soma, 3)


x = 35
import math

print(meu_seno(x))
print("Biblioteca math")
print(f"O seno de {x}: {round(math.sin(x),3)}")
print()
print("Minha função mee_seno")
print(f"O seno de {x}: {meu_seno(x)}")


def multplica_todos(*numeros):
    produto = 1
    for numero in numeros:
        produto *= numero
    return produto

def recebe_valores():
    print("Informe a quantidade de números que deseja multiplicar: ")
    N = int(input())
    return [int(input("Informe um número: ")) for i in range(N)]

print()
print(multplica_todos(*recebe_valores()))
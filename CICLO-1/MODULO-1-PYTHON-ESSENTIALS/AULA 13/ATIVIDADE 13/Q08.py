


# def fibonacci(n):
#     if n == 0:
#         return n
#     if n == 1:
#         return 1
#     aux = fibonacci(n-2) + fibonacci(n-1)
#     # print(aux, end=", ")
#     return aux

def fibonacci(n, lista):
    #caso base quando n é 1 ou zero
    if n == 0 or n==1:
        #atribuindo n na lista na posição 0 quando n = 0 
        # e na posição 1 quando n igual a 1
        lista[n] = n
        return n
    #teste para ver se a posição n que está sendo solicitada
    #na recursão já foi realizada, se já tiver sido ela já será retornada
    #isso irá polpar muito trabalho, pois a recursão não precisará recalcular
    #tudo novamente
    if lista[n] != 0:
        return lista[n]
    #calculo do fib de n passando fib de n-1 e fibo de n-2
    #e atribuição desse fibonacci na lista na posição n
    lista[n] = fibonacci(n-2, lista) + fibonacci(n-1, lista)
    #verificação para imprimir a lista se for a ultima chamada da recursão
    if lista[-1] != 0:
        print(f"A sequência fibonacci de 0 até {n} é:")
        print(lista)
    #renorno de fibo de n
    return lista[n]


entrada = int(input("Digite um número inteiro positivo n: "))
fibo = fibonacci(entrada, [0]*(entrada+1))
# ultimo = fibonacci(entrada)
print(f"O Fibonacci de {entrada} é: {fibo}")


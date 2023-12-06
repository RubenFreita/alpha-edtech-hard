"""
Entrada: O programa recebe um número inteiro N maior ou igual a zero.

Saída: O programa deve imprimir Verdadeiro se N é fatorial, 
caso contrário deve imprimir Falso.
"""
print("Algoritmo para verificar se é Fatorial!")
N = int(input("Digite um número inteiro N maior ou igual a 0: ",))
i = 1
result = 1
while result < N:
    result *= i
    i += 1

if result == N:
    print(f"Verdadeiro")
elif N == 0:
    print("Verdadeiro")
else:
    print(f"Falso")
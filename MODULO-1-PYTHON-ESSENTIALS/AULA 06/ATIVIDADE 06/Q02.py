"""
Entrada: O seu programa deve receber um número inteiro positivo N, que é o tempo inicial do temporizador.

Saída: Seu programa deve escrever a saída conforme os exemplos abaixo.
"""

N = int(input("Digite o número correspondente ao inicio da contagem: "))
count = 0
print(f"N = {N}")
print("Faltam ",N, "segundos")
while N - count>=0:
    count += 2
    N = N - count
    if N > 0:
        print("Faltam ",N, "segundos")
print("Acabou")
"""
Entradas: A primeira entrada é um número inteiro N, representando a 
quantidade de medições de velocidade do motor em um determinado teste. 
Cada uma das próximas N entradas consiste de um único inteiro 
M (0 ≤ M ≤ 10000) representando o número de RPM (rotações por minuto) 
daquela medida.

Saídas: A saída é o índice da medição em que ocorreu a primeira queda 
de velocidade. Caso não aconteça nenhuma queda, o seu programa deve 
imprimir o número 0. (dica: não precisa armazenar os valores em nenhuma 
lista ou array/vetor, já no mesmo instante da leitura deve ser feito o 
cálculo se o valor lido é menor que o número imediatamente anterior).
"""
N = int(input("Informe o número de medições: "))
queda = 0
for i in range(1, N+1):
    medicao = int(input("Informe a medição: "))
    if 'ant' not in vars():
        ant = medicao
    if medicao < ant and queda == 0:
        queda = i
    ant = medicao
print(queda)
    

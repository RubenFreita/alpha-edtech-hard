"""
Entrada: A entrada consiste de uma sequência de inteiros, um em cada linha, 
representando os valores dos golpes aplicados (valores positivos) e 
recebidos (valores negativos) por Ryu. A luta termina quando o inteiro 
lido for 0. Um round só termina quando um dos jogadores fica com 0 ou menos 
pontos de vida. Você pode assumir que em cada round pelo menos um golpe será aplicado.

Saída: A saída deverá conter apenas uma linha, contendo somente “Ryu venceu”, 
“Ken venceu” ou “Empate”, de acordo com o resultado geral da luta.
"""

pontosRyu = 100
pontosKen = 100
roundsVencidosRyu = 0
roundsVencidosKen = 0
print("Luta Iniciada!")
print("Round 1!")
print("Fight!!!")
rounds = 1

while  'golpe' not in vars() or golpe != 0:
    golpe = int(input("Informe o valor de um novo golpe: "))
    if golpe > 0:
        pontosKen -= golpe
    elif golpe < 0:
        pontosRyu += golpe
    if pontosKen <= 0:
        roundsVencidosRyu +=1
        rounds +=1
        print(f"Round {rounds}!")
        print("Fight!!!")
        pontosKen = 100
        pontosRyu = 100
    if pontosRyu <= 0:
        roundsVencidosKen +=1
        rounds +=1
        print(f"Round {rounds}!")
        print("Fight!!!")
        pontosKen = 100
        pontosRyu = 100
if pontosKen < pontosRyu:
    roundsVencidosRyu +=1
elif pontosRyu < pontosKen:
    roundsVencidosKen +=1
if roundsVencidosRyu > roundsVencidosKen:
    print("Ryu Venceu!")
elif roundsVencidosRyu < roundsVencidosKen:
    print("Ken Venceu!")
elif roundsVencidosRyu == roundsVencidosKen:
    print("Empate!")


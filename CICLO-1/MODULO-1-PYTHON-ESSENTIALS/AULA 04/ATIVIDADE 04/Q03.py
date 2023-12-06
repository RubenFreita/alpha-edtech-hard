#Questão 03

valorSaque = int(input("Informe o valor do saque: "))
restoValor = 0
qtdNotas200 = 0
qtdNotas100 = 0
qtdNotas50 = 0
qtdNotas20 = 0
qtdNotas10 = 0
qtdNotas5 = 0
qtdNotas2 = 0
if valorSaque < 10:
    print("O valor mínimo para saque é 10 Reais.")
elif valorSaque > 1000:
    print("O valor máximo para saque é 1000 Reais.")
elif valorSaque%2==0:
    qtdNotas200 = valorSaque//200
    restoValor = valorSaque%200
    qtdNotas100 = restoValor//100
    restoValor = restoValor%100
    qtdNotas50 = restoValor//50
    restoValor = restoValor%50
    qtdNotas20 = restoValor//20
    restoValor = restoValor%20
    qtdNotas10 = restoValor//10
    restoValor = restoValor%10
    
    qtdNotas2 = restoValor//2
    restoValor = restoValor%2

    
else:
    valorSaque = valorSaque - 5
    qtdNotas5 += 1
    qtdNotas200 = valorSaque//200
    restoValor = valorSaque%200
    qtdNotas100 = restoValor//100
    restoValor = restoValor%100
    qtdNotas50 = restoValor//50
    restoValor = restoValor%50
    qtdNotas20 = restoValor//20
    restoValor = restoValor%20
    qtdNotas10 = restoValor//10
    restoValor = restoValor%10
    
    qtdNotas2 = restoValor//2
    restoValor = restoValor%2


print(f"A quantidade de notas de R$200 é de: {qtdNotas200} notas")
print(f"A quantidade de notas de R$100 é de: {qtdNotas100} notas")
print(f"A quantidade de notas de R$50 é de: {qtdNotas50} notas")
print(f"A quantidade de notas de R$20 é de: {qtdNotas20} notas")
print(f"A quantidade de notas de R$10 é de: {qtdNotas10} notas")
print(f"A quantidade de notas de R$5 é de: {qtdNotas5} notas")
print(f"A quantidade de notas de R$2 é de: {qtdNotas2} notas")

# if (restoValor % 5)%2 == 0:

#         qtdNotas5 = (restoValor//5)
#         restoValor = restoValor%5

# if (restoValor % 5)%2 == 0:

#         qtdNotas5 = (restoValor//5) + qtdNotas5
#         restoValor = restoValor%5
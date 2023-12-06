#Questão 07

valorTotal = int(input("Digite um valor inteiro(em Reais): "))
qtdNotas200 = valorTotal//200
restoValor = valorTotal%200
qtdNotas100 = restoValor//100
restoValor = restoValor%100
qtdNotas50 = restoValor//50
restoValor = restoValor%50
qtdNotas20 = restoValor//20
restoValor = restoValor%20
qtdNotas10 = restoValor//10
restoValor = restoValor%10
qtdNotas5 = restoValor//5
restoValor = restoValor%5
qtdNotas2 = restoValor//2
restoValor = restoValor%2
qtdNotas1 = restoValor//1

print(f"A quantidade de notas de R$200 é de: {qtdNotas200} notas")
print(f"A quantidade de notas de R$100 é de: {qtdNotas100} notas")
print(f"A quantidade de notas de R$50 é de: {qtdNotas50} notas")
print(f"A quantidade de notas de R$20 é de: {qtdNotas20} notas")
print(f"A quantidade de notas de R$10 é de: {qtdNotas10} notas")
print(f"A quantidade de notas de R$5 é de: {qtdNotas5} notas")
print(f"A quantidade de notas de R$2 é de: {qtdNotas2} notas")
print(f"A quantidade de notas de R$1 é de: {qtdNotas1} notas")
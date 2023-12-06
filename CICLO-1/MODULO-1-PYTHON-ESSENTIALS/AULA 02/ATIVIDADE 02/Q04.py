#Questão 04
import math

a = int(input("Digite um número inteiro A: "))
b = int(input("Digite um número inteiro B: "))
x = float(input("Digite um número Real X: "))
y = float(input("Digite um número Real Y: "))

r = a + b*x - math.sqrt(b) + ((a+b)/(x-y))

print(f"O resultado da equação é: {r:.2f}")
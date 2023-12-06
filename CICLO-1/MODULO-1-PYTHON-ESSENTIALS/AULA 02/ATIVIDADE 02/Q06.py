#Questão 06

import math

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = int(input("Digite o terceiro número inteiro: "))

max1 = (a+b)/2 + abs(b-a)/2
max2 = (max1+c)/2 + abs(c-max1)/2

print(f"O maior número dentre os informados é: {int(max2)}")
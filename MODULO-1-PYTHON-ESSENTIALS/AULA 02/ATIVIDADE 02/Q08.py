#Questão08
import math
sqrt = math.sqrt

a = float(input("Digite um número real a: "))
b = float(input("Digite um número real b: "))
c = float(input("Digite um número real c: "))
x = float(input("Digite um número real x: "))

delta = b**2 - 4*a*c

x1 = (-b + sqrt(delta))/(2*a)
x2 = (-b - sqrt(delta))/(2*a)
print(f"X' = {x1}")
print(f"X\" = {x2}")

print(f"X é igual a raiz X'? {x==x1}")
print(f"X é igual a raiz X\"? {x==x2}")
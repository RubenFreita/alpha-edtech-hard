#Questão 02
import math

a = float(input("Digite a largura do seu paralelepípedo: "))
b = float(input("Digite o comprimento do seu paralelepípedo: "))
c = float(input("Digite a altura do seu paralelepípedo: "))

V = a*b*c

d = math.sqrt(a**2+b**2+c**3)

print(f"O volume do paralelepípedo é: {V:.2f}")
print(f"O tamanho da diagonal principal do paralelepípedo é: {d:.2f}")
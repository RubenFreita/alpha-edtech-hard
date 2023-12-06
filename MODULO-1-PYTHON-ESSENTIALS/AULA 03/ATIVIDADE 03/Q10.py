#Questão 10
import time
# numeroInteiro = int(input("Digite um número inteiro: "))
# numeroReal = input("Digite um número real: ")
# nome = input("Informe o seu nome: ")


# with open("questao10.txt", "w") as arquivo:
#     arquivo.write(str(numeroInteiro)+"\n")
#     arquivo.write(str(numeroReal)+"\n")
#     arquivo.write(nome+"\n")

with open("questao10.txt", "r") as arquivo:
    numeroInteiro = arquivo.readline().replace("\n","")
    numeroReal = arquivo.readline().replace("\n","")
    numeroReal = float(numeroReal.replace(",","."))
    nome = arquivo.readline().replace("\n","")

print(f"Número inteiro da primeira linha: {numeroInteiro}")
print(f"Número real da segunda linha: {numeroReal}")
print(f"Nome da terceira linha: {nome}")
time.sleep(3)
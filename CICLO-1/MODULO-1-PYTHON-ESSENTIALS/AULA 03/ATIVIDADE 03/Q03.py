#Questão 03
"""
Entrada: Nome Completo
Sáida: Email no seguinte padrão: primeironome.ultimosobrenome@gmail.com
"""

nomeCompleto = input("Informe seu nome completo: ")
nome = nomeCompleto[0: nomeCompleto.find(" ")]
sobrenome = nomeCompleto[-(nomeCompleto[::-1].find(" ")):]


email = nome+"."+sobrenome+"@gmail.com"

print(f"O seu email é: {email}")
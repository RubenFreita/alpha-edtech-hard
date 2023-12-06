#Questão 01
"""
Entrada: Nome e sobrenome
Sáida: Email no seguinte padrão: nome.sobrenome@gmail.com
"""

nome = input("Informe seu nome: ")
sobrenome = input("Informe seu sobrenome: ")

email = nome+"."+sobrenome+"@gmail.com"

print(f"O seu email é: {email}")
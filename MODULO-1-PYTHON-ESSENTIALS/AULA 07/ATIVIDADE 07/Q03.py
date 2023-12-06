"""
ENTRADA: UMA FRASE 'frase'
SAÍDA: A FRASE 'frase' SEM AS VOGAIS
"""

frase = input("Digite a frase que deseja remover as vogais: ")
fraseSemVogais = ""
for letra in frase:
    if letra.lower() != "a" and letra.lower() != "e" and letra.lower() != "i" and letra.lower() != "o" and letra.lower() != "u":
        fraseSemVogais += letra

print(f"{fraseSemVogais}")
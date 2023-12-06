"""
Entrada: Uma frase 'frase'
Saída: Imprime na tela se a frase é ou não um pantograma
"""

alfabeto = "abcdefghijklmnopqrstuvwxyz"
frase = input("Digite a frase que iremos verificar se é um pantograma: ")
count = 0

for letraAlfabeto in alfabeto:
    print(f"letra '{letraAlfabeto}': {frase.lower().count(letraAlfabeto)}")
    if frase.lower().count(letraAlfabeto) > 0:
        count += 1
        print(count)
if count == 26:
    print("A frase informada é um Pantograma!")
else:
    print("A frase informada não é um Pantograma!")
"""
Entrada:
o
Olá todos!
Saída:
lá tds!
Entrada:
e
Nao faz sentido viver sem poder pedalar.
Saída:
Nao faz sntido vivr sm podr pdalar.
"""

letra = input("Digite uma letra: ")
frase = input(f"Informe a frase que iremos remover a letra '{letra}': ")
fraseModificada = ""
for l in frase:
    if l.lower() != letra.lower():
        fraseModificada += l
print(f"{fraseModificada}")
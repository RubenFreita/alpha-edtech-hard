
def conta_palavras(frase):
    palavras = frase.split(" ")
    return len(palavras)


frase1 = "Inconstante, como aura, é por natureza."
print(f"A frase \"{frase1}\" tem {conta_palavras(frase1)} palavras")
frase2 = "Os homens são como as ondas, quando uma geração floresce, a outra declina."
print(f"A frase \"{frase2}\" tem {conta_palavras(frase2)} palavras")
frase3 = "À sua estultícia o homem chama destino."
print(f"A frase \"{frase3}\" tem {conta_palavras(frase3)} palavras")
frase4 = "Pois a flecha não fere os covardes."
print(f"A frase \"{frase4}\" tem {conta_palavras(frase4)} palavras")
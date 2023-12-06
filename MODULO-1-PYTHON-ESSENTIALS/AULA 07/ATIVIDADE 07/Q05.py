"""
Entrada:
Mesmo que a realidade seja um pesadelo, nao podemos deixar de sonhar.
Saída:
Vogais: 40.58%
Consoantes: 40.58%
Espacos: 15.94%
Pontuacoes: 2.90%
"""
caracteres = "aeioubcdfghjklmnpqrstvwxyz .,!?-"
frase = input("Digite uma frase: ")
countVogais = 0
countConsoantes = 0
countEspacos = 0
countPontuacoes = 0

for letra in frase:
    for vogais in caracteres[0:5]:
        if vogais.lower() == letra.lower():
            countVogais += 1
    for consoantes in caracteres[5:26]:
        if consoantes.lower() == letra.lower():
            countConsoantes += 1
    for espaco in caracteres[26]:
        if espaco.lower() == letra.lower():
            countEspacos += 1
    for pontuacoes in caracteres[27:31]:
        if pontuacoes.lower() == letra.lower():
            countPontuacoes += 1
    
print(f"Vogais: {countVogais/len(frase)*100:.2f}%")
print(f"Consoantes {countConsoantes/len(frase)*100:.2f}%")
print(f"Espaços {countEspacos/len(frase)*100:.2f}%")
print(f"Pontuações {countPontuacoes/len(frase)*100:.2f}%")



import random

# Representação das bases nitrogenadas do DNA como string
adenina = 'A'
citosina = 'C'
guanina = 'G'
timina = 'T'
#atribuindo as bases nitrogenadas em uma lista
possibilidades = [adenina, citosina, guanina, timina]
x = ""
#realizando 500 escolhas aleatórias dos items da lista de possibilidades
#e adicionando em uma string x
for i in range(500):
    x += possibilidades[random.randint(0,3)]

# atribuindo x como tupla para uma sequencia de DNA
sequencia_DNA = tuple(x)
print(sequencia_DNA)
#for para printar a sequencia de DNA sem espaços
for i in sequencia_DNA:
    print(i,end="")
print()

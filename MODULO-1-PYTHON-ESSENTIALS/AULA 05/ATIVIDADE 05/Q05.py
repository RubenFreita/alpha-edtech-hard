#Questão 05

"""
O PROGRAMA CÁLCULA A SÉRIE FIBONACCI ATÉ O INDICE 15
"""


r = 1
ant = -1
atual = 1
limite = 15
for i in range(limite+1):
    r = atual + ant
    ant = atual
    atual = r
    if i <limite:
        print(f"{r}", end=", ")
    else:
        print(f"{r}")
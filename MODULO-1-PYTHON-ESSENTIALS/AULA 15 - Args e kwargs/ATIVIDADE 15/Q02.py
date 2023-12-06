
"""
RESPOSTA:
 A função se utiliza de compreensão de lista para utilizar a 
 lista recebida pela função e multiplicar através do for cada
   elemento da lista pelo valor recebido e assim criar uma 
   nova lista contendo os novos valores.
"""

def multiplicar_lista(lista, valor):

    return [elemento * valor for elemento in lista]

 

numeros = [1, 2, 3, 4, 5]

novo_numeros = multiplicar_lista(numeros, 3)

print(novo_numeros)
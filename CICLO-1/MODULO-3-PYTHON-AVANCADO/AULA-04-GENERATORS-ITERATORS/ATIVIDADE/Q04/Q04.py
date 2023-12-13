from sys import getsizeof



# Exemplo de criação de uma lista comum
lista_comum = [x ** 2 for x in range(10**3)]
#armazena todos os elementos da lista na variavel lista_comum



# Exemplo de criação de um generator
generator = (x ** 2 for x in range(10**3))
#armazena apenas o estado inicial do generator
#e só irá devolver os valores dos elementos quando
#quando for solicitado ao ser iterado por um for ou
#pela função next()


for i in generator:
    print(i)
print()

print("Tamanho do generator:")
print(getsizeof(generator))
print("Tamanho da lista:")
print(getsizeof(lista_comum))
"""
Como podemos ver usando a função getsizeof do módulo sys
o total de memória para se armazenar o generator é bem 
menor que o total de memória necessária para se armazenar uma lista.
"""
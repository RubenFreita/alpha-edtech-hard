from sys import getsizeof


quadrados_lista = [x**2 for x in range(1,6)]


quadrados_generator = (x**2 for x in range(1, 6))


print(quadrados_lista)
for i in quadrados_generator:
    print(i)


"""
LIST COMPREHENSION
No list comprehension todos os elementos do range de 1 a 5 
são calculados e adicionados como uma lida na variável quadrados_lista.
Isso faz ser preciso o uso de memória do tamanho do range que nesse caso é 5.

GENERATOR EXPRESSION
Já ao usar o generator expression é criado um objeto generatorna variável
quadrados_generator que tem todas as informações de como serão calculdos
 os seus elementos. Diferente da list comprehension na variável quadrados_generator
 não contém os elementos ao quadrado de 1 a 5, mas apenas a lógica pra se calcular 
 esses elementos. A partir do momento que esses elementos são solicitados o objeto
 devolve um elemento, ou seja, esses elementos serão devolvidos por demanda a 
 medida que serão solicitados. Isso é muito interassnte visto que não precisará 
 de memória para armazenar todos esses elementos de uma vez, mas sim um de cada vez.
"""
print()

print("Tamanho do generator:")
print(getsizeof(quadrados_generator))
print("Tamanho da lista:")
print(getsizeof(quadrados_lista ))
"""
Como podemos ver usando a função getsizeof do módulo sys
o total de memória para se armazenar o generator é bem 
menor que o total de memória necessária para se armazenar uma lista.
"""
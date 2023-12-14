from functools import reduce

lista_de_lista_de_inteiro = [[1,2,3,4,5], [6,7,8,9], [10, 11, 12, 13]]

#usando list comprehension
listas = [ i for lista in lista_de_lista_de_inteiro for i in lista]
print(listas)


#usando reduce com função
def junta_lista(lista1, lista2):
    for i in lista2:
        lista1.append(i)
    return lista1
listas_juntas = reduce(junta_lista, lista_de_lista_de_inteiro)
print(listas_juntas)
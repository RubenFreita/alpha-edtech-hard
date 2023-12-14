from typing import List, Callable


lista_inteiros = [10,200,30,434,5,63,7,89,9,10,11,121,1300,14,155,16,17,18,
                  19,20,403, 1299, 5492, 402]
def transforma_lista_inteiros(\
        lista: List[int], funcao1: Callable, funcao2: Callable) -> List[int]:
    return funcao2(funcao1(lista))

def numero_quadrado(lista: List[int]) -> List[int]:
    return list(map(lambda i: i**2, lista))

def filtro_maiores_400(lista: List[int]) -> List[int]:
    return list(filter(lambda i: i < 400, lista))

lista_transformada = transforma_lista_inteiros(\
    lista_inteiros, numero_quadrado, filtro_maiores_400)
print(lista_transformada)


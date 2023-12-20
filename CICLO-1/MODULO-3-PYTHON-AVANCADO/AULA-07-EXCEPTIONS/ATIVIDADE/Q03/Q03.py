from typing import Union, List

lista = [ 1,2,3,4,5]


def retorna_elemento(index: int, lista: List[int]) -> Union[None, int]:
    try:
        elemento = lista[int(index)]
    except IndexError:
        print("Index informado fora do limites de range da lista!")
    else:
        print("Index informado dentro do limite de rante da lista!")
        return elemento
    

valor1 = retorna_elemento(2,lista)
print(f"Valor da primeira chamada: {valor1}")


valor2 = retorna_elemento(10, lista)
print(f"Valor da segunda chamada: {valor2}")
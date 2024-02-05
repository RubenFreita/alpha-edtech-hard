"""
---
**EXERCÍCIO 03 | SOMA DOS ELEMENTOS DE UMA LISTA**

Criar uma função recursiva que some todos os elementos de uma lista. A função deve aceitar uma lista de números
 como entrada e retornar a soma de seus elementos.

Instruções
1. A lista de números deve ser passada como argumento para a função.
2. A função deve percorrer a lista de maneira recursiva, somando cada elemento ao total.
3. O resultado final deve ser a soma total dos elementos da lista.
"""


def somando_array(array, n):
    if n - 1 == 0:
        return array[n - 1]
    return array[n - 1] + somando_array(array, n - 1)


array = [1, 2, 3, 4, 5, 6, 7]


print(somando_array(array, len(array)))

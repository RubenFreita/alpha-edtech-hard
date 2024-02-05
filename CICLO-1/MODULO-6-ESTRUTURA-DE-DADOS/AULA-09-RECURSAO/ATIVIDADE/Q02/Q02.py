"""
---
**EXERCÍCIO 02 | BUSCA BINÁRIA RECURSIVA**

Implementar o algoritmo de busca binária de maneira recursiva. A função deve buscar um elemento 
dentro de uma lista ordenada e retornar o índice do elemento, caso ele exista, ou indicar de 
alguma forma que o elemento não foi encontrado.

Instruções
1. A lista e o elemento a ser buscado devem ser passados como argumentos para a função.
2. A função deve retornar o índice do elemento se ele for encontrado na lista.
3. Caso o elemento não esteja presente na lista, a função deve retornar -1 ou uma mensagem indicativa.
4. Assuma que a lista já está ordenada.
"""


def busca_binaria(lista_ordenada: list, fim, alvo: str, ini=0):

    if ini <= fim:
        meio = (fim + ini) // 2
        if str(lista_ordenada[meio]) == str(alvo):
            return meio
        elif str(alvo) < str(lista_ordenada[meio]):

            return busca_binaria(lista_ordenada, meio - 1, alvo, ini)
        elif str(alvo) > str(lista_ordenada[meio]):

            return busca_binaria(lista_ordenada, fim, alvo, meio + 1)
    else:
        return -1


lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
resultado = busca_binaria(
    lista,
    len(lista),
    6,
)
if resultado == -1:
    print("O alvo não está na lista!")
else:
    print(f"Alvo {lista[resultado]} encontrado!")

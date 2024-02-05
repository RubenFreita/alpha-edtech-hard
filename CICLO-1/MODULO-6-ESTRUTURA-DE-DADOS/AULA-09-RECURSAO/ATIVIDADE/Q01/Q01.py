"""
---
**EXERCÍCIO 01 | INVERSÃO DE STRING**

Escreva uma função recursiva em Python que recebe uma string como entrada e retorna a string invertida.

Instruções
1. A função deve aceitar uma string como argumento.
2. Não utilize métodos prontos da linguagem para inverter a string diretamente.
3. A solução deve ser puramente recursiva.
"""


def inverte_texto(texto: str, n: int, lista_invertida=[]):
    if n - 1 == 0:
        lista_invertida.append(texto[n - 1])
        return "".join(lista_invertida)
    lista_invertida.append(texto[n - 1])
    return inverte_texto(texto, n - 1, lista_invertida)


texto = "invertido"
n = len(texto)
print(inverte_texto(texto, n))

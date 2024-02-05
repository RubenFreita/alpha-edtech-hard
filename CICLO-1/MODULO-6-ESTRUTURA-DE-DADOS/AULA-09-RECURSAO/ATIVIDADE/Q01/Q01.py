"""
---
**EXERCÍCIO 01 | INVERSÃO DE STRING**

Escreva uma função recursiva em Python que recebe uma string como entrada e retorna a string invertida.

Instruções
1. A função deve aceitar uma string como argumento.
2. Não utilize métodos prontos da linguagem para inverter a string diretamente.
3. A solução deve ser puramente recursiva.
"""


def inverte_texto(array, n):
    if n - 1 == 0:
        return array[n - 1]
    return array[n - 1] + inverte_texto(array, n - 1)


texto = "invertido"
n = len(texto)
print(inverte_texto(texto, n))

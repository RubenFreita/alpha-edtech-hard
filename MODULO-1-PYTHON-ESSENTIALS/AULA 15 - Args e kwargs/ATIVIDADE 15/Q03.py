"""
Crie uma função que receba uma lista de strings e um caractere. 
A função deve retornar uma nova lista contendo apenas as strings 
que contêm o caractere fornecido.
"""

def remove_caractere(lista, caractere):
    lista_com_caractere = []
    for string in lista:
        for char in string:
            if char.lower() == caractere.lower():
                lista_com_caractere.append(string)
                break
    return lista_com_caractere

print(remove_caractere(["joao", "maria", "augusto", "rafaela", "roberto"], "e"))
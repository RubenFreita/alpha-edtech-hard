"""
Entrada: O programa recebe um número inteiro, maior ou igual a 1, 
que indica a dimensão do tabuleiro.

Saída: O programa deve desenhar o tabuleiro com dois caracteres que 
representam as divisões em cores diferentes conforme exemplos 
apresentados a seguir. (dica: print(“x”,end=””) não muda de linha)
"""

entrada = int(input("Digite um número inteiro maior ou igual a 1: "))

for i in range(entrada):
    for j in range(entrada):
        if i % 2==0 and j % 2 == 0:
            print("O",end="")
        if i % 2 == 0 and j % 2 == 1:
            print("X",end="")
        if i % 2 == 1 and j % 2 == 0:
            print("X",end="")
        if i % 2 == 1 and j % 2 == 1:
            print("O",end="")
    print()

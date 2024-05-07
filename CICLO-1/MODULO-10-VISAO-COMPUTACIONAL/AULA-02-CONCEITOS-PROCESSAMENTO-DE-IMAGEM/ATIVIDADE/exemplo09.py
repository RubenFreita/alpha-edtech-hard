import numpy as np
from _morph import mm

# toda entrada de dados com input é um texto (string), usar um input() por linha
exemplo_entrada = """\
7 5
3 2 3 3 4
4 3 0 2 0
2 1 1 0 4
0 3 3 0 0
3 0 3 1 1
0 4 4 0 3
3 3 3 0 4
"""


def imprimirImagem(m):
    # função para imprimir a matriz
    [l, c] = m.shape
    st = ""
    for i in range(l):
        for j in range(c):
            st += str(m[i][j]) + " "
        st += "\n"
    return st


def readImg(h, w):
    # função para ler uma matriz
    m = np.zeros((h, w), dtype=int)
    for l in range(h):  # para cada linha l
        # s = input()    # descomentar esta linha para rodar no moodle
        s = linhas[l + 1]  # comentar esta linha para rodar no moodle
        # print(s.split(' '))
        m[l] = [int(i) for i in s.split(" ") if i]
    return m


# comentar as 4 linhas abaixo antes de pedir para avaliar no moodle
linhas = exemplo_entrada.split("\n")
print("Atenção com os espaços!")
print(linhas)
h, w = [int(i) for i in linhas[0].split(" ") if i]  # ler altura/largura


# descomentar a próxima linha para avaliar no moodle
# h, w = np.array(input().split(' '), dtype=int)

# função para ler uma matriz
m = readImg(h, w)

# função para imprimir a matriz - apenas para verificação
imagem = imprimirImagem(m)
print(imagem)


def readImg2():  # função para ler imagem de tamanho aleatório
    b = []
    ler_linha = input()
    while ler_linha:
        b.append([int(i) for i in ler_linha.split(" ") if i])
        ler_linha = input()
    b = np.array(b).astype("uint8")
    return b


c = (
    readImg2()
)  # copiar e colar uma linha qualquer em cada input, terminar com linha vazia
mm.drawImagePlt(c)
mm.show()

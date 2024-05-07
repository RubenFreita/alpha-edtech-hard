import numpy as np
import matplotlib.pyplot as plt

# Para ler/mostrar uma imagem pequena
# Muito útil para debugar algoritmos de Processamento de Imagens


def imprimirImagem(m):
    l, c = m.shape
    digitos = "%" + str(len(str(np.max(m)))) + "d "
    print('"' + digitos + '"')
    st = ""
    for i in range(l):  # para cada linha
        for j in range(c):  # para cada coluna

            st += digitos % m[i][j]
        st += "\n"
    return st


H, W = 40, 60
K = 255  # tente com um valor maior. O que está ocorrendo?
matriz = (np.random.rand(H, W) * K).astype("uint8")

#
print(matriz)
print()
print("Número máximo dentro da matriz: ", np.max(matriz))
print("Transforma o número máximo em: ", str(np.max(matriz)))
print("Calcula o tamanho do número máximo: ", len(str(np.max(matriz))))
print("Texto do comprimento: ", str(len(str(np.max(matriz)))))
print()

print(imprimirImagem(matriz))
plt.figure(figsize=(5, 5))
_ = plt.imshow(matriz, "gray")
plt.show()


# para mostrar inteiros no eixo vertical
plt.ylim([35, 50])
locs, labels = plt.yticks()
yint = [int(v) for v in locs]
plt.yticks(yint)
_ = plt.imshow(matriz, "gray")
plt.show()

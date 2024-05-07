import cv2
import matplotlib.pyplot as plt
from _morph import mm


import numpy as np, matplotlib.pylab as plt

# criando uma imagem
h, w = 6, 6
f = np.zeros((h, w), dtype=int)
cy, cx = h // 2, w // 2
t = 2
f[cy - t : cy + t, cx - t : cx + t] = 1
f[cy:, cx + 1 : cx + t] = 0
mm.drawImagePlt(f)
mm.show()


def drawImageVizinhos(f, B, x, y):
    h, w = f.shape
    Bh, Bw = B.shape
    Bcx, Bcy = Bw // 2, Bh // 2
    m = min(h, w)
    plt.figure(figsize=(m, m))
    plt.rcParams["xtick.bottom"] = plt.rcParams["xtick.labelbottom"] = False
    plt.rcParams["xtick.top"] = plt.rcParams["xtick.labeltop"] = True
    plt.imshow(f, "gray")
    plt.yticks(range(h))
    plt.xticks(range(w))
    plt.ylabel("y")
    plt.xlabel("x")
    plt.title("Processando pixel (x,y)=(%d,%d)" % (x, y))
    [plt.axvline(i + 0.5, 0, h, color="r") for i in range(w - 1)]
    [plt.axhline(j + 0.5, 0, w, color="r") for j in range(h - 1)]
    [
        plt.plot(
            [i + x - Bcx - 0.5, i + x - Bcx - 0.5],
            [y - Bcy - 0.5, Bh + y - Bcy - 0.5],
            color="y",
            linewidth=5,
        )
        for i in range(Bw + 1)
    ]
    [
        plt.plot(
            [x - Bcx - 0.5, x - Bcx + Bw - 0.5],
            [j + y - Bcy - 0.5, j + y - Bcy - 0.5],
            color="y",
            linewidth=5,
        )
        for j in range(Bh + 1)
    ]


def ero0(f, Bc=np.ones((3, 3), dtype="uint8")):
    H, W = f.shape
    Bh, Bw = Bc.shape
    g = f.copy()  # nas listas, as vezes eu uso assim

    # para varrer imagem na ordem raster
    for y in range(H):  # para cada linha y
        for x in range(W):  # para cada coluna x

            # para cada vizinho de (x,y)
            for by in range(Bh):
                for bx in range(Bw):
                    viz_y = int(y + by - Bh / 2 + 0.5)  # É PURA CONVENÇÃO
                    viz_x = int(x + bx - Bw / 2 + 0.5)

                    # verificar o domínion da image
                    if Bc[by, bx] and 0 <= viz_y < H and 0 <= viz_x < W:

                        # para calcular o mínino dos vizinhos
                        if g[y, x] > f[viz_y, viz_x]:
                            g[y, x] = f[viz_y, viz_x]

            # if int(Bh / 2 - 0.5) - 1 < y < H - int(Bh / 2 - 0.5) and int(
            #     Bw / 2 - 0.5
            # ) - 1 < x < W - int(Bw / 2 - 0.5):
            #     # NÃO MOSTRO VIZINHANÇA DOS PIXELS DE BORDA SOMENTE NESTE EXEMPLO DIDÁTICO !!!
            #     drawImageVizinhos(f, B, x, y)

    return g


B = np.ones((3, 3), dtype=int)
# B = np.array([[0, 1, 0], [1, 1, 1], [0, 1, 0]], dtype=int)
g = ero0(f, B)
# plt.imshow(g)
# plt.show()
mm.drawImagePlt(g)
mm.show()

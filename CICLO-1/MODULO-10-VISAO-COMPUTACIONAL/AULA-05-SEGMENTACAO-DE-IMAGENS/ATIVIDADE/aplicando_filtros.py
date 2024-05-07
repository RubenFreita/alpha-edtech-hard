import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


imagem = cv.imread("minhas_moedas.jpeg", 0)

plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(imagem, "gray"), plt.title("Imagem Original")
plt.subplot(122), plt.hist(imagem.ravel(), 256, [0, 256]), plt.title("Histograma")
plt.show()
h, w = imagem.shape
imagem_limiarizada = np.zeros((h, w))
for i in range(h):
    for j in range(w):

        if imagem[i, j] > 50:
            imagem_limiarizada[i, j] = 255
        # else:
        #     imagem_limiarizada = 0
# _, imagem_limiarizada = cv.threshold(imagem, 127, 255, cv.THRESH_BINARY)

plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(imagem_limiarizada, "gray"), plt.title(
    "Imagem Limiarizada"
)
plt.subplot(122), plt.hist(imagem_limiarizada.ravel(), 256, [0, 256]), plt.title(
    "Histograma"
)
plt.show()


elemento_estruturante = cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
imagem_erodida = cv.erode(imagem_limiarizada, elemento_estruturante, iterations=1)
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(imagem_erodida, "gray"), plt.title(
    "Imagem Processada - Erode"
)
plt.subplot(122), plt.hist(imagem_erodida.ravel(), 256, [0, 256]), plt.title(
    "Histograma"
)
plt.show()

elemento_estruturante = cv.getStructuringElement(cv.MORPH_ELLIPSE, (7, 7))
imagem_dilatada = cv.dilate(imagem_erodida, elemento_estruturante, iterations=6)
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(imagem_dilatada, "gray"), plt.title(
    "Imagem Processada - Dilatada"
)
plt.subplot(122), plt.hist(imagem_dilatada.ravel(), 256, [0, 256]), plt.title(
    "Histograma"
)
plt.show()

elemento_estruturante = cv.getStructuringElement(cv.MORPH_ELLIPSE, (11, 11))
imagem_erodida = cv.erode(imagem_dilatada, elemento_estruturante, iterations=8)
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(imagem_erodida, "gray"), plt.title(
    "Imagem Processada - Erode - Parte 2"
)
plt.subplot(122), plt.hist(imagem_erodida.ravel(), 256, [0, 256]), plt.title(
    "Histograma"
)
plt.show()


# imagem_filtrada = cv.GaussianBlur(imagem_limiarizada, (9, 9), 5)
# plt.figure(figsize=(12, 6))
# plt.subplot(121), plt.imshow(imagem_filtrada, "gray"), plt.title(
#     "Imagem Filtro Gaussiano"
# )
# plt.subplot(122), plt.hist(imagem_filtrada.ravel(), 256, [0, 256]), plt.title(
#     "Histograma"
# )
# plt.show()

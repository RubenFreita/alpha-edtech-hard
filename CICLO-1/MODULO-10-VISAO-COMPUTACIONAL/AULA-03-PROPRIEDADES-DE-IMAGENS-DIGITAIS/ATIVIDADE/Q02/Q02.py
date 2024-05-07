import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread("sudoku.jpeg")
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols, ch = img.shape

# encontrar os pontos que eu quero marcar na imagem
pts1 = np.float32([[48, 58], [354, 48], [20, 373], [376, 377]])
# setar onde eu quero que os pontos que eu encontrei apareçam na nova imagem
pts2 = np.float32([[0, 0], [300, 0], [0, 300], [300, 300]])

# calcula a matriz de transformação através das duas matrizes criadas
# anteriormente
M = cv.getPerspectiveTransform(pts1, pts2)

# aplicando a matriz de transformação M na imagem img e
# definindo um tamanho de 300x300 para a nova imagem
dst = cv.warpPerspective(img, M, (300, 300))

# mostrando as imagens
plt.subplot(121), plt.imshow(img), plt.title("Original")
plt.subplot(122), plt.imshow(dst), plt.title("Transformada")

plt.show()

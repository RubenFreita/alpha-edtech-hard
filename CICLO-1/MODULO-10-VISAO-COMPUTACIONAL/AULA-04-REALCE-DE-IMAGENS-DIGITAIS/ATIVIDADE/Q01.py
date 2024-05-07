import cv2 as cv
import matplotlib.pyplot as plt


imagem = cv.imread("imagem 1.png", 0)


hf = cv.calcHist([imagem], [0], None, [256], [0, 256])
plt.figure(figsize=(12, 6))
plt.subplot(121), plt.imshow(imagem, "gray"), plt.title("Imagem Original")
plt.subplot(122), plt.plot(hf), plt.title("Histograma")
plt.show()


imagem_equalizada = cv.equalizeHist(imagem)
plt.figure(figsize=(12, 6))

plt.subplot(121), plt.imshow(imagem_equalizada, "gray"), plt.title("Imagem Equalizada")
plt.subplot(122), plt.hist(imagem_equalizada.ravel(), 256, [0, 256]), plt.title(
    "Histograma"
)
plt.show()

# imgTratada = cv.medianBlur(imagem_equalizada, 5)
imgTratada = cv.GaussianBlur(imagem_equalizada, (3, 3), 0)
# imgTratada = cv.bilateralFilter(imagem1, 9, 75, 75)

plt.figure(figsize=(12, 6))

plt.subplot(121), plt.imshow(imgTratada, "gray"), plt.title("Imagem Filtro Gaussiano")
plt.subplot(122), plt.hist(imgTratada.ravel(), 256, [0, 256]), plt.title("Histograma")
plt.show()

plt.figure(figsize=(12, 6))
imgFiltrada = cv.Laplacian(imgTratada, cv.CV_8U)
imgRealcada = cv.subtract(imgTratada, imgFiltrada)
plt.subplot(121), plt.imshow(imgRealcada, "gray"), plt.title(
    "Imagem Realçada - Subtratc"
)
plt.subplot(122), plt.hist(imgRealcada.ravel(), 256, [0, 256]), plt.title("Histograma")
plt.show()

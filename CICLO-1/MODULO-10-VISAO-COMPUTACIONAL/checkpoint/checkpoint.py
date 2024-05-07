import cv2
import matplotlib.pyplot as plt

imagem = cv2.imread("rice.png", 0)
# imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)

# plt.hist(imagem.ravel())

imagem[imagem <= 120] = 0
imagem[imagem > 120] = 255
kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
print(kernel)
erode = cv2.erode(imagem, kernel, iterations=3)
dilate = cv2.dilate(erode, kernel, iterations=3)
laplacian = cv2.Laplacian(dilate, cv2.CV_8U)
plt.figure(figsize=(10, 10))
plt.subplot(121), plt.imshow(laplacian, "gray"), plt.title("imagem")
plt.subplot(122), plt.imshow(dilate, "gray"), plt.title("erodida")
# plt.subplot(122), plt.hist(imagem.ravel(), 256, [0, 256]), plt.title("Histograma")
plt.show()
print(imagem)
# print(imagem_rgb)

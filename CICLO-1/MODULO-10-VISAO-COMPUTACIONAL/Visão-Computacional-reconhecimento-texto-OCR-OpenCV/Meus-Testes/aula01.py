import pytesseract as pt
import numpy as np
import cv2
import matplotlib.pyplot as plt
from PIL import Image


# pt.pytesseract.tesseract_cmd = r"C:/Program Files/Tesseract-OCR"
# img = cv2.imread("text-recognize/Imagens/Aula1-teste.png")
# img = cv2.imread("text-recognize\Imagens\Aula2-undersampling.png")
# img = cv2.imread("text-recognize/Imagens/imagem-torta.png")
img = Image.open("text-recognize/Imagens/imagem-torta.png")
# under = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# print(img)
plt.imshow(img)
plt.show()

# texto = pt.image_to_string(under, lang="por", config="--tessdata-dir tessdata --psm 6")
# print(texto)
texto = pt.image_to_osd(img, lang="osd")
print(texto)

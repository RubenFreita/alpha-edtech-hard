import cv2
import matplotlib.pyplot as plt
import numpy as np


img = cv2.imread("minhas_moedas.jpeg")


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

plt.figure(figsize=(12, 10))
plt.subplot(121), plt.imshow(img, "gray"), plt.title("Input")
plt.subplot(122), plt.imshow(thresh, "gray"), plt.title("Thresholding")
plt.show()


# noise removal
kernel = np.ones((3, 3), np.uint8)
opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=2)

kernel_elipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (7, 7))
# sure background area
sure_bg = cv2.morphologyEx(opening, cv2.MORPH_DILATE, kernel_elipse, iterations=10)

plt.figure(figsize=(12, 10))
plt.subplot(121), plt.imshow(opening, "gray"), plt.title("opening")
plt.subplot(122), plt.imshow(sure_bg, "gray"), plt.title("sure_bg")
plt.show()


# Finding sure foreground area
dist_transform = cv2.distanceTransform(sure_bg, cv2.DIST_L2, 5)
print(dist_transform.max())
print(0.7 * dist_transform.max())
ret, sure_fg = cv2.threshold(dist_transform, 0.7 * dist_transform.max(), 255, 0)


plt.figure(figsize=(12, 10))
plt.subplot(121), plt.imshow(dist_transform, "gray"), plt.title("dist_transform")
plt.subplot(122), plt.imshow(sure_fg, "gray"), plt.title("sure_fg")
plt.show()

# Finding unknown region
sure_fg = np.uint8(sure_fg)
unknown = cv2.subtract(sure_bg, sure_fg)
plt.imshow(unknown, "gray"), plt.title("Encontrando os Centros")
plt.show()


# Marker labelling
ret, markers = cv2.connectedComponents(sure_fg)
print(markers.min(), markers.max())
print(markers)
# Add one to all labels so that sure background is not 0, but 1
markers = markers + 1
print(markers)

# Now, mark the region of unknown with zero
markers[unknown == 255] = 0

plt.figure(figsize=(7, 10))
plt.imshow(markers, "pink"), plt.title("markers")
plt.show()


plt.imshow((markers == 10) * 255, "gray")
print(np.sum(markers == 10) * 1)
plt.show()


markers = cv2.watershed(img, markers)
plt.figure(figsize=(7, 10))
plt.imshow(markers, "gray"), plt.title("markers watershed")
plt.show()

bordas_segmentadas = (markers == -1) * 255
kernel_elipse = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
# sure background area
bordas_segmentadas = np.uint8(bordas_segmentadas)
bordas_segmentadas = cv2.dilate(bordas_segmentadas, kernel_elipse, iterations=2)

plt.figure(figsize=(7, 10))
plt.imshow(bordas_segmentadas, "gray")
plt.show()


img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_rgb[bordas_segmentadas == 255] = [255, 0, 255]

print(np.amin(markers), np.amax(markers))

plt.figure(figsize=(8, 10))
plt.imshow(img_rgb, "gray"), plt.title("imagem")
plt.show()

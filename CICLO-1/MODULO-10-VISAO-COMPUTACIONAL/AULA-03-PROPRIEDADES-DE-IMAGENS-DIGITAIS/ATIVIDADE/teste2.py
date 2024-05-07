import numpy as np
import cv2 as cv

img = cv.imread("imagem 2.png", cv.IMREAD_GRAYSCALE)
assert img is not None, "file could not be read, check with os.path.exists()"
rows, cols = img.shape

# M = np.float32(
#     [
#         [1, 0, 100],  # 100 pixels para ao lado direito
#         [0, 1, 200],  # 200 pixels para baixo
#     ]
# )
# dst = cv.warpAffine(img, M, (cols, rows))

# cv.imshow("img", dst)

imagemModificada = cv.resize(img, None, fx=0.5, fy=0.5, interpolation=cv.INTER_CUBIC)
cv.imshow("Resultado", imagemModificada)
cv.waitKey(0)
cv.destroyAllWindows()
# cv.waitKey(0)
# cv.destroyAllWindows()

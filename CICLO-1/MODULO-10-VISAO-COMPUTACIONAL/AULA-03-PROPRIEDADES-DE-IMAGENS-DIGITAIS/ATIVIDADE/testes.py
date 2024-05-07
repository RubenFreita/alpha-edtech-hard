import numpy as np
import cv2 as cv

img = cv.imread("imagem 1.png")
assert img is not None, "file could not be read, check with os.path.exists()"

res = cv.resize(img, None, fx=2, fy=2, interpolation=cv.INTER_CUBIC)

cv.imshow("imagem", res)
cv.waitKey(0)
# OR

height, width = img.shape[:2]
res = cv.resize(img, (2 * width, 2 * height), interpolation=cv.INTER_CUBIC)

cv.imshow("imagem", res)
cv.waitKey(0)
cv.destroyAllWindows()

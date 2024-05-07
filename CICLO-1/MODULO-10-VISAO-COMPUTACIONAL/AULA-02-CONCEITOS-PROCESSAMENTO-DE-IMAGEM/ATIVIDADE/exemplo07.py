from _morph import *
import numpy as np
import matplotlib.pyplot as plt

# usando o arquivo _morph.py
H, W = 40, 60
K = 255  # tente com um valor maior. O que está ocorrendo?
matriz = (np.random.rand(H, W) * K).astype("uint8")

print(mm.drawImage(matriz))
mm.drawImagePlt(matriz)
mm.show()

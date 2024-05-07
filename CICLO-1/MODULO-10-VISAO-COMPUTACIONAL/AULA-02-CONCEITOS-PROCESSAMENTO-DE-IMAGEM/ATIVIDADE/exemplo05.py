import numpy as np


# Matriz

a = [0, 0] * 10
print(a)
print(len(a))
print()

b = [a] * 10
print(np.array(b))
print()


c = np.ones((10, 10), dtype="uint8") * 255
print(c)
print()

d = np.matrix("3 1; 6 4")
print(d)
print(type(d))
print()

e = np.matrix("3 5; 0 2")
print(e)
print()

print(d + 10)
print()

print(d + e)
print()

f = d * e
print(f)
print()

transposta = f.T  # transposta de f
print(transposta)

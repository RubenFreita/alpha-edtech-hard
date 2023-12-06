
conjunto_imutavel = frozenset({4, 5, 6})
conjunto_de_frozensets = {conjunto_imutavel, frozenset({7, 8, 9})}

print(conjunto_de_frozensets)
# Saída: {frozenset({4, 5, 6}), frozenset({7, 8, 9})}
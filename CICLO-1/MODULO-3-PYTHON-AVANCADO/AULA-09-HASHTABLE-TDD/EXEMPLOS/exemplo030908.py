import numpy as np

# Preenchendo o array com valores aleatórios
tamanho_array = 100_000_001
array_inteiros = np.random.randint(1, 10001, tamanho_array)

# Imprimindo os últimos 3000 elementos do array
print("Últimos 3000 elementos:", array_inteiros[:-3000])

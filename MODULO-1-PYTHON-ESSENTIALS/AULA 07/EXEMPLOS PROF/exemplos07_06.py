x = [3, 41, 12, 9, 74, 15]
print(type(x))

for valoresLista in x:
    print('Laço:', valoresLista)

print(x)
print(*x)
print(type(x))
#for valoresLista in x:
#    print('Laço:', valoresLista)

print(max(x))
print(sum(x))

# Importing the statistics module
import statistics
print(statistics.mean(x))

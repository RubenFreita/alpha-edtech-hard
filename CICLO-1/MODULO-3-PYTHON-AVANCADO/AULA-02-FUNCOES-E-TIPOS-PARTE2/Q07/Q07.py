
# Lista inicial de cores
cores = ['vermelho', 'azul', 'verde']

# Adicionando um número à lista
#cores.append(42) - podemos ver que ao adicionar um número a lista de cores dará um erro

#o erro acontece por causa da mutalidade do tipo que será percorrido pelo join
#já que ele espera apenas strings, isso exemplifica a mutalidade de tipos


# Tentativa de concatenar todas as cores em uma string
concatenacao_cores = ', '.join(cores)  # Erro: tentativa de concatenar str com int

print(concatenacao_cores)

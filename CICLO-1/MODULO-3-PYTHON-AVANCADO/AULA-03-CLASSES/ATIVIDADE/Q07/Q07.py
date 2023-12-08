
# Lista inicial de cores
cores = ['vermelho', 'azul', 'verde', 'laranja', 'rosa', 'branco']
print("As cores disponíveis são: ")
#concatenar todas as cores em uma string
concatenacao_cores = ", ".join(cores)
print(concatenacao_cores)

try:
# Adicionando um número à lista
    #cores.append(42) #- podemos ver que ao adicionar um número a lista de cores dará um erro


#o erro acontece por causa da mutalidade do tipo que será percorrido pelo join
#já que ele espera apenas strings, isso exemplifica a mutalidade de tipos


# Tentativa de concatenar todas as cores em uma string
    concatenacao_cores = ', '.join(cores)  # Erro: tentativa de concatenar str com int

except:
    cores.pop() #remove o int adicionado

    concatenacao_cores = ', '.join(cores)  #Sem erro pois entrou no except  foi removido o int da string de cores
print()  
print("As cores disponíveis são: ")
print(concatenacao_cores)

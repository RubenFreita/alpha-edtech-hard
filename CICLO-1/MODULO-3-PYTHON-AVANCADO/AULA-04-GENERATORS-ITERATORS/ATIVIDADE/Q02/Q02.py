

def fibonacci(n):
    i = 0
    #atribuido os valores bases ao alemento atual e ao proximo
    atual, proximo = 0, 1
    #while que irá calcular os elementos de fibonacci de 0 até n
    while i < n:
        #ao uma função usar o yield ela se torna um generate e 
        #retorna o valor do elemento atual e salva o estado da função 
        #até que o objeto generate seja iterado novamente
        #na proxima iteração ele continuará a partir da linha após 
        #o yield normalmente.
        yield atual
        atual, proximo = proximo, atual + proximo
        i+=1

#iterando sobre o objeto generate usando o for
for i in fibonacci(10):
    print(i)


#criando uma lista através do objeto generate
fib = list(fibonacci(6))
print(fib)
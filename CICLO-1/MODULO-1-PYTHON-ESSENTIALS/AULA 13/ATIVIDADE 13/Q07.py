
#fibonacci iterativo

def fibonacci(n):
    ant = 1
    atual = 0
    for i in range(n+1):
        
        print(atual, end=", ")
        ant, atual = atual, ant + atual
        

fibonacci(13)
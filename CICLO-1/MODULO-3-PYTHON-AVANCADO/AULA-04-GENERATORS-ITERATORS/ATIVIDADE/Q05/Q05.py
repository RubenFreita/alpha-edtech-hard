#Exemplo usando Yield e generator


#função retorna um conjunto de valores de a elevado i, onde 
# i é menor que n
def pow(a, n):
    i = 1
    r = 1
    while i<=n+1:
        yield r
        r *= a
        i +=1

elevado = pow(2, 10)

for i in elevado:
    print(i)
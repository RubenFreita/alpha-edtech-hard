import statistics as st #importando lib de estatísticas e nomeando como st

with open("ConjuntoDeDadosQ02.txt", "r") as arquivo: #abrindo arquivo txt da questão 02 em modo de leitura
    conjunto_dados = [] 
    #for para ler o arquivo e adicionar cada valor em um array passando de str para int
    for i in arquivo.read().split(","):
        conjunto_dados.append(int(i))

# print(conjunto_dados)
# print(type(conjunto_dados))
media = round(st.mean(conjunto_dados), 2) #capturando a média do array com a função mean
mediana = st.median(conjunto_dados)#capturando a mediana do array com a função median
maximo = max(conjunto_dados)#capturando o maior número do array com a função max
minimo = min(conjunto_dados)#capturando o menor número do array com a função min
amplitude = maximo - minimo #capturando a amplitude do array subtraindo o maior pelo menor valor do array
primeros5 = conjunto_dados[:5] #capturando os 5 primeiros números do array
ultimos5 = conjunto_dados[-5:] #capturando os 5 últimos números do array
#capturando o desvio padrão do array com a função pstdev
desvio_padrao = round(st.pstdev(conjunto_dados, media), 2)
#capturando a variância do array com a função variance
variancia = round(st.variance(conjunto_dados, media),2)

#prints explicano cada conceito e mostrado o resultado correspondente ao array
print(f"A média é a soma de todos os valores de um conjunto de número \ndivido pelo total de números desse conjunto.")
print(f"A média do array de inteiros é: {media}")
print(f"A mediana é o valor que está no centro de um certo conjunto de números.")
print(f"A média do array de inteiros é: {mediana}")
print(f"O valor máximo de um conjunto de dados é o maior valor dentre eles.")
print(f"O valor máximo do array de inteiros é: {maximo}")
print(f"O valor mínimo de um conjunto de dados é o menor valor dentre eles.")
print(f"O valor mínimo do array de inteiros é: {minimo}")
print(f"A amplitude de um conjunto de dados é a distância do menor valor ao maior valor desse conjunto de dados.")
print(f"A amplitude do array de inteiros é : {amplitude}")
print(f"Os 5 primeiros números de um conjunto de dados é os 5 primeiros \nnúmeros da sequêcia desse conjuntos de dados.")
print(f"Os 5 primeiros números do array de inteiros é: {primeros5}")
print(f"Os 5 últimos números de um conjunto de dados são os 5 últimos \nnúmeros da sequêcia desse conjuntos de dados.")
print(f"Os 5 primeiros números do array de inteiros é: {ultimos5}")
print(f"O desvio padrão ou desvio padrão populacional é uma medida \nde dispersão em torno da média populacional de uma variável aleatória.")
print(f"O desvio padrão do array de inteiros fornecidos é: {desvio_padrao}")
print(f"a variância de uma variável aleatória ou processo estocástico é uma \nmedida da sua dispersão estatística, indicando \"o quão longe\" \nem geral os seus valores se encontram do valor esperado.")
print(f"A Variância do array de inteiros é: {variancia}")
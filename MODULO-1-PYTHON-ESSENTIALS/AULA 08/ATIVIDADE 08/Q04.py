import statistics as st #importando lib de estatísticas e nomeando como st

with open("ConjuntoDeDadosQ02.txt", "r") as arquivo: #abrindo arquivo txt da questão 02 em modo de leitura
    conjunto_dados = [] 
    #for para ler o arquivo e adicionar cada valor em um array passando de str para int
    for i in arquivo.read().split(","):
        conjunto_dados.append(int(i))


media = round(st.mean(conjunto_dados), 2) #capturando a média do array com a função mean
mediana = st.median(conjunto_dados) #capturando a mediana do array com a função median
maximo = max(conjunto_dados)#capturando o maior número do array com a função max
minimo = min(conjunto_dados)#capturando o menor número do array com a função min
amplitude = round(maximo - minimo, 2) #capturando a amplitude do array subtraindo o maior pelo menor valor do array
primeros5 = conjunto_dados[:5] #capturando os 5 primeiros números do array
ultimos5 = conjunto_dados[-5:] #capturando os 5 últimos números do array

#capturando o desvio padrão do array com a função pstdev
desvio_padrao = round(st.pstdev(conjunto_dados, media), 2)
#capturando a variância do array com a função variance
variancia = round(st.variance(conjunto_dados, media),2)
#conjunto dos dados lidos sem os valores que são outliers, ou seja, são números que
#foge do padrão dos outros números.
conjunto_dados_sem_outliers = []
for i in conjunto_dados:
    #if para capturar apenas os valores que estão dentro do range dos
    #que números que não são considerados outleirs
    if media - 2*desvio_padrao <= i <= 2*desvio_padrao + media:
        conjunto_dados_sem_outliers.append(i)# adicionando os números que não são outliers
#prints do array com e sem outliers
print("array com os outliers:")
print(conjunto_dados)
print("array sem os outliers:")
print(conjunto_dados_sem_outliers)
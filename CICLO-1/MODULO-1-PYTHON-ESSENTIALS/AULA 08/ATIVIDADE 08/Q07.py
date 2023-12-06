
# - abrindo o arquivo da questão 06 em modo de leitura
with open("ConjuntoDeDadosQ06.txt", "r") as arquivo:
    
    # - lendo o arquivo e fazendo um cast para transformar a str em um array
    #através da função eval que tenta transformar um str em algum conjunto
    #de dados válidos será ela uma equação ou como nesse caso um array
    conjunto_dados = eval(arquivo.read())

clientes_sem_repeticao = []# - array dos clientes sem repetição
clientes = [] # - array dos clientes que compraram ações, pode ter o nome de um cliente mais de uma vez

# - for para varrer o array de tuplas que contém o conteúdo lido do arquivo
for i in conjunto_dados:
    clientes.append(i[2])# - adicionando os nomes dos clientes no array clientes
    # - if para verificar se o nome do cliente não está contido no array de clientes 
    #sem repetição, se não estiver ele será adicionado
    if i[2] not in clientes_sem_repeticao:
        clientes_sem_repeticao.append(i[2])# - adiciona o nome do cliente no array

# - array que irá conter um array de tuplas com o nome de cada cliente e a 
# quantidade de vezes que cada cliente comprou ações 
# tupla = (cliente, vezes que comprou ações)
contador_clientes = []
# - for que irá varrer o array de clientes sem repetição e irá contar
#quantas vezes cada um realizou compras
for i in clientes_sem_repeticao:
    # - adiciono o nome do cliete e a quantidade de ocorrências do 
    # nome do cliente no array clientes
    contador_clientes.append((i, clientes.count(i)))

#prints do array que contém os clientes e suas quantidades de vezes que compraram ações
print()
print("Array com os clientes e a quantidade de vezes que compraram ações:")
print(contador_clientes)
print()

#=============VERIFICAÇÃO DOS CLIENTES QUE MAIS VEZES COMPRARAM AÇÕES===================

maior = 0 #variave auxiliar para guardar a qtd de compras do maior comprador
indice = 0 #variavel auxilicar que irá guardar o indice do maior comprador
maiores_compradores = set() # - conjunto que irá conter os 3 clientes que compraram mais vezes

# - for que irá ser executado 3 vezes para a cada iteração capturar o cliente que comprou ações mais vezes
for j in range(3):
    # - for mais interno irá varrer o array contador de clientes e irá verificar qual
    #é o cliente que mais vezes comprou ações
    for i in contador_clientes:
        # - verificação que irá checar se o cliente atual comprou mais vezes que o cliente
        #que o valor guardado pelo cliente checado anteriormente
        #Obs.: como a variável maior é inicializada por 0, e todos os clientes fez pelo menos
        #uma compra então a primeira verificação será verdadeira e maior vai 
        # receber a qtd de compras do cliente
        if i[1] > maior:  
            maior = i[1] # atribui a qtd de compras do cliente verificado à variável maior
            indice = contador_clientes.index(i) # captura o index do cliente e atribuir a variavel indice
    # print(contador_clientes[indice][0])
    # - adiciona o nome do cliente que comprou ações mais 
    # vezes no conjunto de maiores compradores
    maiores_compradores.add(contador_clientes[indice][0])
    # - remove o cliente que mais comprou do array que está sendo varrido para 
    #não constar nas próximas verivicações, ou seja, na próxima iteração do for externo
    #o for interno irá capturar o segundo cliente que comprou ações mais vezes
    contador_clientes.remove(contador_clientes[indice])
    maior = 0 #reseta a varivel
    indice = 0 #reseta a variavel

#=============VERIFICAÇÃO DOS CLIENTES QUE MENOS VEZES COMPRARAM AÇÕES===================

# - A lógica é a mesma da captura dos clientes que mais vezes compraram ações

menores_compradores = set()
for j in range(3):
    for i in contador_clientes:
        # - a unica diferença é que se calcularmos um valor menor que zero nunca entraremos
        #no if já que é impossível ter compra menor que zero
        # - então primeiro é verificado se a variavel já foi criada antes, se não tiver sido 
        #a condição do if é satisfeita e a variavel menor é criada e atribuido o valor a ela
        if "menor" not in vars() or i[1] < menor:
            menor = i[1]
            indice = contador_clientes.index(i)
    menores_compradores.add(contador_clientes[indice][0])
    contador_clientes.remove(contador_clientes[indice])
    # - função del apaga a variável menor, garantindo que ela não exista na proxima iteração do for externo
    del menor 
    indice = 0

# - prints dos conjuntos separados e juntos
print("Conjunto dos clientes que compraram ações mais vezes:")
print(maiores_compradores)
print()
print("Conjunto dos clientes que compraram ações menos vezes:")
print(menores_compradores)
maiores_menores = set()
maiores_menores =  menores_compradores.union(maiores_compradores)
print()
print("União entre os conjuntos dos clientes que compraram ações mais e menos vezes:")
print(maiores_menores)

#=========================VALOR TOTAL DE COMPRA DE CADA CLIENTE===============================

# - array de tuplas que irá conter o nome dos clientes e o 
# valor total comprado por cada cliente
valor_total_clientes = []
# - variavel auxiliar que irá conter temporariamente a soma dos valores
#totais comprados por cada cliente
total_comprado = 0

# - for que irá percorrer o array que contém o nome de cada
#cliente sem repetição dos nomes
for i in clientes_sem_repeticao:
    # - for mais interno irá percorrer o conjunto de dados que foi lido do arquivo txt
    for j in conjunto_dados:
        # - o if verifica se o nome do cliente no conjunto de dados é igual ao do 
        #for mais externo, se for ele vai somar o valor total da compra do cliente
        #a variavel total comprado
        if i == j[2]:
            # - a variavel vai receber o produto da quantidade de ações comprada
            #pelo valor da ação, em todas as compras realizadas por este cliente
            total_comprado += j[0]*j[1]
    # - é adicionado ao array de tuplas o nome do cliente e o valor total comprado
    valor_total_clientes.append((i,round(total_comprado,2)))
    total_comprado = 0 # resetando a variavel auxiliar de total comprado pelo cliente

# - print do array de tuplas
print()
print("Array com o valor total de ações compradas por cada cliente: ")
print(valor_total_clientes)

#================VERIFICAÇÃO DE QUAL CLIENTE COMPROU UM VALOR MAIOR DE AÇÕES===============================


maior_compra = 0 # - variavel auxiliar que irá guardar o valor do maior total de compras
conjunto_maiores_compradores = set() # - conjunto maiores compradores de ações

# - for externo para capturar os 3 clientes que compraram o valor mais alto de ações
for j in range(3):
    # - for interno que irá percorrer o array de maiores compradores de ações
    for i in valor_total_clientes:
        # - o if irá verificar se o valor de compra do cliente atual é maior que o 
        #da variavel maior compra
        if i[1] > maior_compra:
            maior_compra = i[1] # - atribuição do maior valor de compras a variavel maior compra
            indice = valor_total_clientes.index(i) # - captura do indice do cliente que o valor mais alto de ações
    #adiciona o nome do cliente que mais comprou um valor mais alto de ações
    conjunto_maiores_compradores.add(valor_total_clientes[indice][0])
    # - remove o cliente do array que contém os nomes dos clientes e os valores gastos
    valor_total_clientes.remove(valor_total_clientes[indice])
    indice = 0 # - reseta a variavel
    maior_compra = 0 # - reseta a variavel

# - prints dos maiores compradores
print()    
print("Maiores compradores")
print(conjunto_maiores_compradores)

#================VERIFICAÇÃO DE QUAL CLIENTE COMPROU UM VALOR MAIOR DE AÇÕES===============================

# - mesma lógica para os clientes que compraram um valor mais alto de ações
conjunto_menores_compradores = set()
for j in range(3):
    for i in valor_total_clientes:
        # - a única diferença está nesta lógica
        if "menor_compra" not in vars() or i[1] < menor_compra:
            menor_compra = i[1]
            indice = valor_total_clientes.index(i)
    conjunto_menores_compradores.add(valor_total_clientes[indice][0])
    valor_total_clientes.remove(valor_total_clientes[indice])
    indice = 0
    del menor_compra

# - print dos cliente que compraram um menor valor de ações
print()    
print("Menores compradores")
print(conjunto_menores_compradores)

print()

# -  print da união dos dois conjuntos
print("União do conjunto dos clientes que compraram um valor de ações mais alto e mais baixo: ")
print(conjunto_maiores_compradores.union(conjunto_menores_compradores))
import statistics as st


qtd_compras = int(input("Informe a quantidade de compras de ações que será efetuadas: "))
print()
print("Informe agora a quantidade de ação e logo em seguida o valor da ação comprada e o nome do cliente!")



conjunto_dados = [] #array que conterá os dados de qtd e o valor de cada ação
array_qtd_acoes = [] #array que conterá apenas os dados de qtd das ações compradas
array_valor_acoes = [] #array que conterá apenas os dados do valor de cada ação comprada
array_cliente_acoes = [] #array que conterá apenas os nomes do cliente de cada ação comprada
clientes_sem_repeticao = [] #array que conterá apenas o nome de cada cliente sem repetição


#for para capturar a quantidade de ações compradas
#e os valores de cada ação comprada
for i in range(qtd_compras):
    qtd_acoes = int(input("Informe a quantidade de ação: "))#input para capturar a qtd de cada ação comprada
    valor_acao = float(input("Informe o valor da ação: ").replace(",","."))#input para capturar o valor de cada ação comprada
    cliente_dono_acao = input("Informe o nome do cliente que comprou a ação: ")

    #adicionando a qtd de ações em um array separado para fazer as análises estatísticas
    array_qtd_acoes.append(qtd_acoes)
    #adicionando o valor de cada ação em um array separado para fazer as análises estatísticas
    array_valor_acoes.append(valor_acao)
    #adicionando o nome do cliente de cada ação em um array separado para fazer as análises estatísticas
    array_cliente_acoes.append(cliente_dono_acao)

    # -if que irá verificar se não tem ocorrência do nome do cliente na lista dos clientes sem repetição
    # se não tiver o nome do cliente será adicionado na lista.
    # - isso irá garantir que cada cliente só tem uma ocorrência do nome na lista.
    if cliente_dono_acao not in clientes_sem_repeticao:
        clientes_sem_repeticao.append(cliente_dono_acao)

    # adicionando cada qtd e valor em forma de tupla 
    # no array tupla = (quantidade de ação, valor da ação)
    conjunto_dados.append((qtd_acoes,valor_acao,cliente_dono_acao))


#capturando cada dado estatístico em relação ao array das quantidades de ações
media_qtd = round(st.mean(array_qtd_acoes), 2)
mediana_qtd = st.median(array_qtd_acoes)
maximo_qtd = max(array_qtd_acoes)
minimo_qtd = min(array_qtd_acoes)
amplitude_qtd = round(maximo_qtd - minimo_qtd, 2)
primeros5_qtd = array_qtd_acoes[0:5]
ultimos5_qtd = array_qtd_acoes[-5:]
desvio_padrao_qtd = round(st.pstdev(array_qtd_acoes, media_qtd), 2)
variancia_qtd = round(st.variance(array_qtd_acoes, media_qtd),2)
print()

#prints da análise estatísticas do array das quantidades de ações
print("Dados estatísticos das quantidades das ações:")
print(f"A média do array de inteiros é: {media_qtd}")
print(f"A média do array de inteiros é: {mediana_qtd}")
print(f"O valor máximo do array de inteiros é: {maximo_qtd}")
print(f"O valor mínimo do array de inteiros é: {minimo_qtd}")
print(f"A amplitude do array de inteiros é : {amplitude_qtd}")
print(f"Os 5 primeiros números do array de inteiros é: {primeros5_qtd}")
print(f"Os 5 primeiros números do array de inteiros é: {ultimos5_qtd}")
print(f"O desvio padrão do array de inteiros fornecidos é: {desvio_padrao_qtd}")
print(f"A Variância do array de inteiros é: {variancia_qtd}")

media_valores = round(st.mean(array_valor_acoes), 2)
mediana_valores = st.median(array_valor_acoes)
maximo_valores = max(array_valor_acoes)
minimo_valores = min(array_valor_acoes)
amplitude_valores = round(maximo_valores - minimo_valores, 2)
primeros5_valores = array_valor_acoes[0:5]
ultimos5_valores = array_valor_acoes[-5:]
desvio_padrao_valor = round(st.pstdev(array_valor_acoes, media_valores), 2)
variancia_valor = round(st.variance(array_valor_acoes, media_valores),2)
print()

#prints da análise estatísticas do array das quantidades de ações
print("Dados estatísticos dos valores das ações:")
print(f"A média do array de inteiros é: {media_valores}")
print(f"A média do array de inteiros é: {mediana_valores}")
print(f"O valor máximo do array de inteiros é: {maximo_valores}")
print(f"O valor mínimo do array de inteiros é: {minimo_valores}")
print(f"A amplitude do array de inteiros é : {amplitude_valores}")
print(f"Os 5 primeiros números do array de inteiros é: {primeros5_valores}")
print(f"Os 5 primeiros números do array de inteiros é: {ultimos5_valores}")
print(f"O desvio padrão do array de inteiros fornecidos é: {desvio_padrao_valor}")
print(f"A Variância do array de inteiros é: {variancia_valor}")



#for para varrer 
# for i in array_cliente_acoes:
#     if i not in clientes_sem_repeticao:
#         clientes_sem_repeticao.append(i)
print()
#for para varrer o array dos nomes dos clientes sem repetição
for i in clientes_sem_repeticao:
    #-dentro do print foi usado a função count que irá contar o total de ocorrências do
    #nome do de cada cliente no array que contém os nome dos clientes que compraram as ações.
    #-isso irá identificar o total de vezes que cada cliente comprou ações
    print(f"O cliente {i} comprou {array_cliente_acoes.count(i)} ações.")


# with open("ConjuntoDeDadosQ06.txt", "w") as arquivo:
#     arquivo.write(str(conjunto_dados))


# print()
# print(clientes_sem_repeticao)
# print(conjunto_dados)
# print(array_qtd_acoes)
# print(array_valor_acoes)
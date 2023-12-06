import csv #biblioteca para tratamento de arquivos csv
# lista de produtos
produtos = [] 

#abertura do arquivo csv em modo de leitura
with open("produtosQ03.csv", "r", encoding="utf-8") as arquivo:
    #instanciando a criação de um objeto iterável com as informações do 
    #arquivo que foi aberto em modo de leitura e capturando os item que
    #são separados por ponto e vírgula
    arquivo_csv = csv.reader(arquivo, delimiter=";")
    #for para percorrer o objeto iterável 
    #cada linha é uma lista de strings com as informações do produto
    for linha in arquivo_csv:
        #adicionando cada item de cada linha em uma tupla e adicionando
        #esta tupla de produto na lista de produtos
        produtos.append((linha[0], int(linha[1]), int(linha[2]), float(linha[3])))

while 1: #loop infinito para iteração com usuário
    #input do código de produto que o usuário quer alterar
    codigo_produto = input("Informe o código do produto que deseja alterar: ")
    #for para percorrer a lista de produtos
    if codigo_produto == "":
        break
    else:
        for produto in produtos:
            #verificação do codigo informado pelo usuário em cada código existente 
            #na lista de produtos, se haver algum produto que o coódigo seja igual a 
            #condição do if será satisfeita
            if codigo_produto == str(produto[1]):
                print()
                #informações do produto escolhido
                print(f"O produto de código: {codigo_produto} tem as seguintes informações:")
                print(f"Nome: {produto[0]}, código: {produto[1]}, Quantidade: {produto[2]}, Preço: {produto[3]}")
                print()
                #input da nova quantidade atribuida pelo usuário
                nova_qtd = int(input("Informe uma nova quantidade para este produto: "))
                #captura do indice do produto(tupla) que o código pertence
                indice = produtos.index(produto)
                #adicionando o produto(tupla) com a quantidade nova no lugar do produto que 
                #tinha a quantidade de produtos antiga
                produtos[indice] = (produto[0], produto[1], nova_qtd, produto[3])
                print("Quantidade do produto atualizada!")

#percorrendo a lista de produtos após as alterações
for i, produto in enumerate(produtos):
    #substituindo cada tupla por uma nova que tem um campo a mais, que é 
    #o campo de valor total que é igual a quantidade * preço
    produtos[i] = ((produto[0], produto[1], produto[2], produto[3], round(produto[2]*produto[3], 2)))


#criando arquivo csv em modo de escrita
with open("produtosQ05.csv", "w", encoding="utf-8") as arquivo:
    #instanciando um objeto que irá utilizar o arquivo criado e irá
    #escrever cada tupla da lista de produtos no arquivo separado por ;
    csv_write = csv.writer(arquivo, delimiter=";")
    #for que irá percorrer a lista de produtos para escrever cada tupla 
    #no arquivo csv criado
    for linha in produtos:
        csv_write.writerow(linha)





print()
#print dos produtos depois das modificações
print(f"\t  Produtos Depois das Alterações")
print(f"Produto:   (Nome, \tCódigo, Qtd, Preço, \tTotal)")
contador = 0
for produto in produtos:
    contador += 1
    print(f"Produto {contador}: ({produto[0]}, \t{produto[1]},    {produto[2]},  {produto[3]}, \t{produto[4]})")
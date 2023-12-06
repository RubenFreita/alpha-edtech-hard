import csv #biblioteca para tratamento de arquivos csv
# lista de produtos
produtos = []
#lista de produtos antes de realizar as alterações nos produtos
produtos_antes = []

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

#realizando cast de produtos para string e usando a função eval() para que a variável 
#produto_antes não seja uma referência da variável produtos
produtos_antes = eval(str(produtos))

while 1: #loop infinito para iteração com usuário
    #input do código de produto que o usuário quer alterar
    codigo_produto = input("Informe o código do produto que deseja alterar: ")
    #verificação para encerrar o loop infinito se o usuário digitar um campo em branco
    if codigo_produto == "":
        break
    else:
        #for para percorrer a lista de produtos
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








#print dos produtos antes das modificações
print()
print(f"\tProdutos Antes das Alterações")
print(f"Produto:   (Nome, \tCódigo, Qtd, Preço)")
contador = 0
for produto in produtos_antes:
    contador += 1
    print(f"Produto {contador}: ({produto[0]}, \t{produto[1]},    {produto[2]},  {produto[3]})")

print()

#print dos produtos depois das modificações
print(f"\tProdutos Depois das Alterações")
print(f"Produto:   (Nome, \tCódigo, Qtd, Preço)")
contador = 0
for produto in produtos:
    contador += 1
    print(f"Produto {contador}: ({produto[0]}, \t{produto[1]},    {produto[2]},  {produto[3]})")
import csv #biblioteca para tratamento de arquivos csv
# lista de produtos
produtos = []

#abertura de arquivo csv em modo de leitura, 
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

#print da lista de tuplas
print("Lista de produtos")
print(produtos)

print()
#print dos produtos em forma de tabela
print(f"\t  Produtos Cadastrados")
print(f"Produto:   (Nome, \tCódigo, Qtd, Preço)")
contador = 0
for produto in produtos:
    contador += 1
    print(f"Produto {contador}: ({produto[0]}, \t{produto[1]},    {produto[2]},  {produto[3]})")
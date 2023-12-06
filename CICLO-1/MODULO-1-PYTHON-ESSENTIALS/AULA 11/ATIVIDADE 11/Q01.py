
produtos = []
while 1: # loop infinito
    opcao = input("Digite 1 para adicionar um novo produto e 0 para sair: ") #opção de controle de fluxo
    if opcao == "1": #condição de controle de fluxo
        #recebimento das informações do produto
        nome_produto = input("Informe o nome do produto: ") 
        codigo_produto = input("Informe o codigo do produto(com 4 dígitos): ")
        quantidade_produto = input("Informe a quantidade do produto: ")
        preco_produto = input("Informe o preço do produto: ")
        #adicionando o produto em tupla na lista de produtos
        produtos.append((nome_produto, codigo_produto, quantidade_produto, preco_produto))
    elif opcao == "0": #condição de controle de fluxo
        print("Saindo do menu de adicionar produtos...")
        break #break para sair do loop infinito
    else: #opções diferentes de 0 e 1
        print("Opção inválida, informe uma opção válida!!")

print(f"\t  Produtos Cadastrados")
print(f"Produto: (Nome, Código, Quantidade, Preço)")
contador = 0 #contador que vai indicar a numeração do produto
#for para varrer o array de produtos
for produto in produtos:
    contador += 1
    #prints que irá mostrar cada produto e suas informações
    print(f"Produto {contador}: ({produto[0]}, {produto[1]}, {produto[2]}, {produto[3]})")
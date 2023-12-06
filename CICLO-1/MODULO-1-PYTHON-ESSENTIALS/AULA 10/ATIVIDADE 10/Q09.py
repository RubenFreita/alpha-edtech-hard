
armazens = {}
produtos = []

while 1:
    opcao1 = input("Digite o 1 para criar um novo armazém e 0 para encerrar o a criação de armazéns: ")
    if opcao1 == "1":
        armazem = input("Informe o nome do armazém: ")
        while 1:
            opcao2 = input("Digite o 1 para adicionar um novo produto e 0 para sair: ")
            if opcao2 == "1":
                produto = frozenset([input("Informe o código do produto: ")])
                
                if produto not in produtos:
                    produtos.append(produto)
            elif opcao2 == "0":
                break
            else:
                print("Informe uma opção válida!\n")
        armazens[armazem] = frozenset(produtos)
        produtos = []
    elif opcao1 == "0":
        break
    else:
        print("Informe uma opção válida!\n")
print("Informe o nome do armazém que deseja ver os produtos:")
armazem_escolhido = input()
print(f"O armazém escolhido foi o: {armazem_escolhido}")
print("Produtos:")
print(armazens[armazem_escolhido])
with open("saidaQ09.txt", "w") as arquivo:
    arquivo.write(str(armazens))
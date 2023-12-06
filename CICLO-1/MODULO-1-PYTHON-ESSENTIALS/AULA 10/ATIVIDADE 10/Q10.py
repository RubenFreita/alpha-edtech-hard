with open("saidaQ09.txt", "r") as arquivo:
    armazens = eval(arquivo.read())
print("Escolha qual armazém deseja alterar: ")
contador = 0
for i in armazens:
    contador += 1
    print(f"Digite {contador} - para alterar o armazém {i}")
opcao = input()
if opcao == "1":
    produtos = set(armazens["rocha"])
    print(produtos)
elif opcao == "2":
    produtos = set(armazens["freitas"])
elif opcao == "3":
    produtos = set(armazens["doisirmaos"])
else:
    print("Opção inválida, encerrando o programa...")
    exit()
produtos_antigo = str(produtos)

print("Digite 1 para adicionar um produto;")
print("Digite 2 para remover um produto.")
opcao = input("Digite a opção: ")
if opcao == "1":
    produto = frozenset([input("Informe o código do produto que deseja adicionar: ")])
    produtos.add(produto)
    produtos = frozenset(produtos)
    print("Item adicionado com sucesso!!")
elif opcao == "2":
    produto = frozenset([input("Informe o código do produto que deseja remover: ")])
    if produto not in produtos:
        print("Produto inexistente, encerrando o programa...")
        exit()
    produtos.remove(produto)
    produtos = frozenset(produtos)
    print("Item removido com sucesso!")
else:
    print("Opção inválida, encerrando o programa...")
    exit()
print()
print("Produtos antes da operação:")
print(eval(produtos_antigo))
print()
print("Produtos depois da operação:")
print(produtos)
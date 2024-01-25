
# import sys

# sys.path.append(r'C:/Users/ruben/Documents/ALPHAEDTECH/HARD/CICLO-1/MODULO-6-ESTRUTURA-DE-DADOS/AULA-02/ATIVIDADE/Q01')
from models.produto import Produto
from models.estoque import Estoque





def exibir_menu():
    print("\n============= Menu =============")
    print("1. Adicionar Produto")
    print("2. Atualizar Quantidade do Produto")
    print("3. Remover Produto")
    print("4. Listar Produtos")
    print("5. Desordenar Produtos")
    print("6. Ordenar Produtos Por Nome")
    print("7. Ordenar Produtos Por id")
    print("8. Busca Binário")
    print("0. Sair")


def programa(estoque: Estoque):
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-8): ")

        if opcao == "1":
            nome_produto = input("Digite o nome do produto: ")
            valor_produto = float(input("Digite o valor do produto: "))
            quantidade_produto = int(input("Digite a quantidade do produto: "))
            novo_produto = Produto(nome_produto, valor_produto)
            estoque.adicionar_produtos(novo_produto, quantidade_produto)
            input("\nClique em Enter para continuar...\n")

        elif opcao == "2":
            nome_produto = input("Digite o nome do produto a ser atualizado: ")
            quantidade_produto = int(input("Digite a nova quantidade: "))
            produto_a_atualizar = Produto(nome_produto, 0)
            estoque.atualizar_qtd_produto(produto_a_atualizar, quantidade_produto)
            input("\nClique em Enter para continuar...\n")

        elif opcao == "3":
            nome_produto = input("Digite o nome do produto a ser removido: ")
            produto_a_remover = Produto(nome_produto, 0)
            estoque.remover_produtos(produto_a_remover)
            input("\nClique em Enter para continuar...\n")

        elif opcao == "4":
            estoque.listar_produtos()
            input("\nClique em Enter para continuar...\n")

        elif opcao == "5":
            estoque.produtos.desordena()
            input("\nClique em Enter para continuar...\n")
        elif opcao == "6":
            estoque.produtos.ordena_nome()
            input("\nClique em Enter para continuar...\n")
        elif opcao == "7":
            estoque.produtos.ordena_id()
            input("\nClique em Enter para continuar...\n")
        elif opcao == "8":
            alvo = input("\nInforme o nome do produto: ")
            print("\nResultado da Busca Binária:")
            print(estoque.produtos.busca_binaria(alvo))
            input("\nClique em Enter para continuar...\n")
        

        elif opcao == "0":
            print("Saindo do programa. Até logo!")
            break

        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")
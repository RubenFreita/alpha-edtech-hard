from collections import deque
import os


class NodeTree:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __eq__(self, other) -> bool:
        if other != None:
            if self.data == other.data and isinstance(other, NodeTree):
                return True
            else:
                return False


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insere(self, data):
        new_node = NodeTree(data)
        if self.root == None:
            self.root = new_node
            print(
                f"\nINFO: O documento '{new_node.data}' foi adicionado como raiz no sistema!"
            )
            return

        node = self.root
        while node:
            if new_node.data < node.data:
                if node.left == None:
                    node.left = new_node
                    print(f"\nINFO: O documento {new_node.data} foi adicionado!")
                    return
                node = node.left
            elif new_node.data > node.data:
                if node.right == None:
                    node.right = new_node
                    print(f"\nINFO: O documento {new_node.data} foi adicionado!")
                    return
                node = node.right
            else:
                print(
                    f"\nINFO: O nó {new_node.data} já existe na arvore e não pode ser adicionado!"
                )
                return

    def modify_document(self, key, modify):
        doc_modify = NodeTree(key)
        if self.root == None:
            print(f"\nINFO: O documento '{doc_modify.data}' não foi encontrado!")
            print("INFO: Tente adicioná-lo no sistema se desejado!")
            return

        node = self.root
        while node:
            if doc_modify.data < node.data:
                if node.left == None:
                    print(
                        f"\nINFO: O documento '{doc_modify.data}' não foi encontrado!"
                    )
                    print("INFO: Tente adicioná-lo no sistema se desejado!")
                    return
                node = node.left
            elif doc_modify.data > node.data:
                if node.right == None:
                    print(
                        f"\nINFO: O documento '{doc_modify.data}' não foi encontrado!"
                    )
                    print("\nINFO: Tente adicioná-lo no sistema se desejado!")
                    return
                node = node.right
            else:
                self.delete(key)
                self.insere(modify)
                limpatela()
                print(
                    f"\nINFO: O documento '{doc_modify.data}' foi modificado para '{modify}'!"
                )

                return

    def search_node(self, key):
        key_searched = NodeTree(key)

        node = self.root
        while node:
            if node == key_searched:
                return True
            else:
                if key_searched.data < node.data:
                    node = node.left
                else:
                    node = node.right
        else:
            return False

    def delete(self, key):
        def delete_rec(root, key):
            if root is None:
                return root

            if key < root.data:
                root.left = delete_rec(root.left, key)
            elif key > root.data:
                root.right = delete_rec(root.right, key)
            else:
                if root.left is None:
                    return root.right
                elif root.right is None:
                    return root.left

                root.data = self.minValue(root.right)
                root.right = delete_rec(root.right, root.data)

            return root

        self.root = delete_rec(self.root, key)

    def minValue(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.data

    def print_tree(self, node=None, level=0, prefix="Raiz: "):
        if node is None:
            node = self.root

        if node is not None:
            print(" " * 4 * level + prefix + str(node.data))
            if node.left or node.right:
                if node.left:
                    self.print_tree(node.left, level + 1, "Esquerda--- ")
                else:
                    print(" " * 4 * (level + 1) + "Esquerda--- Vazio")
                if node.right:
                    self.print_tree(node.right, level + 1, "Direita--- ")
                else:
                    print(" " * 4 * (level + 1) + "Direita--- Vazio")

    def display_documents(self):
        root = self.root

        def em_ordem(self, raiz):
            if not raiz:
                return

            # Visita filho da esquerda.
            em_ordem(self, raiz.left)

            # Visita nodo corrente.
            print(raiz.data)

            # Visita filho da direita.
            em_ordem(self, raiz.right)

        em_ordem(self, root)


def limpatela():
    os.system("clear" if os.name == "posix" else "cls")


def limpatela_menu():
    input("\nPressione ENTER para continuar... ")
    limpatela()


def main_menu():
    tree = BinaryTree()

    while True:
        print("\n--- Menu Principal do Sistema de Documentos ---")
        print("1. Inserir documento")
        print("2. Modificar documento")
        print("3. Procurar documento")
        print("4. Remover documento")
        print("5. Exibir árvore")
        print("6. Listar documentos")
        print("7. Sair")

        choice = input("Escolha uma opção: ")

        if choice == "1":
            limpatela()
            data = input("Insira o valor do documento: ")
            tree.insere(str(data))
            limpatela_menu()
        elif choice == "2":
            limpatela()
            key = input("Insira o valor do documento a ser modificado: ")
            modify = input("Insira o novo valor do documento: ")
            tree.modify_document(str(key), str(modify))
            limpatela_menu()
        elif choice == "3":
            limpatela()
            key = input("Insira o valor do documento a procurar: ")
            if tree.search_node(key):
                print(f"\nINFO: O documento {key} foi encontrado no sistema!")
            else:
                print(f"\nINFO: O documento {key} não foi encontrado no sistema!")
            limpatela_menu()
        elif choice == "4":
            limpatela()
            key = input("Insira o valor do documento a remover: ")
            if tree.search_node(key):
                tree.delete(str(key))
                print(f"\nINFO: O documento {key} foi removido do sistema!")
            else:
                print(f"\nINFO: O documento {key} não foi encontrado no sistema!")
            limpatela_menu()
        elif choice == "5":
            limpatela()
            print("Documentos Mostrado Em Forma de Árvore.\n")
            tree.print_tree()
            limpatela_menu()
        elif choice == "6":
            limpatela()
            print("Documentos Listados Por Ordem Alfabetica.\n")
            tree.display_documents()
            limpatela_menu()
        elif choice == "7":
            print("INFO: Saindo do programa...")
            limpatela_menu()
            break
        else:
            limpatela()
            print("INFO: Opção inválida. Por favor, tente novamente.")
            limpatela_menu()


if __name__ == "__main__":
    main_menu()

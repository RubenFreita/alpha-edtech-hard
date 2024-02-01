from collections import deque


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
            return

        node = self.root
        while node:
            if new_node.data < node.data:
                if node.left == None:
                    node.left = new_node
                    return
                node = node.left
            elif new_node.data > node.data:
                if node.right == None:
                    node.right = new_node
                    return
                node = node.right
            else:
                print(
                    f"O nó {new_node.data} já existe na arvore e não pode ser adicionado!"
                )
                return

    def search_node(self, key):
        key_searched = NodeTree(key)

        node = self.root
        while node:
            if node == key_searched:
                print(f"\nValor {key} encontrado")
                return True
            else:
                if key_searched.data < node.data:
                    node = node.left
                else:
                    node = node.right
        else:
            print("Valor não encontrado!")
            return False

    # def delete(self, value):
    #     node_remove = NodeTree(value)
    #     node = self.root
    #     node_prev = self.root
    #     while node:
    #         if node.data == node_remove.data:
    #             # caso 1: O nó não tem filhos
    #             if node.left == None and node.right == None:
    #                 if node.data < node_prev.data:
    #                     node_prev.left = None
    #                 elif node.data > node_prev.data:
    #                     node_prev.right = None
    #                 del node
    #                 return
    #             # O nó tem apenas um filho
    #             elif node.left == None or node.right == None:
    #                 if node.left != None and node.right == None:
    #                     if node.data < node_prev.data:
    #                         node_prev.left = node.left
    #                     elif node.data > node_prev.data:
    #                         node_prev.right = node.left
    #                 elif node.left == None and node.right != None:
    #                     if node.data < node_prev.data:
    #                         node_prev.left = node.right
    #                     elif node.data > node_prev.data:
    #                         node_prev.right = node.right
    #                 del node
    #                 return
    #             # print(node.data)
    #             # print(node.left)
    #             # print(node.right.data)
    #             return
    #         elif node_remove.data < node.data:
    #             node_prev = node
    #             node = node.left
    #         else:
    #             node_prev = node
    #             node = node.right
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

    def display_tree(self):
        root = self.root

        def em_ordem(self, raiz):
            if not raiz:
                return

            # Visita filho da esquerda.
            em_ordem(self, raiz.left)

            # Visita nodo corrente.
            print(raiz.data)
            # if raiz.left != None:
            #     print(f"no - {raiz.data} -> esquerdo: {raiz.left.data}")
            # if raiz.right != None:
            #     print(f"no - {raiz.data} -> right: {raiz.right.data}")

            # Visita filho da direita.
            em_ordem(self, raiz.right)

        em_ordem(self, root)


tree = BinaryTree()
nodes = [4, 2, 3, 5, 1, 6, 9, 7, 8]
docs = ["Documentos", "Musicas", "Videos", "Livros", "Imagens"]
for i in docs:
    tree.insere(i)


# result = tree.search_node(10)
print()
tree.display_tree()
tree.print_tree()
print()
# tree.delete(4)
# tree.print_tree()
# print()
# tree.delete(1)
# tree.print_tree()

# tree.print_tree()

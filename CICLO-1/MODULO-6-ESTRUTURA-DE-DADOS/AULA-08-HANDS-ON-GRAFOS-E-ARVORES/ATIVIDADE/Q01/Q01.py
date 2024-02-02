class Comentario:
    def __init__(self, conteudo, curtida, apoio, riso, raiva) -> None:
        self.conteudo = conteudo
        self.curtida = curtida
        self.apoio = apoio
        self.riso = riso
        self.raiva = raiva

    def aumentar_curtida(self, qtd):
        self.curtida += qtd

    def aumentar_apoio(self, qtd):
        self.apoio += qtd

    def aumentar_riso(self, qtd):
        self.riso += qtd

    def aumentar_raiva(self, qtd):
        self.raiva += qtd


class NodeCometario:
    def __init__(self, comentario: Comentario) -> None:
        self.comentario = comentario
        self.right = None
        self.left = None


class ComentarioTree:
    def __init__(self) -> None:
        self.root = None
        self.option = 1

    def insert(self, comentario: Comentario):
        new_comentario = NodeCometario(comentario)
        if self.root == None:
            self.root = new_comentario
            return

        node = self.root
        if self.option == 1:
            while node:
                if new_comentario.comentario.curtida < node.comentario.curtida:
                    if node.left == None:
                        node.left = new_comentario
                        return
                    node = node.left
                elif new_comentario.comentario.curtida > node.comentario.curtida:
                    if node.right == None:
                        node.right = new_comentario
                        return
                    node = node.right
                else:
                    pass

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

    def insert(self, key):
        pass

class Pai(object):
    def __init__(self, peso, altura):
        self.peso = peso
        self.altura = altura


class Filha(Pai):
    def __init__(self, peso, altura, cabelo):
        super().__init__(peso, altura)
        self.cabelo = cabelo

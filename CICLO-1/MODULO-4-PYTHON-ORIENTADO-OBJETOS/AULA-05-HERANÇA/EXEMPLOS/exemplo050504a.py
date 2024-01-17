class Pai(object):
    def __init__(self, nomePai):
        self.nome = nomePai
        print('Construindo a classe Pai')

    def __str__(self):
        return f"Pai:= {self.nome};"


class Filha(Pai):
    def __init__(self, nomeFilha, nomePai):
        self.nomeFilha = nomeFilha
        super(Filha, self).__init__(nomePai)

    def __str__(self):
        return f"Pai:= {self.nome}; Filha: {self.nomeFilha};"


pmarcotti = Pai("Paulo Marcotti")
print(pmarcotti)

angela = Filha("Angela G Marcotti", pmarcotti.nome)
print(angela)

class Estudante:
    def __init__(self, nome):
        self._nome = nome

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novonome):
        self._nome = novonome


asp = Estudante("Andre")
print(asp.nome)

asp.nome = 'Pereira'
print(asp.nome)

asp._nome = "Limoeiro"
print(asp._nome)

class Funcionario:
    def __init__(self, id: int, nome: str) -> None:
        self.id = id
        self._nome = nome


x = Funcionario(1, "Paulo Marcotti")
print(x.id)
print(x._nome)

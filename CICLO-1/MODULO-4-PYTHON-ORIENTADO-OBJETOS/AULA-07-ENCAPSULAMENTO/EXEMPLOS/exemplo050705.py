class Funcionario:
    def __init__(self, id: int, nome: str) -> None:
        self.id = id
        self.__nome = nome


x = Funcionario(1, "Paulo Marcotti")
print(x.id)
# Forma menos convencional
print(x._Funcionario__nome)
# "Funcionario" has no attribute "_Funcionario__nome" [attr-defined]

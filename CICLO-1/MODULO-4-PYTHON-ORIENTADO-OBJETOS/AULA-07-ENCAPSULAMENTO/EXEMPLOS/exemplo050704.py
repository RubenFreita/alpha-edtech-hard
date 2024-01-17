class Funcionario:
    def __init__(self, id:int, nome:str) -> None:
        self.id = id
        self._nome = nome


class Chefe(Funcionario):
    def mostrar_bonus(self) -> None:
        print(f"{self._nome} vari receber R$ 1000 de bônus!")


x = Funcionario(1, "Paulo Marcotti")
print(x.id)
print(x._nome) # acessado protected!!!

y = Chefe(2, "Kenji Taniguchi")
y.mostrar_bonus()

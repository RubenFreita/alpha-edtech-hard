from typing import NoReturn

class Funcionario:
    def __init__(self, id:int, nome:str) -> None:
        self.id = id
        self.__nome = nome

    @property
    def nome(self) -> str:
        return self.__nome

    # @nome.getter
    # def nome(self) -> NoReturn:
    #     raise Exception("Nao pode acessar o nome!")
    
    
    
   



x = Funcionario(1, "Paulo Marcotti")
print(x.id)
# Forma menos convencional
# print(x.__nome)
# Exception: Não pode acessar o nome!
print(x.nome)

from abc import ABCMeta, abstractmethod


class Funcionario(metaclass=ABCMeta):
    @abstractmethod
    def cargo(self) -> str:
        pass


class Chefe(Funcionario):
    def cargo(self) -> str:
        return "chefe da galera"


class Dono(Funcionario):
    def cargo(self) -> str:
        return "dono"


def mostrar_cargo(funcionario: Funcionario) -> None:
    cargo = funcionario.cargo()
    mensagem = f"Nivel Hierarquico: {cargo}"
    print(mensagem)


pessoa1 = Chefe()
pessoa2 = Dono()
mostrar_cargo(pessoa1)
mostrar_cargo(pessoa2)

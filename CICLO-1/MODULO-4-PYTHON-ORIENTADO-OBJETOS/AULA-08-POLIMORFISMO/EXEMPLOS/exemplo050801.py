class Funcionario:
    def cargo(self) -> str:
        return "apenas funcionario"

class Chefe(Funcionario):
    def cargo(self) -> str:
        return "boss de alguem"

class Dono(Funcionario):
    def cargo(self) -> str:
        return "dono da bagassa"

def mostrar_cargo(funcionario: Funcionario) -> None:
    cargo = funcionario.cargo()
    mensagem = f"Nivel Hierarquico: {cargo}"
    print(mensagem)

pessoa1 = Funcionario()
pessoa2 = Chefe()
pessoa3 = Dono()
mostrar_cargo(pessoa1)
mostrar_cargo(pessoa2)
mostrar_cargo(pessoa3)
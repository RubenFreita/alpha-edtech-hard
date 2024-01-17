from dataclasses import dataclass


@dataclass
class Usuario:
    id: int
    nome: str


@dataclass
class Admin(Usuario):
    nivel: int


@dataclass
class UsuarioExterno(Usuario):
    fonte: str


def mostra_usuario(u: Usuario) -> None:
    print("+-------------------+")
    print("| Dados do usuario: ")
    print(f"| id: {u.id}; ")
    print(f"| nome: {u.nome}; ")
    print("+-------------------+")


usuario1 = Admin(1, "Gabriel", 3)
usuario2 = UsuarioExterno(2, "Maria", "Google")

mostra_usuario(usuario1)
mostra_usuario(usuario2)

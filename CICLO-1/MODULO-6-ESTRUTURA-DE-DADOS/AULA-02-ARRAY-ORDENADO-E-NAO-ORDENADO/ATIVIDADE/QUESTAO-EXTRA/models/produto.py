class Produto():
    id = 0
    def __init__(self, nome: str, valor: float) -> None:
        self.nome = nome
        self.valor = valor
        self.id = Produto.id
        Produto.id += 1

    def __str__(self) -> str:
        return self.nome
    
    def __eq__(self, __value: object) -> bool:
        if isinstance(__value, Produto) and self.nome == __value.nome:
            return True
        else:
            return False
class Produto:
    nome: str
    valor: float
    valor_total: float

    def __init__(self, nome: str, valor: float):
        self.nome = nome
        self.valor = valor
        self.valor_total = 0

    def atualiza_valor_total(self, quantidade: int):
        self.valor_total = self.valor * quantidade
    

feijao = Produto("Arroz", 3.15)
feijao.atualiza_valor_total(4)
print(feijao.valor_total)
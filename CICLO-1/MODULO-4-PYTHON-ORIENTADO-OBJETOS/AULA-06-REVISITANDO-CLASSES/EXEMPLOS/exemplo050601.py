class Paralelepipedo:
    def __init__(self, larg, compr, prof):
        self.largura = larg
        self.comprimento = compr
        self.profundidade = prof

    # Implementar método construtor alternativo com decorator
    @classmethod
    def cubo(cls, x=1.0):
        # inicializar um Paralelepipedo com __init__ e os valores x, x, x
        # criando assim um cubo de lado x
        return cls(x, x, x)

    def multiplicar(self, fator=100.0):
        self.largura *= (1.0+fator/100.0)
        self.comprimento *= (1.0+fator/100.0)
        self.profundidade *= (1.0+fator/100.0)
        self.largura = round(self.largura, 2)
        self.comprimento = round(self.comprimento, 2)
        self.profundidade = round(self.profundidade, 2)

    # Implementar método imprimir
    def __str__(self) -> str:
        return f"forma= {self.largura} x {self.comprimento} x {self.profundidade}"


tijolo = Paralelepipedo(0.15, 0.25, 0.10)
print("tijolo: ", tijolo)
# bloco = tijolo.multiplicar(50)
# print("bloco: ", bloco)
tijolo.multiplicar(50.0)
print("bloco: ", tijolo)

cubinho = Paralelepipedo.cubo(2.5)
print("cubinho: ", cubinho)

cubao = cubinho
cubao.multiplicar(200.0)
print("cubao: ", cubao)

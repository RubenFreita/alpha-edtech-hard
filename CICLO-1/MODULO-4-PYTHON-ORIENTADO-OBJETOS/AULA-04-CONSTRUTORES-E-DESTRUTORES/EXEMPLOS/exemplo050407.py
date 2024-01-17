class Paralelepipedo:
    largura: float = 10
    comprimento: float = 10
    profundidade: float = 10

    # Implementar método construtor
    def __init__(self, largura, comprimento, profundidade):
        self.largura = largura
        self.comprimento = comprimento
        self.profundidade = profundidade

    # Implementar método construtor alternativo com decorator
    @classmethod
    def cubo(cls, x=1.0):
        # inicializar um Paralelepipedo com __init__ e os valores x, x, x
        # criando assim um cubo de lado x
        return cls(x, x, x)

    # Implementar método construtor alternativo com decorator
    @classmethod
    def placa(cls, x=1.0, profundidade=1.0):
        # criando uma placa de lado x e profundidade 
        return cls(x, x, profundidade)

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

plaquinha = Paralelepipedo.placa(10.0, 1.5)
print("plaquinha: ", plaquinha)



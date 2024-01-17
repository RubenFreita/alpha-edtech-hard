class Paralelepipedo:
    qtdParalelepipedo = 0 # Atributo da Classe e não de cada objeto

    def __init__(self, largura: float = 0.15, comprimento: float = 0.25, profundidade: float = 0.10):
        self.largura = largura # Atributo de Instância
        self.comprimento = comprimento
        self.profundidade = profundidade
        Paralelepipedo.qtdParalelepipedo += 1

    def __del__(self):
        # del self
        Paralelepipedo.qtdParalelepipedo -= 1


tijolo1 = Paralelepipedo(0.15, 0.25, 0.10)
tijolo2 = Paralelepipedo(0.35, 0.45, 0.20)

tijolo1.__del__()
print("Quantidade: ", Paralelepipedo.qtdParalelepipedo)

print(tijolo1.__dict__)
print(tijolo2.__dict__)

print(tijolo1)
print(type(tijolo1))

# tijolo1.__delattr__

# print(tijolo1.__dict__)
# print(tijolo1)
# print(type(tijolo1))

# del tijolo1

# print(tijolo1.__dict__)
# print(tijolo1)
# print(type(tijolo1))

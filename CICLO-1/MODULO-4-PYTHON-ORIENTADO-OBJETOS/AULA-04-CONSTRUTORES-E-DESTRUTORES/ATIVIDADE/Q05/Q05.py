
class Triangulo:
    def __init__(self, lado1, lado2, lado3) -> None:
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.perimetro = lado1 + lado2 + lado3

    @classmethod
    def isoceles(cls, lados_iguais, lado_diferente):
        return cls(lados_iguais, lados_iguais, lado_diferente)
    
    @classmethod
    def equilatero(cls, lado):
        return cls.isoceles(lado, lado)

if __name__ == "__main__":

    triangulo_normal = Triangulo(1, 2, 3)
    print(triangulo_normal.perimetro)

    triangulo_isoceles = Triangulo.isoceles(2, 4)
    print(triangulo_isoceles.perimetro)

    triangulo_equilatero = Triangulo.equilatero(3)
    print(triangulo_equilatero.perimetro)
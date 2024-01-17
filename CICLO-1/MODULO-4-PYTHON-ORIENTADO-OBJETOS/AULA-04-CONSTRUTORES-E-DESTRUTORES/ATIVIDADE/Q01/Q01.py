
class Calculadora:
    def __init__(self, **numeros) -> None:
        for atr, numero in numeros.items():
            setattr(self, atr, numero)

    def soma(self):
        return sum(self.__dict__.values())
    
    def produto(self):
        resultado = 1
        for i in self.__dict__.values():
            resultado *= i
        return resultado



if __name__ == '__main__':
    calculadora = Calculadora(n1=1, n2=2, n3=3, n4=10)
    print(calculadora.__dict__)
    print(calculadora.soma())
    print(calculadora.produto())

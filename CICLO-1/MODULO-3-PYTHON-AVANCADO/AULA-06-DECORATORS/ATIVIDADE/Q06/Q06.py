
def quadrado(entrada: str) -> int:
    try:
        return int(entrada)**2
    except ValueError:
        print("A entrada não pode ser convertido para o tipo int.")
    finally:
        print("Fim da execução do programa!")


print(quadrado("4"))
print(quadrado("e"))
print(quadrado("0"))
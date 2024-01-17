
class NotaFiscal:
    def __init__(self, nome_arquivo: str) -> None:
        self.arquivo = open(nome_arquivo + ".txt", "w")
    
    def __enter__(self):
        print("Criando arquivo...")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Saindo do arquivo...")

if __name__ == "__main__":

    with NotaFiscal("compras") as nota_fiscal:
        nota_fiscal.arquivo.write("comprando arroz...")


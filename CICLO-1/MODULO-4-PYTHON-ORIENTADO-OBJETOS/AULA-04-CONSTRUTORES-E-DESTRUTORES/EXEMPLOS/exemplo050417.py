class ConstrutorDinamico:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)


# Criando uma instância com atributos dinâmicos
objeto1 = ConstrutorDinamico(nome="Luis Carlos", idade=25, cidade="Redenção")

# Exibindo os atributos
print("Objeto 1:")
print("Nome:", objeto1.nome)
print("Idade:", objeto1.idade)
print("Cidade:", objeto1.cidade)

# Adicionando mais atributos dinamicamente
objeto1.profissao = "Arquiteto de Software"

# Exibindo novamente os atributos
print("\nObjeto 1 após adicionar a profissão:")
print("Nome:", objeto1.nome)
print("Idade:", objeto1.idade)
print("Cidade:", objeto1.cidade)
print("Profissão:", objeto1.profissao)

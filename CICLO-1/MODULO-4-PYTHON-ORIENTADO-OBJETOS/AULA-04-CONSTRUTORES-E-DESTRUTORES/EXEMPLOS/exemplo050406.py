class MinhaClasse:
    def __init__(self, atributo1, atributo2):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    @classmethod
    def construtor_alternativo(cls, parametro):
        # Lógica do construtor alternativo
        # Pode retornar uma instância da classe
        # com base nos parâmetros fornecidos
        # ... chamou o construtor __init__ criando um novo objeto
        return cls("Valor Padrão", parametro)


# Uso do construtor padrão
objeto1 = MinhaClasse("valorAtributo1", "valorAtributo2")
print("objeto1:=", objeto1)
print(type(objeto1))
print("objeto1.atributo1:=", objeto1.atributo1)
print("objeto1.atributo1:=", objeto1.atributo2)

# Uso do construtor alternativo
objeto2 = MinhaClasse.construtor_alternativo("Novo Valor")
print("objeto2:=", objeto2)
print(type(objeto2))
print("objeto2.atributo1:=", objeto2.atributo1)
print(type(objeto2.atributo1))
print("objeto2.atributo2:=", objeto2.atributo2)
print(type(objeto2.atributo2))

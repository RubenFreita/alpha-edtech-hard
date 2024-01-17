class MinhaClasse:
    id: str = "ST"

    def __init__(self, atributo1, atributo2):
        self.id = MinhaClasse.id
        MinhaClasse.id += "IN"
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    @classmethod
    def construtor_alternativo(cls, parametro):
        # chama o construtor __init__ criando o novo objeto
        return cls("CA", parametro)


# Uso do construtor padrão
objeto1 = MinhaClasse("P1", "V1")
print("objeto1.atributo1:=", objeto1.atributo1)
print("objeto1.atributo1:=", objeto1.atributo2)

print("objeto1.id:=", objeto1.id)

# Uso do construtor alternativo
objeto2 = MinhaClasse.construtor_alternativo("V2")
print("objeto2.atributo1:=", objeto2.atributo1)
print("objeto2.atributo2:=", objeto2.atributo2)

print("objeto2.id:=", objeto2.id)

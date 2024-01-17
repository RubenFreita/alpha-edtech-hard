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

    @classmethod
    def construtor_alternativo(cls, parametro, param3):
        # chama o construtor __init__ criando o novo objeto
        # agora declarado o mesmo metodo com outra assinatura
        if param3 >= "M":
            return cls("CA", parametro)
        else:
            return cls("CA", param3)


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

# Uso do construtor alternativo com outra assinatura
objeto3 = MinhaClasse.construtor_alternativo("V3", "X1")
print("objeto3.atributo1:=", objeto3.atributo1)
print("objeto3.atributo2:=", objeto3.atributo2)
print("objeto3.id:=", objeto3.id)

# Uso do construtor alternativo com outra assinatura
objeto4 = MinhaClasse.construtor_alternativo("V4", "D1")
print("objeto4.atributo1:=", objeto4.atributo1)
print("objeto4.atributo2:=", objeto4.atributo2)
print("objeto4.id:=", objeto4.id)

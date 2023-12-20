class CustomObject:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

    def __hash__(self):
        # Combine os hashes dos atributos relevantes
        return hash((self.attribute1, self.attribute2))

    def __eq__(self, other):
        # Verifique a igualdade dos atributos relevantes
        return (isinstance(other, CustomObject) and
                self.attribute1 == other.attribute1 and
                self.attribute2 == other.attribute2)

# Exemplo de uso:
objeto1 = CustomObject(10, "abc")
objeto3 = CustomObject(10, "abc") #objeto igual ao objeto1
objeto2 = CustomObject(20, "def")

# Criação de um dicionário usando objetos CustomObject como chaves
dicionario = {objeto1: "Valor 1", objeto2: "Valor 2"}
print(objeto1.__hash__())
print(objeto3.__hash__())
print(objeto1==objeto3) #verifica igualdade dos objetos 1 e 3

# Acesse os valores usando as chaves customizadas
print(dicionario[objeto1])  # Saída: Valor 1
print(dicionario[objeto2])  # Saída: Valor 2


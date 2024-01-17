class Estudante:
    __escolaNome = 'Alpha Instituto'  # Estudanteprivate class attribute

    def __init__(self, nome, idade):
        self.__nome = nome  # private instance attribute
        self.__idade = idade  # private instance attribute

    def __display(self):  # private method
        print('Este eh um metodo private.')


asp = Estudante("Andre", 25)
print(asp._Estudante__nome)

asp._Estudante__nome = 'Pereira'
print(asp._Estudante__nome)
asp._Estudante__display()

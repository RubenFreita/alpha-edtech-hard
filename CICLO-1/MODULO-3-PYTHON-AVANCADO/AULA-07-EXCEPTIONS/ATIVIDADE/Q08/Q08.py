

class IdadeInvalidaError(ValueError):

    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)

def valida_idade(idade):
    if 0 <= idade <=130:
        print("Idade Válida!")
    else:
        raise IdadeInvalidaError("A idade não é válida!")
    
    
for i in [50, 150, -1]:
    try:
        valida_idade(i)
    except IdadeInvalidaError as i:
        print(i)
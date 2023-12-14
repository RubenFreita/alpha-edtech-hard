from typing import Callable

def cria_formatacao(formatacao: str) -> Callable[[str], str]:
    string = "Hello World!!"
    def aplica_formatacao() -> str:
        return formatacao + string + formatacao
    return aplica_formatacao()

formatacao1 = cria_formatacao("@@@@@@@")
print(formatacao1)

print()
formatacao2 = cria_formatacao(">>>>>>>")
print(formatacao2)
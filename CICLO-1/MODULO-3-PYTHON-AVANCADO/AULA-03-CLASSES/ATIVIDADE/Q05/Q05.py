from typing import Optional

def apresentacao(nome: Optional[str] = None) -> str:
    if nome:
        return f"Bem-vindo, {nome}!"
    else:
        return "Bem-vindo, visitante!"

# Chamada da função com diferentes valores
mensagem_1 = apresentacao("João")
mensagem_2 = apresentacao()

print(mensagem_1)
print(mensagem_2)
import re


class SenhaFracaError(Exception):

    def __init__(self, mensagem="A senha não está segura!") -> None:
        self.mensagem = mensagem
        super().__init__(self.mensagem)

def valida_senha(senha: str):
    especiais = re.compile('[^A-Za-z0-9]+')
    mauisculas = re.compile(r'[A-Z]')
    if len(senha) >= 8 and especiais.search(senha) and mauisculas.search(senha):
        print("Senha Forte!")
    else:
        raise SenhaFracaError




senhas = ["Alpha", "Alpha@", "Alpha%23"]
for i in senhas:
    try:
        valida_senha(i)
    except SenhaFracaError as senha:
        print(senha)
    finally:
        print("Fim da iteração!")

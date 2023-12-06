


entrada = input("Digite o seu nome completo: ").split()
ultimoSobrenome = entrada[-1][0].upper() + entrada[-1][1:-1].lower() + entrada[-1][-1].lower()
ultimoSobrenome += ", "
abreviacoes = ""
for palavra in entrada[0:-1]:
    abreviacoes += palavra[0].upper() + ". "


nomeFormatado = ultimoSobrenome + abreviacoes
print(nomeFormatado)
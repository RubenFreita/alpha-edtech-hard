

nomeUsuario = input("Digite o seu nome de usuário: ")
senha = input("Digite a sua senha: ")
count = 1
while nomeUsuario == senha:
    print("Digite a senha diferente do nome de usuário!")
    print(f"Você só tem mais {3 - count} tentativas!")
    nomeUsuario = input("Digite o seu nome de usuário novamente: ")
    senha = input("Digite a sua senha novamente: ")
    count+=1
    if(count == 3):
        print("Você ultrapassou o total de tentativas!")
        break
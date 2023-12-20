import os

try:
    with open("naoexiste.txt", "r") as arquivonaoexiste:
        arquivonaoexiste.read()
except FileNotFoundError as e:
    print("O Arquivo Não existe")
    print(f"Erro capturado: {e}")


try:
    os.chdir(r'C:\\Program Files\\windowsApps')
except PermissionError as p:
    print("Você não tem permissão para cessar a pasta desejada!")
    print(p)
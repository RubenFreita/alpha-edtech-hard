

def leitura_arquivo(nome_arquivo: str):
    try:
        try:
            with open(nome_arquivo, "r") as arquivo:
                leitura = arquivo.read()
            
        except FileNotFoundError:
            print(f"O arquivo \"{nome_arquivo}\" não existe!")
            return "Leitura indisponível"
        except PermissionError:
            print(f"Você não tem permissão para ler este arquivo!")
            return "Leitura indisponível"
        else:
            return leitura
    except Exception as e:
        print('Outras exceções de leitura do arquivo!')
        print(e)
        return "Problema na leitura do arquivo!"

#arquivo foi criado e retirado todas as permissões para dar erro de permissão
leitura1 = leitura_arquivo("teste.txt")
print(leitura1)
leitura2 = leitura_arquivo("test.txt")
print(leitura2)


# comando para retirar as permissões de um arquivo no windows.
# icacls "caminho do arquivo" /inheritance:r /remove "*S-1-1-0"

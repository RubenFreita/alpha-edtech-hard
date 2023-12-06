

quantidade_valores = int(input("Informe a quantidade de valores a serem armazanados: "))

conjunto_dados = [] 
for i in range(quantidade_valores):
    conjunto_dados.append(int(input(f"Informe o valor {i} a ser armazenado: ")))    
conjunto_dados_str = []
for i in conjunto_dados:
    conjunto_dados_str.append(str(i))
with open("ConjuntoDeDadosQ01.txt","w") as arquivo_financeiro:
    arquivo_financeiro.write(", ".join(conjunto_dados_str))



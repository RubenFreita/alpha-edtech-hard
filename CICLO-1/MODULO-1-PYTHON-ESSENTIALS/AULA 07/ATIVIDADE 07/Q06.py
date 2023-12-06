

entrada = input("Informe uma frase: ")
tamInicial = len(entrada)
for i in range(len(entrada)):
    entrada += entrada[(len(entrada ) -1) - i*2]
entrada = entrada[tamInicial:len(entrada)]
print(entrada)
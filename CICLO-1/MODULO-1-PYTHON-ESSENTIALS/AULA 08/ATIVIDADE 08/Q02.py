

with open("ConjuntoDeDadosQ01.txt","r") as arquivo_financeiro: #abrindo arquivo txt em modo de leitura
    conjunto_dados = arquivo_financeiro.read().split(",") # lendo o arquivo txt em atribuindo em um array
soma = 0
media = 0
qtd_valores_validos = 0 # quantidade de valores que são maiores que 0
for valor in conjunto_dados:
    if int(valor) > 0: #verificação para somar apenas os números válidos
        qtd_valores_validos +=1 # atribuindo 1 ao contador de números válidos
        soma += int(valor) 
        #verificação para encontrar o maior dentre os valores válidos do array
        #primeiro o if verifica se a variável maior já foi instânciada se não tiver
        #ela será criada e atribuida o primeiro valor do array
        #após a primeira verificação a primeira parte do sempre será falsa então restará verificar apenas a segunda
        #que é a verificação de maior valor, se for vdd a variável maior será atualidada
        if 'maior' not in vars() or int(valor) > maior:
            maior = int(valor)
        if 'menor' not in vars() or int(valor) < menor: #mesma lógica que o if para achar o maior valor
            menor = int(valor)
#a media será a soma dos valores válidos dividida pela qtd de valores válidos
media = round(soma / qtd_valores_validos)
#for para varrer o array e substituir os valores inválidos pela média dos valores válidos
for i in range(len(conjunto_dados)):
    if int(conjunto_dados[i]) <= 0:
        conjunto_dados[i] = str(media)
    
print(f"A média é: {media}")
print(f"O valor mínimo é: {menor}")
print(f"O valor máximo é: {maior}")
print(f"Os 5 primeiros valores são: {conjunto_dados[:5]}")
print(f"Os 5 últimos valores são: {conjunto_dados[-5:]}")

#abrindo/criando um arquivo em modo de escrita e adicionando
# o array alterado somente com números válidos
with open("ConjuntoDeDadosQ02.txt", "w") as arquivo_final:
    arquivo_final.write(", ".join(conjunto_dados))#passando o array concatenado como str e separado por ","

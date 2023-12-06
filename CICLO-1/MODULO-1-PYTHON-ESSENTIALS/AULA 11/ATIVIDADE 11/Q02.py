#array de produtos
produtos = []
#abertura de um arquivo txt em modo de leitura que tem 
# armazenado uma lista de produtos e as suas descrições
with open("produtosQ02.txt", "r", encoding="utf-8") as arquivo:
    #adicionando a lista e separando por ponto e vírgula
    produtos = arquivo.read().split("; ") 
    

print(f"\t  Produtos Cadastrados")
print(f"Produto: (Nome, Código, Qtd, Preço)")
contador = 0
#for para mostrar todos os produtos da lista produtos
for produto in produtos:
    contador += 1
    print(f"Produto {contador}: ({produto})")


#dicionário com um dicionário interno como valor
informacoes_pessoais = {"nome": "augusto",
                        "idade": 26,
                        "profissao": "dev",
                        "filme_favorito": "interestelar",
                        "familiares": {
                            "pai": "jose",
                            "mae": "maria",
                            "avo": "sebastiao"
                        }}
nome_pai = informacoes_pessoais["familiares"]["pai"]
nome_mae = informacoes_pessoais["familiares"]["mae"]

print(f"Nome do pai: {nome_pai}")
print(f"Nome do mãe: {nome_mae}")
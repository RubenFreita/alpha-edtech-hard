"""
Não é possível ter chaves duplicadas em um dicionário em python.
Quando se tenta criar duas chaves iguais ele sobescreve a primeira 
adicionada, como é mostrado no código abaixo.
"""

informacoes_pessoais = {"nome": "augusto",
                        "idade": 26,
                        "profissao": "dev",
                        "filme_favorito": "interestelar",
                        "familiares": { #será sobrescrito
                            "pai": "jose",
                            "mae": "maria",
                            "avo": "sebastiao"
                        },
                        "familiares": "nao tem", #irá sobrescrever
                        }
print(informacoes_pessoais)

obj1 = {
    "Nome": "Paulo", 
    "Gerente": "Samir",
    "Cargo": "Instrutor", 
    "Idade": 66, 
    "Altura": 1.71, 
    "Trabalho": "Remoto"
}
print(obj1)

#Idade
anosVida = obj1.get("Idade")
print(anosVida)
print()

#Lista de Itens de um Dicionário
itens = obj1.items()
print(itens)
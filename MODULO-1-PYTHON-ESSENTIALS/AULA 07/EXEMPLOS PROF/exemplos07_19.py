
obj1 = {
    "Nome": "Paulo", 
    "Gerente": "Samir",
    "Cargo": "Instrutor", 
    "Idade": 66, 
    "Altura": 1.71, 
    "Trabalho": "Remoto"
}
print(obj1)

dict_values = obj1.values()
print(dict_values)
print()

#
obj1.update({"Altura": 1.69})
print(obj1)
print()

#
#obj2 = obj1.copy()
#print(obj2)

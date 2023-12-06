
cores_primarias = set(["amarelou", "vermelhou", "azulou", "medrou","burrou" ])
cores_2 = set()
cores_3 = set()
cores_4 = set()
uniao_todas = set()
respostas_usuario = set()
contador = 0

for cor1 in cores_primarias:
    for cor2 in cores_primarias:
        if cor1 > cor2:
            contador += 1
            respostas_usuario.add(input(f"Qual a mistura das cores {cor1} e {cor2}? "))
            cores_2.add(cor1+cor2)

uniao_todas = cores_primarias.union(cores_2)

for cor1 in uniao_todas:
    for cor2 in uniao_todas:
        for cor3 in uniao_todas:
            if cor1 > cor2 > cor3:
                contador += 1
                respostas_usuario.add(input(f"Qual a mistura das cores {cor1}, {cor2} e {cor3}? "))
                cores_3.add(cor1+cor2+cor3)


for cor1 in uniao_todas:
    for cor2 in uniao_todas:
        for cor3 in uniao_todas:
            for cor4 in uniao_todas:
                if cor1 > cor2 > cor3 > cor4:
                    contador += 1
                    respostas_usuario.add(input(f"Qual a mistura das cores {cor1}, {cor2}, {cor3} e {cor4}? "))
                    cores_4.add(cor1+cor2+cor3+cor4)

uniao_todas = uniao_todas.union(cores_3)
uniao_todas = uniao_todas.union(cores_4)

# with open("saidaQ02.txt", "w") as arquivo:
#     arquivo.write(str(uniao_todas))
print(uniao_todas)
# print(contador)

if uniao_todas <= respostas_usuario:
    print("Respostas corretas!")
else:
    print("Respostas inválidas!")
print(f"Resposta esperada: {uniao_todas}")
print("Respostas do usuário:")
print(respostas_usuario)


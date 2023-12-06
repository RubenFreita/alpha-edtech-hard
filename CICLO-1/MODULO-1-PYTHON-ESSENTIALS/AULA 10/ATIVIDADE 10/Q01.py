
cores_primarias = set(["amarelo", "azul", "vermelho"])
respostas_usuario = set()

for cor1 in cores_primarias:
    for cor2 in cores_primarias:
        if cor1 > cor2:
            respostas_usuario.add(input(f"Qual a mistura da cor {cor1} e a cor {cor2}? "))
respostas_usuario.add(input(f"Qual a mistura da cor vermelho, azul e amarelo? "))

if {"roxo", "verde", "laranja", "preto"} <= respostas_usuario:
    print("Respostas corretas!")
else:
    print("Respostas inválidas!")
print("Resposta esperada: roxo, verde, laranja, preto")
print("Resposta do usuário:")
print(respostas_usuario)
#Questão 07
print("Responda as perguntas abaixo com sim ou com não!!")
pergunta1 = input("Telefonou para a vítima? ")
pergunta2 = input("Esteve no local do crime? ")
pergunta3 = input("Mora perto da vítima? ")
pergunta4 = input("Devia para a vítima? ")
pergunta5 = input("Já trabalhou com a vítima? ")
contador = 0

if pergunta1.lower() == "sim":
    contador += 1
elif pergunta1.lower() != "nao" and pergunta1.lower() != "não":
    print("Responda as perguntas de forma correta.")
    print("O programa será encerrado, pois a pergunta 1 foi respondida incorretamente!")
    exit()
if pergunta2.lower() == "sim":
    contador += 1
elif pergunta2.lower() != "nao" and pergunta2.lower() != "não":
    print("Responda as perguntas de forma correta.")
    print("O programa será encerrado, pois a pergunta 2 foi respondida incorretamente!")
    exit()
if pergunta3.lower() == "sim":
    contador += 1
elif pergunta3.lower() != "nao" and pergunta3.lower() != "não":
    print("Responda as perguntas de forma correta.")
    print("O programa será encerrado, pois a pergunta 3 foi respondida incorretamente!")
    exit()
if pergunta4.lower() == "sim":
    contador += 1
elif pergunta4.lower() != "nao" and pergunta4.lower() != "não":
    print("Responda as perguntas de forma correta.")
    print("O programa será encerrado, pois a pergunta 4 foi respondida incorretamente!")
    exit()
if pergunta5.lower() == "sim":
    contador += 1
elif pergunta5.lower() != "nao" and pergunta5.lower() != "não":
    print("Responda as perguntas de forma correta.")
    print("O programa será encerrado, pois a pergunta 5 foi respondida incorretamente!")
    exit()

if contador == 2:
    print("Você é classificado como Suspeito!")
elif 3 <= contador <= 4: 
    print("Você é classificado como Cúmplice!")
elif contador == 5: 
    print("Você é classificado como Assassino!")
else:
    print("Você é classificado como Inocente!")

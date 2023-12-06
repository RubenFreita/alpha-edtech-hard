#Questão 02


nota1 = float(input("Informe a sua primeira nota: "))
nota2 = float(input("Informe a sua segunda nota: "))
nota3 = float(input("Informe a sua terceira nota: "))

media = round((nota1+nota2+nota3)/3, 2)
print(media)
if media < 7:
    print("Reprovado")
if(media == 10):
    print("Aprovado com Distinção")
elif media >= 7:
    print("Aprovado")

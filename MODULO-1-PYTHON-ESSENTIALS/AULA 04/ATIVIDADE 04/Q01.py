#Questão 01


data = input("Digite uma data no formato dd/mm/aaaa: ")

dia = data[0:2]
mes = data[3:5]
ano = data[6:11]

dataValida = False
#anor bissexto tem que ser divisivel por 4 e não divisivel por 100
#se for divisivel por 100 tem que ser divisivel por 400
if int(mes) == 2:
    if int(dia) == 29:
        if int(ano)%4 == 0 and int(ano)%100 != 0:
            dataValida = True
        elif int(ano)%100 == 0 and int(ano)%400==0:
            dataValida = True
    else:
        if 1 <= int(dia) <= 28:
            dataValida = True
else:
    if 1 <= int(mes) <= 7:
        if int(mes)%2==1 and 1 <= int(dia) <= 31:
            dataValida = True
        elif int(mes)%2==0 and 1 <= int(dia) <=30:
            dataValida = True
    if 8 <= int(mes) <= 12:
        if int(mes)%2==0 and 1 <= int(dia) <= 31:
            dataValida = True
        elif int(mes)%2==1 and 1 <= int(dia) <=30:
            dataValida = True

if dataValida:
    print(f"A data {dia}/{mes}/{ano} é válida")
else:
    print(f"A data {dia}/{mes}/{ano} não é válida")
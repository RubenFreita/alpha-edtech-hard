#Questão 10

entrada = int(input("Digite o número a ser encriptado: "))
a = entrada%10
b = (entrada//10)%10
c = (entrada//100)%10
d = (entrada//1000)%10

a=a+1
b=b+1
c=c+1
d=d+1
print(f"O número {entrada} encriptado é: {d%10}{c%10}{b%10}{a%10}",sep="")
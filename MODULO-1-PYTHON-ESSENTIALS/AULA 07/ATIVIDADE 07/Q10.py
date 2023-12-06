
equacao = input("Digite uma equação com parênteses: ")
count = 0
for i in equacao:
    if i == "(":
        count -=1
    elif i == ")":
        count += 1
if count == 0:
    print("Correto")
else:
    print("Incorreto")
    
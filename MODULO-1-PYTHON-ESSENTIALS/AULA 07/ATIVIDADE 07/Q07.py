

str1 = input("Digite a primeira palavra: ")
str2 = input("Digite a segunda palavra: ")
strCoincidencia = ""
for i in str1:
    for j in str2:
        if i == j:
            strCoincidencia += i
            break
print(strCoincidencia.upper())
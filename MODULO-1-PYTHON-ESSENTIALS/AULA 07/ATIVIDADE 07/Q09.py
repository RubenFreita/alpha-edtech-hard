
frase = "".join(input("Digite uma frase: ").split())
fraseInversa = frase[::-1]
print(frase)
print(fraseInversa)
count = 0
for i in range(len(frase)):
    if frase[i].lower() == fraseInversa[i].lower():
        count +=1

if count == len(frase):
    print("É palíndromo")
else:
    print("Não é palíndromo")
nome = "Paulo Marcotti"
print(type(nome))
numeroVogais = 0
for letra in nome:
    letra = letra.lower()
    print('Letra: "', letra, '"')
    for vogal in 'aeiou':
      if letra==vogal:
        numeroVogais += 1
print('comprimento do texto: ', len(nome))
print(numeroVogais)
#

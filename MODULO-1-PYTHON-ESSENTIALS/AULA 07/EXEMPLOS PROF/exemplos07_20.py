
#name = input('Digite o nome do arquivo:')
name = "anotacoes.txt"
handle = open(name, 'r')
#counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        print(word)
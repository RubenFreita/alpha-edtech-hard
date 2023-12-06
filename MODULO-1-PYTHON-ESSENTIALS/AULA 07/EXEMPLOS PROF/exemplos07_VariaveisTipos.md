# Tipos de Variáveis ou Classes de Variáveis em Python

## **Trilha Python 2024 - Módulo 01 - Python Essentials**
## Aula 07 (14/11/2023) - Tipos de Variáveis

Imagine que você está construindo algo com blocos de LEGO. 
Cada bloco é como um tipo de variável, e o jeito como você os encaixa 
é o sistema de tipos.

No Python, existem diferentes tipos de variáveis, como números, textos e listas. 
Esses tipos ajudam a prevenir erros quando você está escrevendo seu programa. 
É como se cada bloco de LEGO tivesse regras sobre com quais outros blocos ele pode se encaixar.

Por exemplo, se você está lidando com números, você usa o tipo de variável 
chamado "int" para representar números inteiros, 
e "float" para números decimais. 

Se está trabalhando com palavras, você usa o tipo "str" para strings.

O sistema de tipos ajuda a garantir que você não misture coisas que não se encaixam. 
Por exemplo, você não tentaria encaixar um bloco de LEGO de rodas em um bloco 
de LEGO de janelas, porque não faz sentido. 
Da mesma forma, o sistema de tipos evita que você faça coisas como tentar somar 
uma palavra com um número.
Muito embora, o Python faça algumas conversões de tipo, permitindo misturar
tipos diferentes de variáveis num mesmo comando.

Então, quando você está programando em Python, lembre-se dos tipos de variáveis 
como diferentes blocos de LEGO que se encaixam de maneiras específicas. 
Isso ajuda a evitar erros e torna seu programa mais robusto.

Variáveis são criadas pelo interpretador da linguagem Python (lembre que Python é uma
linguagem interpretada e não compilada (ou seja, não gera um programa executável, em linguagem
de máquina).
As variaveis são criadas através da atribuição de valores à uma variável
e destruídas pelo coletro de lixo (garbage collector), quando não existem
mais referências a elas.

Em Python, um nome sempre será um objeto. Entretanto, às vezes é conveniente usar 
um nome chamado None ou nulo. 
Python fornece um tipo especial de objeto para esta finalidade chamada NoneType. 
Sempre há somente um objeto do tipo NoneType e o nome desse objeto é None.

A fim de utilizar um objeto em um programa em Python, esse objeto deve ter um nome. 
O nome de um objeto é uma variável usada para identificar esse objeto em um programa. 
Em Python, um objeto precisa iniciar por uma letra ou pelo símbolo (sublinhado _).
Os nomes podem ter letras ou números, mas não outros caracteres especiais.
Letras minísculas ou maiúsculas são diferentes.

Nós podemos explicitamente atribuir um nome ao None

Esta indicação cría um objeto com nome i e liga vários atributos com esse objeto. 
x = 75
O tipo do objeto é int e seu valor é 75.

Alguns atributos de um objeto, tal como seu tipo, são limitados quando o objeto 
é criado e não podem ser mudados. Isto é chamado ligação estática.

As ligações para outros atributos de um objeto, tais como seu valor, 
podem ser mudados durante a execução do programa onde o objeto está. 
Isto é chamado de ligação dinâmica. Reforçando que o novo valor pode ser
de outro tipo.

Existem vários tipos simples de dados predefinidos no Python, tais como:
- Números:
	- inteiros x = 75
	- reais valor =3.1416
	- números complexos (parte real e parte imaginária) c = 3 + 5j
- Texto (chamado usualmente de string)

Além disso, existem tipos que funcionam comocoleções.
Os principais tipo de coleções são:
- Lista
- Tupla
- Dicionário

Os tipos de variáveis no Python podem ser:
- mutáveis: permitem que os conteúdos das variáveis sejam alterados.
- imutáveis: não permitem que os conteúdos das variáveis sejam alterados.

Em Python, os nomes de variáveis são referências que podem ser alteradas em tempo de execução.

Os tipos e funções mais comuns estão implementados na forma de "builtins",
ou seja, eles estão sempre disponíveis em tempo de execução, sem a necessidade 
de importar nenhuma biblioteca.

Exemplos da utilização dos diversos tipos de variáveis em Python

``` python exemplos07_01.py
x = 75
y = x
if x is y:
	print("y e x são o mesmo objeto neste momento")
else:
	print("y e x são objetos diferentes")

z = 75
if x == z:
	print("z e x tem o mesmo valor")
else:
	print("z e x têm valores diferentes")

if type(x) == type(z):
	print("z e x têm o mesmo tipo de variável")
else:
	print("z e x têm não o mesmo tipo de variável")
```

Vamos pensar em orientação a objetos no Python de uma maneira mais descontraída, 
usando uma analogia com o mundo real!

**Classes (ou Famílias de Objetos):**

Imagine que você tem uma família de animais. 
Cada animal tem suas próprias características e comportamentos. 
Em Python, chamamos essa família de animais de "classe". 
Uma classe é como um plano para criar objetos específicos.

**Instâncias (ou Animais Individuais):**

Agora, cada animal específico, como o meu gato (Joey) ou a minha cachorrinha (Kika), 
seria uma "instância" dessa classe de animais. 
As instâncias são como os animais reais que existem com base no plano da classe.

**Atributos (ou Características):**

Cada animal tem suas próprias características, como cor do pelo, tamanho etc. 
Em Python, chamamos essas características de "atributos". 
Por exemplo, um atributo de um gato pode ser a cor do pelo.

**Métodos (ou Comportamentos):**

Os comportamentos dos animais, como correr, miar ou latir, são 
como os "métodos" em Python. 
Os métodos são funções que as instâncias da classe podem executar. 
Por exemplo, um método de um gato pode ser "miar".

**Herança (ou Famílias Relacionadas):**

Se você tem uma família de animais, pode haver características ou 
comportamentos que são comuns a todos, como respirar ou comer. 
Em Python, expressamos isso usando "herança". 
Uma classe pode herdar características e comportamentos de outra, 
assim como uma família pode compartilhar certas características.

Lembre-se, quando você cria um novo animal (instância), 
ele herda todas as características da sua família (classe). 
E, quando esse animal faz alguma coisa especial (método), 
isso é como um comportamento único daquela instância.

Assim, em Python, a orientação a objetos nos ajuda a organizar e estruturar 
nosso código de uma maneira que reflete o mundo real, 
facilitando a compreensão e a manutenção do programa.

## Quebrando uma linha de comando em Python

``` python exemplos07_02.py
# Quebrando a linha de comandos em Python

# No meio de uma expressão matemática, usar a contra-barra
a = 3 +5 * \
	51 / 4

# No meio de uma lista com elementos separados por vírgula
# somente mudar de linha com enter
b = ['a', 'b', 'c', 
        'd', 'e']

# No meio de uma sequência de parâmetros separados por vírgula
# somente mudar de linha com enter
c = min('A', 'B', 'c', 
        'd', 'D')
```

Tipos: Inteiro, ponto flutuante, texto/string, booleano, complexo

``` python exemplos07_03.py
a = 1
print(a)
print(type(a))
print('\n')
#
a = 1.0
print(a)
print(type(a))
print('\n')
#
a = "paulo"
print(a)
print(type(a))
print('\n')
#
a = ('joão' != 'joao')
print(a)
print(type(a))
print('\n')
#
a = 1 + 2j
print(a)
print(type(a))
#
```

Operações

``` python exemplos07_04.py
a = 9
b = 5
print(type(a))
print(type(b))
c = a / b
print(c)
print(type(c))
print('\n')
#
a = 9.0
b = 5.0
print(type(a))
print(type(b))
c = a / b
print(c)
print(type(c))
#
```

Leitura e verificação da corretude

``` python exemplos07_05.py
while True:
  try:
    idade = int(input('\n Digite sua idade: '))
    break
  except ValueError:
    print("\n Valor digitado é invalido, favor digitar um número inteiro para idade.")
```

``` python exemplos07_06.py
x = [3, 41, 12, 9, 74, 15]
print(type(x))

for valoresLista in x:
    print('Laço:', valoresLista)

print(x)
print(*x)
print(type(x))
#for valoresLista in x:
#    print('Laço:', valoresLista)

print(max(x))
print(sum(x))

# Importing the statistics module
import statistics
print(statistics.mean(x))
```

``` python exemplos07_07.py
RAs = [1, 41, 12, 9, 74, 15]
print(type(RAs))
print(RAs[0])
print(type(RAs[0]))
print(RAs[1])
print(RAs[2])
print(RAs[3])
print(RAs[4])
print(RAs[5])
print('comprimento da lista: ', len(RAs))
#
print(RAs[6])
```

``` python exemplos07_08.py
nome = "Paulo Marcotti"
print('Letra: ', nome[0])
print('Letra: ', nome[1])
print('Letra: ', nome[2])
print('Letra: "', nome[3], '"')
print('Letra: "', nome[4], '"')
print('Letra em branco: "', nome[5], '"')
```

``` python exemplos07_09.py
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
```

## Packing, Unpacking

``` python exemplos07_10.py
a, b = 0, "Paulo"
print(a)
print(b)
# Trocando valores sem variável auxiliar
a, b = b, a
print(a)
print(b)
```

## Tuplas são como Listas mas colocadas entre parentesis
As tuple são imutáveis, enquanto as list são mutáveis

``` python exemplos07_11.py
xTupla = (1, 2, 3)
print(xTupla[0])
print(xTupla[1])
print(xTupla[2])

xTupla = (1, 2, 3, 4)
xTupla[2] = 22
```

Leitura de 3 valores na mesma linha do input()
separados por espaço

``` python exemplos07_12.py
V = [int(i) for i in input().split(" ") if i]
N = V[0]
M = V[1]
C = V[2]
print(N, M, C)
```

## Dicionários em Python
https://www.freecodecamp.org/news/python-dictionary-methods-dictionaries-in-python/

``` python exemplos07_13.py
#Dicionários em Python

#Dicionario vazio
dic1 = {}
print(dic1)
print()

#key-value pairs 
dic1 = {1:'Pyton', 2:'Java'}
print(dic1)
print()

dic1 = {'First': 'Python', 'Second': 'Java'}
print(dic1)
print()
#
dic1['Second'] = 'C++'
print(dic1)
print()
#
dic1['Third'] = 'Ruby'
print(dic1)
```

## List

``` python exemplos07_14.py
alunos = ['Deivid', 'Athilio', 'Gabriel', 'Brenda']
print(alunos)
print(type(alunos))
alunos.remove('Gabriel')
print(alunos)
alunos.pop(2)
print(alunos)
alunos.insert(2, 'Vinicius')
print(alunos)
alunos.insert(1, 'Luiz')
print(alunos)
alunos.insert(2, 'Ana')
print(alunos)
alunos.insert(2, 'Carlos')
print(alunos)
#
print(alunos[1])
print(len(alunos))
print(type(alunos))
```

List versus Tuple

https://www.geeksforgeeks.org/python-difference-between-list-and-tuple/

``` python exemplos07_15.py
alunos = ('Yasmin', 'Laura', 'Bruno', 'Antonio')
print(alunos)
print(alunos[1])
print(len(alunos))
print(type(alunos))
```

### pop dictionary

``` python exemplos07_16.py
#pop element
a = dic1.pop('Third')
print('Value:', a)
print('Dictionary:', dic1)
print()

#pop the key-value pair
b = dic1.popitem()
print('Key, value pair:', b)
print('Dictionary', dic1)
print()

#empty dictionary
dic1.clear()
print(dic1)
```

``` python exemplos07_17.py
dic1 = {'First': 'Python', 'Second': 'Java'}
#access elements using keys
print(dic1['First'])
print(dic1.get('Second'))
print()
#
dic1 = {'First': 'Python', 'Second': 'Java', 'Third': 'Ruby'}
#get keys
print(dic1.keys())
#get values
print(dic1.values())
#get key-value pairs
print(dic1.items())
print()
print(dic1.get('First'))
```

``` python exemplos07_18.py
obj1 = {
    "Nome": "Paulo", 
    "Gerente": "Samir",
    "Cargo": "Instrutor", 
    "Idade": 66, 
    "Altura": 1.71, 
    "Trabalho": "Remoto"
}
print(obj1)

#Idade
anosVida = obj1.get("Idade")
print(anosVida)
print()

#Lista de Itens de um Dicionário
itens = obj1.items()
print(itens)
```

``` python exemplos07_19.py
obj1 = {
    "Nome": "Paulo", 
    "Gerente": "Samir",
    "Cargo": "Instrutor", 
    "Idade": 66, 
    "Altura": 1.71, 
    "Trabalho": "Remoto"
}
print(obj1)

dict_values = obj1.values()
print(dict_values)
print()

#
obj1.update({"Altura": 1.69})
print(obj1)
print()

#
obj2 = obj1.copy()
print(obj2)
```

``` anotacoes.txt
Paulo Marcotti ministrando aulas de Python Essentials
Neste verão tão quente como está aqui em São Paulo
O Feriado de quarta-feira, no meio da semana, nem
dá pra aproveitar
```

``` python exemplos07_20.py
#name = input('Digite o nome do arquivo:')
name = "anotacoes.txt"
handle = open(name, 'r')
#counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        print(word)
```

``` python exemplos07_21.py
#name = input('Enter file:')
name = "anotacoes.txt"
handle = open(name, 'r')
counts = dict()

for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

bigcount = None
bigword = None
for word, count in list(counts.items()):
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
```

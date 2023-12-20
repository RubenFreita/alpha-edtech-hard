### Miscelâneas

## Estruturas de Dados

Estrutura de dados é uma maneira organizada de armazenar e manipular dados para que possamos realizar operações eficientes. É como a "caixa" ou "formato" que usamos para guardar informações, permitindo-nos acessá-las, modificá-las e realizar diferentes operações.

Imagine que você está resolvendo um quebra-cabeça. Se todas as peças estão bagunçadas aleatoriamente, levará mais tempo e esforço para encontrar a peça correta. No entanto, se as peças estão organizadas, com bordas e cores similares juntas, torna-se mais fácil resolver o quebra-cabeça. Da mesma forma, as estruturas de dados ajudam a organizar informações de maneira eficiente para facilitar a manipulação.

**Tipos Comuns de Estruturas de Dados:**

1. **Arrays:**
   - **O que são:** Uma coleção ordenada de elementos, onde cada elemento tem um índice.
   - **Para que servem:** Acesso rápido a elementos, especialmente se soubermos o índice.
   - **Analogia:** Uma prateleira de livros numerados.

2. **Listas Ligadas:**
   - **O que são:** Uma sequência de elementos onde cada elemento possui uma referência ao próximo elemento na sequência.
   - **Para que servem:** Inserção e exclusão eficientes de elementos.
   - **Analogia:** Uma corrente onde cada elo aponta para o próximo.

3. **Pilhas:**
   - **O que são:** Uma coleção de elementos com operações de inserção (push) e remoção (pop) realizadas no topo.
   - **Para que servem:** Útil para operações LIFO (Last In, First Out), como desfazer ações em um software.
   - **Analogia:** Pilha de pratos onde sempre adicionamos ou removemos do topo.

4. **Filas:**
   - **O que são:** Semelhantes a pilhas, mas operam em um princípio FIFO (First In, First Out).
   - **Para que servem:** Útil para operações onde o primeiro elemento a entrar é o primeiro a sair.
   - **Analogia:** Uma fila no supermercado.

5. **Árvores:**
   - **O que são:** Estrutura hierárquica de elementos, com um elemento chamado raiz e outros agrupados em níveis.
   - **Para que servem:** Organizar dados hierarquicamente, como a estrutura de pastas em um computador.
   - **Analogia:** Uma árvore genealógica.

6. **Grafos:**
   - **O que são:** Conjunto de vértices (nós) conectados por arestas.
   - **Para que servem:** Modelar relações complexas entre diferentes elementos.
   - **Analogia:** Uma rede de estradas interconectadas.

Entender estruturas de dados é fundamental para projetar algoritmos eficientes e resolver problemas de forma otimizada. Escolher a estrutura de dados certa para um determinado problema pode fazer uma grande diferença na eficiência do seu código.
## Engenharia de Software

Engenharia de Software é uma disciplina da ciência da computação que se dedica à concepção, construção, manutenção e evolução de sistemas de software de forma sistemática, controlada e eficiente. É a aplicação de princípios de engenharia para o desenvolvimento de software de alta qualidade.

**Princípios Fundamentais da Engenharia de Software:**

1. **Processo Sistemático:**
   - **O que é:** A Engenharia de Software segue um processo bem definido, que consiste em fases como análise, projeto, implementação, testes e manutenção.
   - **Analogia:** Assim como construir uma casa, prédio ou uma pirâmide segue uma sequência de etapas, o desenvolvimento de software também tem um processo.

2. **Controle e Organização:**
   - **O que é:** Envolve a aplicação de técnicas e métodos para organizar e controlar o desenvolvimento de software, garantindo eficiência e qualidade.
   - **Analogia:** Semelhante à gestão de um projeto de construção, onde há planejamento, monitoramento e controle.

3. **Qualidade e Eficiência:**
   - **O que é:** A busca pela qualidade no software, garantindo que ele atenda aos requisitos e seja eficiente em termos de desempenho e recursos.
   - **Analogia:** Como um fabricante de carros que se esforça para produzir veículos seguros, confiáveis e eficientes.

**Atividades Principais da Engenharia de Software:**

1. **Análise de Requisitos:**
   - **O que é:** Entender e documentar os requisitos do cliente para o software.
   - **Analogia:** Como um arquiteto que coleta informações sobre o que o cliente deseja em uma casa.

2. **Projeto de Software:**
   - **O que é:** Criar uma estrutura lógica para o software com base nos requisitos.
   - **Analogia:** Como um engenheiro que projeta os planos detalhados de uma construção.

3. **Implementação:**
   - **O que é:** Escrever o código-fonte do software com base no design.
   - **Analogia:** Como os engenheiros, projetistas e construtores que seguem o planejamento definido anteriormente para construir a casa.

4. **Testes:**
   - **O que é:** Verificar se o software funciona conforme esperado e identificar possíveis erros.
   - **Analogia:** Semelhante a inspecionar uma casa para garantir que tudo funcione corretamente. Exemplo, ao testar a entrada do carro na garagem foi esquecido que o motorista precisa descer do carro após estacionar.

5. **Manutenção:**
   - **O que é:** Realizar alterações no software para corrigir erros, adicionar novos recursos ou melhorar o desempenho.
   - **Analogia:** Como fazer correções antes da entrega da casa para atender às necessidades não previstas no projeto da casa. Exemplo, mesmo que a garagem estava correta para um carro de passageiro, o proprietário esqueceu de avisar que ele tinha um caminhão utilitário baú.

6. **Evolução:**
   - **O que é:** Realizar alterações substanciais no software mas não para corrigir erros, agora para adicionar novas funcionalidades, recursos ou melhorar o desempenho.
   - **Analogia:** Como fazer reformas e ampliações em uma casa para atender às novas necessidades. Exemplo, a casa funcional mas agora o pai está com uma idade avançada e precisa rampas para cadeiras de rodas, barras de apoio nos banheiros um novo quarto no andar térreo.

**Benefícios da Engenharia de Software:**

- **Eficiência:** Desenvolver software de forma mais rápida e com menos erros.
- **Qualidade:** Entregar produtos de software mais confiáveis e que atendam às expectativas.
- **Controle:** Gerenciar o desenvolvimento de software de forma organizada e controlada.

Engenharia de Software é a abordagem organizada e disciplinada para desenvolver software. Assim como em outras engenharias, ela visa criar soluções confiáveis e eficientes para atender às necessidades dos usuários. Essa disciplina é crucial para lidar com a crescente complexidade dos sistemas de software na atualidade.
## TDD

TDD (Test-Driven Development) ou Desenvolvimento Orientado a Testes, é uma prática na engenharia de software em que você escreve testes automatizados antes de escrever o código de produção. O ciclo básico do TDD consiste em três etapas principais: escrever um teste, fazer o teste passar e, em seguida, refatorar (melhorar) o código escrito.

**O Ciclo do TDD:**

1. **Escrever um Teste:**
   - **O que é:** Antes de começar a escrever o código real, você escreve um teste que descreve uma funcionalidade específica que deseja implementar.
   - **Analogia:** Se você estivesse construindo um carro, seria como escrever uma lista de verificações para garantir que cada parte do carro funcione corretamente.

2. **Fazer o Teste Passar:**
   - **O que é:** Escrever o código de produção mínimo necessário para fazer o teste passar. Atualmente a ideia do MVP (Mínimo Produto Viável, como implementar e aprimorar para gerar mais resultados antes de investir muito dinheiro) como usar esse conceito para validar uma ideia e crescer com o feedback do mercado.
   - **Analogia:** No contexto do carro, isso seria realmente construir a parte do carro correspondente ao que você listou na sua lista de verificações.

3. **Refatorar o Código:**
   - **O que é:** Melhorar o código sem alterar seu comportamento, mantendo os testes passando.
   - **Analogia:** Ajustar ou melhorar as peças do carro para torná-las mais eficientes, mantendo as funcionalidades.

**Por que usar TDD?**

1. **Feedback Rápido:**
   - O TDD fornece feedback rápido sobre a qualidade do seu código. Se um teste falhar, você saberá imediatamente que algo precisa ser corrigido.

2. **Código Mais Robusto:**
   - O código resultante do TDD geralmente é mais robusto, pois é validado por testes automatizados.

3. **Facilita a Manutenção:**
   - Testes automatizados tornam a manutenção do código mais fácil. Se você precisa fazer alterações no futuro, os testes ajudam a garantir que as alterações não quebram a funcionalidade existente.

4. **Design Melhorado:**
   - O TDD muitas vezes leva a um design de código melhor, pois você precisa pensar nas interfaces e na estrutura do código antes de implementar.

5. **Confiança no Código:**
   - Ter um conjunto abrangente de testes automatizados dá confiança de que o código está funcionando conforme o esperado.

**Exemplo Prático:**

Vamos imaginar que você está desenvolvendo uma função simples que adiciona dois números. No TDD, o ciclo seria assim:

1. **Escrever um Teste:**
   - Escrever um teste que chama a função `adicionar(2, 3)` e verifica se o resultado é 5.

2. **Fazer o Teste Passar:**
   - Implementar a função `adicionar` para retornar a soma de dois números.

3. **Refatorar o Código:**
   - Se necessário, ajustar o código para torná-lo mais limpo ou eficiente, mantendo os testes passando.

O TDD é uma abordagem que visa criar software de alta qualidade, confiável e fácil de manter. Ele promove a escrita de código testável desde o início do desenvolvimento, garantindo que cada parte do sistema seja verificada automaticamente quanto à conformidade com os requisitos. Isso resulta em um processo de desenvolvimento mais seguro e eficiente.

# Hash Table Python construindo com TDD (Test Development Drive)

https://realpython.com/python-hash-table/
Bartosz Zaczynski
## Conteúdo

- [Get to Know the Hash Table Data Structure](https://realpython.com/python-hash-table/#get-to-know-the-hash-table-data-structure)
    - [Hash Table vs Dictionary](https://realpython.com/python-hash-table/#hash-table-vs-dictionary)
    - [Hash Table: An Array With a Hash Function](https://realpython.com/python-hash-table/#hash-table-an-array-with-a-hash-function)
- [Understand the Hash Function](https://realpython.com/python-hash-table/#understand-the-hash-function)
    - [Examine Python’s Built-in hash()](https://realpython.com/python-hash-table/#examine-pythons-built-in-hash)
    - [Dive Deeper Into Python’s hash()](https://realpython.com/python-hash-table/#dive-deeper-into-pythons-hash)
    - [Identify Hash Function Properties](https://realpython.com/python-hash-table/#identify-hash-function-properties)
    - [Compare an Object’s Identity With Its Hash](https://realpython.com/python-hash-table/#compare-an-objects-identity-with-its-hash)
    - [Make Your Own Hash Function](https://realpython.com/python-hash-table/#make-your-own-hash-function)
- [Build a Hash Table Prototype in Python With TDD](https://realpython.com/python-hash-table/#build-a-hash-table-prototype-in-python-with-tdd)
    - [Take a Crash Course in Test-Driven Development](https://realpython.com/python-hash-table/#take-a-crash-course-in-test-driven-development)
    - [Define a Custom HashTable Class](https://realpython.com/python-hash-table/#define-a-custom-hashtable-class)
    - [Insert a Key-Value Pair](https://realpython.com/python-hash-table/#insert-a-key-value-pair)
    - [Find a Value by Key](https://realpython.com/python-hash-table/#find-a-value-by-key)
    - [Delete a Key-Value Pair](https://realpython.com/python-hash-table/#delete-a-key-value-pair)
    - [Update the Value of an Existing Pair](https://realpython.com/python-hash-table/#update-the-value-of-an-existing-pair)
    - [Get the Key-Value Pairs](https://realpython.com/python-hash-table/#get-the-key-value-pairs)
    - [Use Defensive Copying](https://realpython.com/python-hash-table/#use-defensive-copying)
    - [Get the Keys and Values](https://realpython.com/python-hash-table/#get-the-keys-and-values)
    - [Report the Hash Table’s Length](https://realpython.com/python-hash-table/#report-the-hash-tables-length)
    - [Make the Hash Table Iterable](https://realpython.com/python-hash-table/#make-the-hash-table-iterable)
    - [Represent the Hash Table in Text](https://realpython.com/python-hash-table/#represent-the-hash-table-in-text)
    - [Test the Equality of Hash Tables](https://realpython.com/python-hash-table/#test-the-equality-of-hash-tables)
- [Resolve Hash Code Collisions](https://realpython.com/python-hash-table/#resolve-hash-code-collisions)
    - [Find Collided Keys Through Linear Probing](https://realpython.com/python-hash-table/#find-collided-keys-through-linear-probing)
    - [Use Linear Probing in the HashTable Class](https://realpython.com/python-hash-table/#use-linear-probing-in-the-hashtable-class)
    - [Let the Hash Table Resize Automatically](https://realpython.com/python-hash-table/#let-the-hash-table-resize-automatically)
    - [Calculate the Load Factor](https://realpython.com/python-hash-table/#calculate-the-load-factor)
    - [Isolate Collided Keys With Separate Chaining](https://realpython.com/python-hash-table/#isolate-collided-keys-with-separate-chaining)
- [Retain Insertion Order in a Hash Table](https://realpython.com/python-hash-table/#retain-insertion-order-in-a-hash-table)
- [Use Hashable Keys](https://realpython.com/python-hash-table/#use-hashable-keys)
    - [Hashability vs Immutability](https://realpython.com/python-hash-table/#hashability-vs-immutability)
    - [The Hash-Equal Contract](https://realpython.com/python-hash-table/#the-hash-equal-contract)
- [Conclusion](https://realpython.com/python-hash-table/#conclusion)

## Introdução HashTable

Criado há mais de meio século, a tabela hash é uma estrutura de dados clássica que tem sido fundamental para a programação. Até os dias de hoje, ela ajuda a resolver muitos problemas da vida real, como indexar tabelas de banco de dados, armazenar valores calculados em cache ou implementar conjuntos. Frequentemente, ela é abordada em entrevistas de emprego, e o Python utiliza tabelas hash em muitos lugares para tornar as consultas de nomes quase instantâneas.

Embora o Python venha com sua própria tabela hash chamada "dict" (dicionário), pode ser útil entender como as tabelas hash funcionam nos bastidores. Uma avaliação de codificação pode até desafiá-lo a construir uma. Este tutorial irá guiá-lo através dos passos de implementar uma tabela hash do zero, como se não houvesse nenhuma no Python. Ao longo do caminho, você enfrentará alguns desafios que introduzirão conceitos importantes e lhe darão uma ideia de por que as tabelas hash são tão rápidas.

Além disso, você terá um curso prático de desenvolvimento orientado a testes (TDD) e praticará ativamente enquanto constrói sua tabela hash passo a passo. Não é necessário ter experiência prévia com TDD, mas ao mesmo tempo, você não ficará entediado mesmo que tenha!

Neste tutorial, você aprenderá:

- Como uma tabela hash difere de um dicionário
- Como implementar uma tabela hash do zero em Python
- Como lidar com colisões de hash e outros desafios
- Quais são as propriedades desejadas de uma função hash
- Como o hash() do Python funciona nos bastidores

Será útil se você já estiver familiarizado com dicionários em Python e tiver conhecimento básico de princípios de programação orientada a objetos. Para obter o código-fonte completo e os passos intermediários da tabela hash implementada neste tutorial, siga o link abaixo.

### Conheça a Estrutura de Dados Tabela Hash

Antes de aprofundar, é importante familiarizar-se com a terminologia, pois pode ficar um pouco confusa. Coloquialmente, o termo "tabela hash" ou "hash map" é frequentemente usado de forma intercambiável com a palavra "dicionário". No entanto, há uma diferença sutil entre os dois conceitos, pois o primeiro é mais específico que o último.

#### Tabela Hash vs. Dicionário

Na ciência da computação, um dicionário é um tipo de dado abstrato composto por chaves e valores organizados em pares. Além disso, ele define as seguintes operações para esses elementos:

- Adicionar um par chave-valor
- Excluir um par chave-valor
- Atualizar um par chave-valor
- Encontrar um valor associado à chave fornecida

De certa forma, esse tipo de dado abstrato se assemelha a um dicionário bilíngue, onde as chaves são palavras estrangeiras e os valores são suas definições ou traduções para outros idiomas. No entanto, nem sempre é necessário haver um sentido de equivalência entre chaves e valores. Um catálogo telefônico é outro exemplo de um dicionário, que combina nomes com os respectivos números de telefone.

Sempre que você mapeia uma coisa para outra ou associa um valor a uma chave, você está essencialmente usando uma espécie de dicionário. É por isso que os dicionários também são conhecidos como mapas ou arrays associativos.

Dicionários têm algumas propriedades interessantes. Uma delas é que você pode pensar em um dicionário como uma função matemática que projeta um ou mais argumentos para exatamente um valor. As consequências diretas desse fato são as seguintes:

- Apenas Pares Chave-Valor: Você não pode ter uma chave sem o valor ou vice-versa em um dicionário. Eles sempre vão juntos.
- Chaves e Valores Arbitrários: Chaves e valores podem pertencer a dois conjuntos disjuntos do mesmo tipo ou tipos diferentes. Tanto chaves quanto valores podem ser quase qualquer coisa, como números, palavras ou até mesmo imagens.
- Pares Chave-Valor Não Ordenados: Devido ao último ponto, os dicionários geralmente não definem nenhuma ordem para seus pares chave-valor. No entanto, isso pode depender da implementação específica.
- Chaves Únicas: Um dicionário não pode conter chaves duplicadas, pois isso violaria a definição de uma função.
- Valores Não Únicos: O mesmo valor pode ser associado a muitas chaves, mas não é obrigatório.

Existem conceitos relacionados que estendem a ideia de um dicionário. Por exemplo, um multimapa permite que você tenha mais de um valor por chave, enquanto um mapa bidirecional não apenas mapeia chaves para valores, mas também fornece mapeamento na direção oposta. No entanto, neste tutorial, você considerará apenas o dicionário regular, que mapeia exatamente um valor para cada chave.

---
Figura: Representação Gráfica de um Tipo de Dado Abstrato Dicionário
É um mapa unidirecional de chaves para valores, que são dois conjuntos completamente diferentes de elementos. Imediatamente, você pode ver menos valores do que chaves, pois a palavra "bow" acontece ser um homônimo com múltiplos significados. Conceitualmente, este dicionário ainda contém quatro pares, no entanto. Dependendo de como você decidiu implementá-lo, você poderia reutilizar valores repetidos para conservar memória ou duplicá-los para simplicidade.

---
Agora, como você codificaria tal dicionário em uma linguagem de programação? A resposta correta é que você não o faria, porque a maioria das linguagens modernas inclui dicionários como tipos de dados primitivos ou classes em suas bibliotecas padrão. O Python vem com um tipo embutido chamado "dict", que já encapsula uma estrutura de dados altamente otimizada escrita em C, para que você não precise escrever um dicionário do zero.

---

O dict do Python permite que você realize todas as operações de dicionário listadas no início desta seção:

```python
>>> glossário = {"BDFL": "Benevolent Dictator For Life"}
>>> glossário["GIL"] = "Global Interpreter Lock"  # Adicionar
>>> glossário["BDFL"] = "Guido van Rossum"  # Atualizar
>>> del glossário["GIL"]  # Excluir
>>> glossário["BDFL"]  # Buscar
'Guido van Rossum'
>>> glossário
{'BDFL': 'Guido van Rossum'}
```

Com a sintaxe de colchetes (`[ ]`), você pode adicionar um novo par chave-valor a um dicionário. Você também pode atualizar o valor ou excluir um par existente identificado por uma chave. Finalmente, você pode procurar o valor associado à chave fornecida.

Você pode fazer uma pergunta diferente. Como o dicionário embutido realmente funciona? Como ele mapeia chaves de tipos de dados arbitrários e como o faz tão rapidamente?

Encontrar uma implementação eficiente desse tipo de dado abstrato é conhecido como o problema do dicionário. Uma das soluções mais conhecidas aproveita a estrutura de dados da tabela hash, que você está prestes a explorar. No entanto, observe que essa não é a única maneira de implementar um dicionário em geral. Outra implementação popular é baseada em uma árvore rubro-negra.

Tabela Hash: Um Array Com uma Função de Hash

Você já se perguntou por que acessar elementos de sequências em Python é tão rápido, independentemente do índice solicitado? Diga que você estava trabalhando com uma sequência muito longa de caracteres, como esta:

```python
>>> import string
>>> texto = string.ascii_uppercase * 100_000_000

>>> texto[:50]  # Mostra os primeiros 50 caracteres
'ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWX'

>>> len(texto)
2600000000
```

Há 2,6 bilhões de caracteres provenientes de letras ASCII repetidas na variável texto acima, que você pode contar com a função len() do Python. No entanto, obter o primeiro, do meio, último ou qualquer outro caractere desta string é igualmente rápido:

```python
>>> texto[0]  # O primeiro elemento
'A'

>>> texto[len(texto) // 2]  # O elemento do meio
'A'

>>> texto[-1]  # O último elemento, o mesmo que texto[len(texto) - 1]
'Z'
```

O mesmo é válido para todos os tipos de sequências em Python, como listas e tuplas. Como assim? O segredo para essa velocidade impressionante é que sequências em Python são respaldadas por um array, que é uma estrutura de dados de acesso aleatório. Ele segue dois princípios:

1. O array ocupa um bloco contínuo de memória.
2. Cada elemento no array tem um tamanho fixo conhecido antecipadamente.

Quando você conhece o endereço de memória de um array, chamado de offset, então pode chegar ao elemento desejado no array instantaneamente calculando uma fórmula bastante simples:
Fórmula para Calcular o Endereço de Memória de um Elemento de Sequência
Fórmula para Calcular o Endereço de Memória de um Elemento de Sequência

Você começa no offset do array, que também é o endereço do primeiro elemento do array, com o índice zero. Em seguida, avança adicionando o número necessário de bytes, que você obtém multiplicando o tamanho do elemento pelo índice do elemento alvo. Sempre leva a mesma quantidade de tempo para multiplicar e adicionar alguns números juntos.

Observação: Ao contrário dos arrays, as listas do Python podem conter elementos heterogêneos de tamanhos variados, o que quebraria a fórmula acima. Para mitigar isso, o Python adiciona outro nível de indireção introduzindo um array de ponteiros para locais de memória, em vez de armazenar valores diretamente no array:
Array de Ponteiros para Endereços de Memória
Array de Ponteiros para Endereços de Memória

Ponteiros são apenas números inteiros, que sempre ocupam a mesma quantidade de espaço. É costume denotar endereços de memória usando a notação hexadecimal. O Python e algumas outras linguagens prefixam tais números com 0x.

Ok, então você sabe que encontrar um elemento em um array é rápido, não importa onde esse elemento esteja fisicamente localizado. Você pode pegar a mesma ideia e reutilizá-la em um dicionário? Sim!

As tabelas hash recebem seu nome de um truque chamado hashing, que permite traduzir uma chave arbitrária em um número inteiro que pode funcionar como um índice em um array regular. Portanto, em vez de pesquisar um valor por um índice numérico, você o buscará por uma chave arbitrária sem uma perda de desempenho perceptível. Isso é interessante!

Na prática, o hashing não funcionará com todas as chaves, mas a maioria dos tipos incorporados no Python pode ser hashada. Se você seguir algumas regras, poderá criar seus próprios tipos hasháveis também. Você aprenderá mais sobre o hashing na próxima seção.

Entender a Função de Hash

Uma função de hash realiza o hashing transformando qualquer dado em uma sequência de bytes de tamanho fixo chamada valor de hash ou código de hash. É um número que pode funcionar como uma impressão digital digital ou um resumo, geralmente muito menor que os dados originais, o que permite verificar sua integridade. Se você já baixou um arquivo grande da Internet, como uma imagem de disco de uma distribuição Linux, talvez tenha notado um checksum MD5 ou SHA-2 na página de download.

Além de verificar a integridade dos dados e resolver o problema do dicionário, as funções de hash ajudam em outras áreas, incluindo segurança e criptografia. Por exemplo, você geralmente armazena senhas hashadas em bancos de dados para mitigar o risco de vazamentos de dados. Assinaturas digitais envolvem o uso de hashing para criar um resumo da mensagem antes da criptografia. Transações de blockchain são outro exemplo primário do uso de uma função de hash para fins criptográficos.

Nota: Uma função de hash criptográfica é um tipo especial de função de hash que deve atender a alguns requisitos adicionais. Neste tutorial, você encontrará apenas a forma mais básica da função de hash usada na estrutura de dados da tabela hash.

Embora existam muitos algoritmos de hash, todos compartilham algumas propriedades comuns que você está prestes a descobrir nesta seção. Implementar corretamente uma boa função de hash é uma tarefa difícil que pode exigir a compreensão de matemática avançada envolvendo números primos. Felizmente, você geralmente não precisa implementar manualmente tal algoritmo.

O Python vem com um módulo hashlib embutido, que fornece uma variedade de funções de hash criptográficas conhecidas, bem como algoritmos de checksum menos seguros. A linguagem também possui uma função global hash(), usada principalmente para busca rápida de elementos em dicionários e conjuntos. Você pode estudar como ela funciona primeiro para aprender sobre as propriedades mais importantes das funções de hash.
Examine o hash() Embutido do Python

Antes de tentar implementar uma função de hash do zero, espere um momento e analise o hash() do Python para destilar suas propriedades. Isso ajudará você a entender quais problemas estão envolvidos ao projetar sua própria função de hash.

Nota: A escolha de uma função de hash pode impactar drasticamente o desempenho da sua tabela hash. Portanto, você dependerá da função hash() embutida ao construir uma tabela hash personalizada mais tarde neste tutorial. Implementar uma função de hash nesta seção serve apenas como um exercício.

Para começar, experimente chamar hash() em algumas literais de tipos de dados embutidos no Python, como números e strings, para ver como a função se comporta:

```python
>>> hash(3.14)
322818021289917443

>>> hash(3.14159265358979323846264338327950288419716939937510)
326490430436040707

>>> hash("Lorem")
7677195529669851635

>>> hash("Lorem ipsum dolor sit amet, consectetur adipisicing elit,"
... "sed do eiusmod tempor incididunt ut labore et dolore magna"
... "aliqua. Ut enim ad minim veniam, quis nostrud exercitation"
... "ullamco laboris nisi ut aliquip ex ea commodo consequat."
... "Duis aute irure dolor in reprehenderit in voluptate velit"
... "esse cillum dolore eu fugiat nulla pariatur. Excepteur sint"
... "occaecat cupidatat non proident, sunt in culpa qui officia"
... "deserunt mollit anim id est laborum.")
1107552240612593693
```

Já existem várias observações que você pode fazer ao analisar o resultado. Em primeiro lugar, a função de hash embutida pode retornar valores diferentes em seu ambiente para algumas das entradas mostradas acima. Enquanto a entrada numérica sempre parece produzir um valor de hash idêntico, a string provavelmente não. Por quê? Pode parecer que hash() é uma função não determinística, mas isso não poderia estar mais longe da verdade!

Quando você chama hash() com o mesmo argumento dentro da sessão existente do seu interpretador, você continuará obtendo o mesmo resultado:

```python
>>> hash("Lorem")
7677195529669851635

>>> hash("Lorem")
7677195529669851635

>>> hash("Lorem")
7677195529669851635
```

Isso ocorre porque os valores de hash são imutáveis e não mudam durante a vida útil de um objeto. No entanto, assim que você sair do Python e iniciá-lo novamente, é quase certo que verá valores de hash diferentes em invocações diferentes do Python. Você pode testar isso tentando a opção -c para executar um script de uma linha no terminal:

   Windows
   Linux + macOS

```bash
C:\> python -c print(hash('Lorem'))
6182913096689556094

C:\> python -c print(hash('Lorem'))
1756821463709528809

C:\> python -c print(hash('Lorem'))
8971349716938911741
```

Esse é um comportamento esperado, implementado no Python como uma medida contra ataques de Negação de Serviço (DoS) que exploravam uma vulnerabilidade conhecida das funções de hash em servidores web. Atacantes podiam abusar de um algoritmo de hash fraco para criar colisões de hash, sobrecarregando o servidor e tornando-o inacessível. O resgate era um motivo típico para o ataque, já que a maioria das vítimas ganhava dinheiro por meio de uma presença online ininterrupta.

Hoje, o Python habilita a randomização de hash por padrão para algumas entradas, como strings, para tornar os valores de hash menos previsíveis. Isso torna o hash() um pouco mais seguro e o ataque mais difícil. No entanto, você pode desativar a randomização, definindo um valor de semente fixo por meio da variável de ambiente PYTHONHASHSEED, por exemplo:

   Windows
   Linux + macOS

```bash
C:\> set PYTHONHASHSEED=1

C:\> python -c print(hash('Lorem'))
440669153173126140

C:\> python -c print(hash('Lorem'))
440669153173126140

C:\> python -c print(hash('Lorem'))
440669153173126140
```

Agora, cada invocação do Python produz o mesmo valor de hash para uma entrada conhecida. Isso pode ajudar na partição ou compartilhamento de dados em um cluster de interpretadores Python distribuídos. Apenas tenha cuidado e compreenda os riscos envolvidos ao desativar a randomização de hash. Em resumo, o hash() do Python é de fato uma função determinística, o que é uma das características mais fundamentais da função de hash.

Aprofunde-se no hash() do Python

Outra característica interessante do hash() é que ele sempre produz uma saída de tamanho fixo, não importa quão grande tenha sido a entrada. Em Python, o valor de hash é um número inteiro com uma magnitude moderada. Ocasionalmente, ele pode resultar em um número negativo, então leve isso em consideração se planejar depender dos valores de hash de alguma forma:

```python
>>> hash("Lorem")
-972535290375435184
```

A consequência natural de uma saída de tamanho fixo é que a maior parte da informação original é perdida de forma irreversível durante o processo. Isso é aceitável, já que você deseja que o valor de hash resultante atue como um resumo unificado de dados arbitrariamente grandes, afinal. No entanto, como a função de hash projeta um conjunto potencialmente infinito de valores em um espaço finito, isso pode levar a uma colisão de hash quando duas entradas diferentes produzem o mesmo valor de hash.

Nota: Se você tem inclinação matemática, pode usar o princípio das gaiolas para descrever colisões de hash de maneira mais formal:

    Dados m itens e n contêineres, se m > n, então há pelo menos um contêiner com mais de um item.

Neste contexto, os itens são um número potencialmente infinito de valores que você alimenta na função de hash, enquanto os contêineres são seus valores de hash atribuídos a partir de um pool finito.

Colisões de hash são um conceito essencial em tabelas de hash, que você revisitará posteriormente com mais profundidade ao implementar sua tabela de hash personalizada. Por enquanto, você pode pensar nelas como altamente indesejáveis. Você deve evitar colisões de hash o máximo possível, pois podem levar a pesquisas muito ineficientes e podem ser exploradas por hackers. Portanto, uma boa função de hash deve minimizar a probabilidade de uma colisão de hash tanto para segurança quanto para eficiência.

Na prática, isso muitas vezes significa que a função de hash deve atribuir valores uniformemente distribuídos sobre o espaço disponível. Você pode visualizar a distribuição de valores de hash produzidos pela função hash() do Python plotando um histograma textual no seu terminal. Copie o bloco de código a seguir e salve-o em um arquivo chamado hash_distribution.py:

```python
# hash_distribution.py

from collections import Counter

def distribuir(itens, num_containers, funcao_hash=hash):
    return Counter([funcao_hash(item) % num_containers for item in itens])

def plotar(histograma):
    for chave in sorted(histograma):
        contagem = histograma[chave]
        preenchimento = (max(histograma.values()) - contagem) * " "
        print(f"{chave:3} {'■' * contagem}{preenchimento} ({contagem})")
```

Ele usa uma instância Counter para representar convenientemente o histograma dos valores de hash dos itens fornecidos. Os valores de hash são distribuídos sobre o número especificado de contêineres envolvendo-os com o operador módulo. Agora, você pode pegar cem caracteres ASCII imprimíveis, por exemplo, calcular seus valores de hash e mostrar sua distribuição:

```python
>>> from hash_distribution import plotar, distribuir
>>> from string import printable

>>> plotar(distribuir(printable, num_containers=2))
0 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ (51)
1 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   (49)

>>> plotar(distribuir(printable, num_containers=5))
0 ■■■■■

■■■■■■■■■■■■■■            (15)
1 ■■■■■■■■■■■■■■■■■■■■■■■■■■ (26)
2 ■■■■■■■■■■■■■■■■■■■■■■     (22)
3 ■■■■■■■■■■■■■■■■■■         (18)
4 ■■■■■■■■■■■■■■■■■■■        (19)
```

Quando há apenas dois contêineres, você deve esperar uma distribuição mais ou menos equitativa. Adicionar mais contêineres deve resultar em preenchê-los mais ou menos uniformemente. Como você pode ver, a função hash() embutida é bastante boa, mas não perfeita na distribuição uniforme dos valores de hash.

Relacionado a isso, a distribuição uniforme de valores de hash geralmente é pseudoaleatória, o que é especialmente importante para funções de hash criptográficas. Isso impede que potenciais atacantes usem análise estatística para tentar prever a correlação entre a entrada e a saída da função de hash. Considere alterar uma única letra em uma string e verifique como isso afeta o valor de hash resultante em Python:

```python
>>> hash("Lorem")
1090207136701886571

>>> hash("Loren")
4415277245823523757
```

Agora é um valor de hash completamente diferente, apesar de apenas uma letra ser diferente. Os valores de hash geralmente estão sujeitos a um efeito avalanche, já que até a menor alteração na entrada é amplificada. No entanto, essa característica da função de hash não é essencial para implementar uma estrutura de dados de tabela de hash.

Na maioria dos casos, a função hash() do Python exibe ainda outra característica não essencial de funções de hash criptográficas, que decorre do princípio das gaiolas mencionado anteriormente. Ela se comporta como uma função unidirecional porque encontrar sua inversa é praticamente impossível na maioria dos casos.

```python
>>> hash(42)
42
```

Os valores de hash de inteiros pequenos são iguais a si mesmos, o que é um detalhe de implementação que o CPython usa por simplicidade e eficiência. Lembre-se de que os valores de hash reais não importam, desde que você possa calculá-los de maneira determinística.

Por fim, calcular um valor de hash em Python é rápido, mesmo para entradas muito grandes. Em um computador moderno, chamar hash() com uma string de 100 milhões de caracteres como argumento retorna instantaneamente. Se não fosse tão rápido, a sobrecarga adicional do cálculo do valor de hash compensaria os benefícios do uso de hash em primeiro lugar.

Identificar Propriedades da Função de Hash

Com base no que você aprendeu até agora sobre o hash() do Python, agora você pode tirar conclusões sobre as propriedades desejadas de uma função de hash em geral. Aqui está um resumo dessas características, comparando a função de hash regular com sua versão criptográfica:

| Característica             | Função de Hash       | Função de Hash Criptográfica |
|-----------------------------|----------------------|-------------------------------|
| Determinística              | ✔️                   | ✔️                            |
| Entrada Universal           | ✔️                   | ✔️                            |
| Saída de Tamanho Fixo       | ✔️                   | ✔️                            |
| Rápida para Calcular        | ✔️                   | ✔️                            |
| Distribuição Uniforme       | ✔️                   | ✔️                            |
| Distribuição Aleatória      |                      | ✔️                            |
| Semente Aleatória           |                      | ✔️                            |
| Função Unidirecional        |                      | ✔️                            |
| Efeito Avalanche            |                      | ✔️                            |

Os objetivos de ambos os tipos de funções de hash se sobrepõem, então eles compartilham algumas características comuns. Por outro lado, uma função de hash criptográfica fornece garantias adicionais em torno da segurança.

Antes de criar sua própria função de hash, você dará uma olhada em outra função incorporada ao Python que é aparentemente sua substituta mais direta.

Comparar a Identidade de um Objeto com Seu Hash

Provavelmente, uma das implementações de função de hash mais diretas imagináveis em Python é a built-in id(), que informa a identidade de um objeto. No interpretador padrão do Python, a identidade é o mesmo que o endereço de memória do objeto expresso como um número inteiro:

```python
>>> id("Lorem")
139836146678832
```

A função id() possui a maioria das propriedades desejadas de uma função de hash. Afinal, é super rápida e funciona com qualquer entrada. Ela retorna um inteiro de tamanho fixo de maneira determinística. Ao mesmo tempo, você não pode facilmente recuperar o objeto original com base em seu endereço de memória. Os endereços de memória em si são imutáveis durante a vida útil de um objeto e um tanto randomizados entre as execuções do interpretador.

Então, por que o Python insiste em usar uma função diferente para hash?

Em primeiro lugar, a intenção do id() é diferente do hash(), então outras distribuições do Python podem implementar a identidade de maneiras alternativas. Em segundo lugar, os endereços de memória são previsíveis sem ter uma distribuição uniforme, o que é tanto inseguro quanto severamente ineficiente para hashing. Finalmente, objetos iguais geralmente devem produzir o mesmo código de hash mesmo que tenham identidades distintas.

Nota: Mais tarde, você aprenderá mais sobre o contrato entre a igualdade de valores e os códigos de hash correspondentes.

Com isso fora do caminho, você finalmente pode pensar em criar sua própria função de hash.

Criar Sua Própria Função de Hash

Projetar uma função de hash que atenda a todos os requisitos do zero é difícil. Como mencionado anteriormente, você usará a função hash() embutida para criar seu protótipo de tabela de hash na próxima seção. No entanto, tentar construir uma função de hash do zero é uma ótima maneira de aprender como ela funciona. No final desta seção, você terá apenas uma função de hash rudimentar que está longe de ser perfeita, mas terá obtido insights valiosos.

Neste exercício, você pode se limitar a apenas um tipo de dado a princípio e implementar uma função de hash bruta ao seu redor. Por exemplo, você pode considerar strings e somar os valores ordinais dos caracteres individuais nelas:

```python
>>> def hash_function(text):
...     return sum(ord(character) for character in text)
```

Você itera sobre o texto usando uma expressão geradora, converte cada caractere individual no ponto de código Unicode correspondente com a função ord() embutida e, finalmente, soma os valores ordinais. Isso fornecerá um único número para qualquer texto fornecido como argumento:

```python
>>> hash_function("Lorem")
511

>>> hash_function("Loren")
512

>>> hash_function("Loner")
512
```

Imediatamente, você notará alguns problemas com esta função. Não apenas ela é específica para strings, mas também sofre de uma distribuição pobre de códigos de hash, que tendem a formar aglomerados em valores de entrada semelhantes. Uma leve mudança na entrada tem pouco efeito na saída observada. Ainda pior, a função permanece insensível à ordem dos caracteres no texto, o que significa que anagramas da mesma palavra, como Loren e Loner, levam a uma colisão de códigos de hash.

Para corrigir o primeiro problema, tente converter a entrada para uma string com uma chamada para str(). Agora, sua função será capaz de lidar com qualquer tipo de argumento:

```python
>>> def hash_function(key):
...     return sum(ord(character) for character in str(key))
```

```python
>>> hash_function("Lorem")
511

>>> hash_function(3.14)
198

>>> hash_function(True)
416
```

Você pode chamar hash_function() com um argumento de qualquer tipo de dado, incluindo uma string, um número de ponto flutuante ou um valor booleano.

Observe que esta implementação será tão boa quanto a representação de string correspondente. Alguns objetos podem não ter uma representação textual adequada para o código acima. Em particular, instâncias de classes personalizadas sem os métodos especiais .__str__() e .__repr__() devidamente implementados são um bom exemplo. Além disso, você não será capaz de distinguir entre diferentes tipos de dados:

```python
>>> hash_function("3.14")
198

>>> hash_function(3.14)
198
```

Na realidade, você gostaria de tratar a string "3.14" e o número de ponto flutuante 3.14 como objetos distintos com códigos de hash diferentes. Uma maneira de mitigar isso seria trocar str() por repr(), que envolve a representação das strings com apóstrofos adicionais ('):

```python
>>> repr("3.14")
"'3.14'"

>>> repr(3.14)
'3.14'
```

Isso melhorará sua função de hash em certa medida:

```python
>>> def hash_function(key):
...     return sum(ord(character) for character in repr(key))
```

```python
>>> hash_function("3.14")
276

>>> hash_function(3.14)
198
```

As strings agora são distinguíveis dos números. Para lidar com o problema dos anagramas, como Loren e Loner, você pode modificar sua função de hash levando em consideração o valor do caractere, bem como sua posição dentro do texto:

```python
>>> def hash_function(key):
...     return sum(
...         index * ord(character)
...         for index, character in enumerate(repr(key), start=1)
...     )
```

Aqui, você soma os produtos derivados da multiplicação dos valores ordinais dos caracteres e seus índices correspondentes. Observe que você enumera os índices a partir de um em vez de zero. Caso contrário, o primeiro caractere seria sempre descartado, pois o valor seria multiplicado por zero.

Agora sua função de hash é bastante universal e não causa tantas colisões quanto antes, mas sua saída pode crescer arbitrariamente grande porque quanto maior a string, maior o código de hash. Além disso, ela é bastante lenta para entradas maiores:

```python
>>> hash_function("Tiny")
1801

>>> hash_function("This has a somewhat medium length.")
60919

>>> hash_function("This is very long and slow!" * 1_000_000)
33304504435500117
```

Você sempre pode lidar com o crescimento ilimitado tomando o módulo (%) do seu código de hash em relação a um tamanho máximo conhecido, como cem:

```python
>>> hash_function("Tiny") % 100
1

>>> hash_function("This has a somewhat medium length.") % 100
19

>>> hash_function("This is very long and slow!" * 1_000_000) % 100
17
```

Lembre-se de que escolher um pool menor de códigos de hash aumenta a probabilidade de colisões de códigos de hash. Se você não conhece o número de seus valores de entrada antecipadamente, é melhor deixar essa decisão para depois, se possível. Você também pode impor um limite aos seus códigos de hash assumindo um valor máximo razoável, como sys.maxsize, que representa o maior valor de inteiros suportado nativamente no Python.

Ignorando a lentidão da função por um momento, você notará outro problema peculiar com sua função de hash. Isso resulta em uma distribuição subótima de códigos de hash por meio de agrupamentos e não aproveita todos os slots disponíveis:

```python
>>> from hash_distribution import plot, distribute
>>> from string import printable

>>> plot(distribute(printable, 6, hash_function))
  0 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   (31)
  1 ■■■■                              (4)
  2 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■   (31)
  4 ■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■■ (33)
  5 ■                                 (1)
```

A distribuição é desigual. Além disso, existem seis contêineres disponíveis, mas um está ausente no histograma. Esse problema decorre do fato de que os dois apóstrofos adicionados por repr() fazem com que praticamente todas as chaves neste exemplo resultem em um número de hash par. Isso pode ser evitado removendo o apóstrofo à esquerda, se existir:

```python
>>> hash_function("a"), hash_function("b"), hash_function("c")
(350, 352, 354)

>>> def hash_function(key):
...     return sum(
...         index * ord(character)
...         for index, character in enumerate(repr(key).lstrip("'"), 1)
...     )

>>> hash_function("a"), hash_function("b"), hash_function("c")
(175, 176, 177)

>>> plot(distribute(printable, 6, hash_function))
  0 ■■■■

■■■■■■■■■■■■■■■■   (16)
  1 ■■■■■■■■■■■■■■■■   (16)
  2 ■■■■■■■■■■■■■■■    (15)
  3 ■■■■■■■■■■■■■■■■■■ (18)
  4 ■■■■■■■■■■■■■■■■■  (17)
  5 ■■■■■■■■■■■■■■■■■■ (18)
```

A chamada para str.lstrip() afetará uma string apenas se ela começar com o prefixo especificado para remover.

Naturalmente, você pode continuar aprimorando ainda mais sua função de hash. Se você estiver curioso sobre a implementação de hash() para strings e sequências de bytes em Python, atualmente usa o algoritmo SipHash, que pode recorrer a uma versão modificada do FNV se o primeiro não estiver disponível. Para descobrir qual algoritmo de hash seu interpretador Python está usando, recorra ao módulo sys:

```python
>>> import sys
>>> sys.hash_info.algorithm
'siphash24'
```

Neste ponto, você tem uma compreensão bastante boa da função de hash, como ela deve funcionar e quais desafios você pode enfrentar ao implementá-la. Nas próximas seções, você usará uma função de hash para construir uma tabela de hash. A escolha de um algoritmo de hash específico influenciará o desempenho da tabela de hash. Com esse conhecimento como sua base, você pode ficar à vontade para continuar usando a função de hash embutida hash().

Construa um Protótipo de Tabela de Hash em Python com TDD

Nesta seção, você vai criar uma classe personalizada representando a estrutura de dados da tabela de hash. Ela não será apoiada por um dicionário Python, para que você possa construir uma tabela de hash do zero e praticar o que aprendeu até agora. Ao mesmo tempo, você modelará sua implementação seguindo o dicionário embutido, imitando suas características mais essenciais.

Observação: Este é apenas um lembrete rápido de que implementar uma tabela de hash é apenas um exercício e uma ferramenta educacional para ensinar sobre os problemas que essa estrutura de dados resolve. Assim como codificar uma função de hash personalizada antes, uma implementação de tabela de hash puramente em Python não tem uso prático em aplicativos da vida real.

Aqui está uma lista dos requisitos de alto nível para a sua tabela de hash, que você estará implementando agora. No final desta seção, sua tabela de hash exibirá os seguintes recursos principais. Ela permitirá que você:

- Crie uma tabela de hash vazia
- Insira um par chave-valor na tabela de hash
- Exclua um par chave-valor da tabela de hash
- Encontre um valor pela chave na tabela de hash
- Atualize o valor associado a uma chave existente
- Verifique se a tabela de hash possui uma determinada chave

Além disso, você implementará algumas características não essenciais, mas ainda úteis. Especificamente, você deve ser capaz de:

- Criar uma tabela de hash a partir de um dicionário Python
- Criar uma cópia rasa de uma tabela de hash existente
- Retornar um valor padrão se a chave correspondente não for encontrada
- Relatar o número de pares chave-valor armazenados na tabela de hash
- Retornar as chaves, valores e pares chave-valor
- Tornar a tabela de hash iterável
- Tornar a tabela de hash comparável usando o operador de teste de igualdade
- Mostrar uma representação textual da tabela de hash

Ao implementar esses recursos, você exercitará ativamente o desenvolvimento orientado por testes, adicionando gradualmente mais recursos à sua tabela de hash. Observe que seu protótipo cobrirá apenas o básico. Você aprenderá como lidar com casos mais avançados um pouco mais tarde neste tutorial. Em particular, esta seção não abordará como:

- Resolver colisões de código de hash
- Manter a ordem de inserção
- Redimensionar dinamicamente a tabela de hash
- Calcular o fator de carga

Sinta-se à vontade para usar os materiais suplementares como pontos de verificação de controle se você ficar preso ou se quiser pular algumas etapas intermediárias de refatoração. Cada subseção termina com um estágio de implementação completo e os testes correspondentes, a partir dos quais você pode começar. Pegue o seguinte link e faça o download dos materiais de apoio com o código-fonte completo e as etapas intermediárias usadas neste tutorial:

Código-fonte: Clique aqui para baixar o código-fonte que você usará para construir uma tabela de hash em Python.

Faça um Curso Intensivo em Desenvolvimento Orientado por Testes

Agora que você conhece as propriedades de alto nível de uma função de hash e seu propósito, pode exercitar uma abordagem de desenvolvimento orientado por testes para construir uma tabela de hash. Se você nunca tentou essa técnica de programação antes, ela se resume a três etapas que você tende a repetir em um ciclo:

🟥 Vermelho: Pense em um único caso de teste e automatize-o usando um framework de teste de unidade de sua escolha. Seu teste falhará neste ponto, mas tudo bem. Os executadores de teste geralmente indicam um teste com falha com a cor vermelha, daí o nome dessa fase de ciclo.
🟩 Verde: Implemente o mínimo necessário para fazer seu teste passar, mas apenas isso! Isso garantirá uma cobertura de código mais alta e economizará você de escrever código redundante. O relatório de teste ficará verde de forma satisfatória depois.
♻️ Refatorar: Opcionalmente, modifique seu código sem alterar seu comportamento, desde que todos os casos de teste ainda passem. Você pode usar isso como uma oportunidade para remover duplicação e melhorar a legibilidade do seu código.

O Python vem com o pacote unittest embutido, mas a biblioteca pytest de terceiros tem uma curva de aprendizado, sem dúvida, mais suave, então você usará isso neste tutorial. Vá em frente e instale o pytest em seu ambiente virtual agora:

```bash
(venv) C:\> python -m pip install pytest
```

Lembre-se de que você pode verificar cada estágio de implementação em vários pontos de controle. Em seguida, crie um arquivo chamado `test_hashtable.py` e defina uma função de teste fictícia nele para verificar se o pytest a reconhecerá:

```python
# test_hashtable.py

def test_should_always_pass():
    assert 2 + 2 == 22, "This is just a dummy test"
```

O framework aproveita a instrução assert embutida para executar seus testes e relatar seus resultados. Isso significa que você pode usar a sintaxe regular do Python, sem importar nenhuma API específica até ser absolutamente necessário. Ele também detecta arquivos de teste e funções de teste, contanto que seus nomes comecem com o prefixo de teste.

A instrução assert recebe uma expressão booleana como argumento, seguida por uma mensagem de erro opcional. Quando a condição é avaliada como True, então nada acontece, como se não houvesse nenhuma assertiva. Caso contrário, o Python levantará uma AssertionError e exibirá a mensagem no fluxo de erro padrão (stderr). Enquanto isso, o pytest intercepta erros de assertiva e constrói um relatório em torno deles.

Agora, abra o terminal, altere seu diretório de trabalho para onde você salvou aquele arquivo de teste e execute o comando pytest sem argumentos. Sua saída deve se parecer com isso:

- No Windows:
```bash
(venv) C:\> python -m pytest
=========================== test session starts ===========================
platform win32 -- Python 3.10.2, pytest-6.2.5, pluggy-1.0.0
rootdir: C:\Users\realpython\hashtable
collected 1 item

test_hashtable.py F                                                 [100%]

================================ FAILURES =================================
_________________________ test_should_always_pass _________________________

    def test_should_always_pass():
>       assert 2 + 2 == 22, "This is just a dummy test"
E       AssertionError: This is just a dummy test
E       assert (2 + 2) == 22

test_hashtable.py:4: AssertionError
========================= short test summary info =========================
FAILED test_hashtable.py::test_should_always_pass - AssertionError: This...
============================ 1 failed in 0.03s ============================
```

- No Linux + macOS:
```bash
(venv) $ python -m pytest
=========================== test session starts ===========================
platform win32 -- Python 3.10.2, pytest-6.2.5, pluggy-1.0.0
rootdir: C:\Users\realpython\hashtable
collected 1 item

test_hashtable.py F                                                 [100%]

================================ FAILURES =================================
_________________________ test_should_always_pass _________________________

    def test_should_always_pass():
>       assert 2 + 2 == 22, "This is just a dummy test"
E       AssertionError: This is just a dummy test
E       assert (2 + 2) == 22

test_hashtable.py:4: AssertionError
========================= short test summary info =========================
FAILED test_hashtable.py::test_should_always_pass - AssertionError: This...
============================ 1 failed in 0.03s ============================
```

Ops! Há uma falha no seu teste. Para encontrar a causa raiz, aumente a verbosidade da saída do pytest anexando a flag -v ao comando. Agora você pode identificar onde está o problema:

```bash
(venv) C:\> python -m pytest -v
=========================== test session starts ===========================
platform win32 -- Python 3.10.2, pytest-6.2.5, pluggy-1.0.0
rootdir: C:\Users\realpython\hashtable
collected 1 item

test_hashtable.py::test_should_always_pass FAILED                 [100%]

==================================== FAILURES =====================================
_________________________ test_should_always_pass __________________________

    def test_should_always_pass():
>       assert 2 + 2 == 22, "This is just a dummy test"
E       AssertionError: This is just a dummy test
E       assert (2 + 2) == 22

test_hashtable.py:4: AssertionError
========================= short test summary info =========================
FAILED test_hashtable.py::test_should_always_pass - AssertionError: This...
============================ 1 failed in 0.03s ============================
```

A saída mostra quais foram os valores real e esperado para a asserção que falhou. Neste caso, somar dois mais dois resulta em quatro, em vez de vinte e dois. Você pode corrigir o código corrigindo o valor esperado:

```python
# test_hashtable.py

def test_should_always_pass():
    assert 2 + 2 == 4, "This is just a dummy test"
```

Quando você executar pytest novamente, não deve haver mais falhas nos testes:

- No Windows:
```bash
(venv) C:\> python -m pytest
=========================== test session starts ===========================
platform win32 -- Python 3.10.2, pytest-6.2.5, pluggy-1.0.0
rootdir: C:\Users\realpython\hashtable
collected 1 item

test_hashtable.py .                                                 [100%]

============================ 1 passed in 0.00s ============================
```

- No Linux + macOS:
```bash
(venv) $ python -m pytest
=========================== test session starts ===========================
platform win32 -- Python 3.10.2, pytest-6.2.5, pluggy-1.0.0
rootdir: C:\Users\realpython\hashtable
collected 1 item

test_hashtable.py .                                                 [100%]

============================ 1 passed in 0.00s ============================
```

Isso é tudo! Você acabou de aprender os passos essenciais para automatizar casos de teste para a implementação da sua tabela de hash. Naturalmente, você pode usar um IDE como o PyCharm ou um editor como o VS Code que se integra a frameworks de teste se isso for mais conveniente para você. Em seguida, você vai colocar esse novo conhecimento em prática.

Lembre-se de seguir o ciclo vermelho-verde-refatorar descrito anteriormente. Portanto, você deve começar identificando seu primeiro caso de teste. Por exemplo, você deve ser capaz de instanciar uma nova tabela de hash chamando a hipotética classe HashTable importada do módulo hashtable. Essa chamada deve retornar um objeto não vazio:

```python
# test_hashtable.py

from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable() is not None
```

Neste ponto, seu teste se recusará a ser executado por causa de uma declaração de importação não satisfeita no topo do arquivo. Afinal, você está na fase vermelha. A fase vermelha é o único momento em que você pode adicionar novos recursos, então crie outro módulo chamado hashtable.py e coloque a definição da classe HashTable nele:

```python
# hashtable.py

class HashTable:
    pass
```

É um espaço reservado de classe básico, mas deve ser o suficiente para fazer seu teste passar. A propósito, se você estiver usando um editor de código, poderá dividir convenientemente a visualização em colunas, exibindo o código em teste e os testes correspondentes lado a lado.

Uma vez que a execução do pytest tenha êxito, você pode começar a pensar em outro caso de teste, já que há praticamente nada para refatorar ainda. Por exemplo, uma tabela de hash básica deve conter uma sequência de valores. Nesta fase inicial, você pode assumir que a sequência tem um tamanho fixo estabelecido no momento da criação da tabela de hash. Modifique seu caso de teste existente conforme necessário:

```python
# test_hashtable.py

from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(size=100) is not None
```

Você especifica o tamanho usando um argumento de palavra-chave. No entanto, antes de adicionar novo código à classe HashTable, execute seus testes novamente para confirmar que você entrou na fase vermelha novamente. Presenciar um teste falhando pode ser inestimável. Quando você implementar uma parte do código mais tarde, saberá se ela atende a um grupo específico de testes ou se eles permanecem inalterados. Caso contrário, seus testes podem mentir para você, verificando algo diferente do que você pensou!

Após confirmar que você está na fase vermelha, declare o método .__init__() na classe HashTable com a assinatura esperada, mas não implemente seu corpo:

```python
# hashtable.py

class HashTable:
    def __init__(self, size):
        pass
```

Boom! Você está de volta à fase verde mais uma vez, então que tal um pouco de refatoração desta vez? Por exemplo, você pode renomear o argumento size para capacity se isso for mais descritivo para você. Não se esqueça de alterar o caso de teste primeiro, depois execute o pytest e sempre atualize o código em teste como última etapa:

```python
# hashtable.py

class HashTable:
    def __init__(self, capacity):
        pass
```

Como você pode ver, o ciclo vermelho-verde-refatorar consiste em estágios breves, geralmente durando no máximo alguns segundos cada um. Então, por que você não continua adicionando mais casos de teste? Seria bom se sua estrutura de dados pudesse relatar a capacidade da tabela de hash usando a função len() embutida do Python. Adicione outro caso de teste e observe como ele falha miseravelmente:

```python
# test_hashtable.py

from hashtable import HashTable

def test_should_create_hashtable():
    assert HashTable(capacity=100) is not None

def test_should_report_capacity():
    assert len(HashTable(capacity=100)) == 100
```

Para lidar corretamente com len(), você deve implementar o método especial .__len__() em sua classe e lembrar da capacidade fornecida através do inicializador da classe:

```python
# hashtable.py

class HashTable:
    def __init__(self, capacity):
        self.capacity = capacity

    def __len__(self):
        return self.capacity
```

Você pode pensar que o TDD não está levando você na direção certa. Isso não é como você pode ter imaginado a implementação da tabela de hash. Onde está a sequência de valores com a qual você começou no início? Infelizmente, dar pequenos passos e fazer muitas correções de curso ao longo do caminho é algo que o desenvolvimento orientado a testes recebe muitas críticas. Portanto, pode não ser apropriado para projetos que envolvem muita experimentação.

Por outro lado, implementar uma estrutura de dados bem conhecida, como uma tabela de hash, é uma aplicação perfeita desta metodologia de desenvolvimento de software. Você tem expectativas claras que são fáceis de codificar como casos de teste. Em breve, você verá por si mesmo que dar o próximo passo levará a uma leve mudança na implementação. Não se preocupe com isso, porque aperfeiçoar o código em si é menos importante do que fazer seus casos de teste passarem.

À medida que você adiciona mais restrições por meio dos casos de teste, frequentemente é necessário repensar sua implementação. Por exemplo, uma nova tabela de hash provavelmente deve começar com espaços vazios para os valores armazenados:

```python
# test_hashtable.py

# ...

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [None, None, None]
```

Em outras palavras, uma nova tabela de hash deve expor um atributo .values com o comprimento solicitado e preenchido com os elementos None. A propósito, é comum usar nomes de função tão verbosos porque eles aparecerão em seu relatório de teste. Quanto mais legíveis e descritivos forem seus testes, mais rapidamente você descobrirá qual parte precisa ser corrigida.

Nota: Como regra geral, seus casos de teste devem ser o mais independentes e atômicos possível, o que geralmente significa usar apenas uma afirmação por função. No entanto, seus cenários de teste às vezes podem precisar de um pouco de configuração ou limpeza. Eles também podem envolver alguns passos. Nesses casos, é comum estruturar sua função em torno da chamada convenção dado-quando-então:

```python
def test_should_create_empty_value_slots():
    # Dado
    expected_values = [None, None, None]
    hash_table = HashTable(capacity=3)

    # Quando
    actual_values = hash_table.values

    # Então
    assert actual_values == expected_values
```

A parte "Dado" descreve o estado inicial e as condições prévias para o seu caso de teste, enquanto "Quando" representa a ação do seu código em teste, e "Então" é responsável por afirmar o resultado resultante.

Esta é uma das muitas maneiras possíveis de atender aos seus testes existentes:

```python
# hashtable.py

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]

    def __len__(self):
        return len(self.values)
```

Você substitui o atributo .capacity por uma lista do comprimento solicitado contendo apenas elementos None. Multiplicar um número por uma lista ou vice-versa é uma maneira rápida de preencher essa lista com o valor ou valores fornecidos. Além disso, você atualiza o método especial .__len__() para que todos os testes passem.

Nota: Um dicionário Python tem um comprimento correspondente ao número real de pares chave-valor armazenados, em vez de sua capacidade interna. Você alcançará um efeito semelhante em breve.

Agora que você está familiarizado com o TDD, é hora de aprofundar e adicionar as demais características à sua tabela de hash.

Inserir um Par Chave-Valor

Agora que você pode criar uma tabela de hash, é hora de dar a ela algumas capacidades de armazenamento. A tabela de hash tradicional é suportada por uma matriz capaz de armazenar apenas um tipo de dado. Devido a isso, implementações de tabelas de hash em muitas linguagens, como Java, exigem que você declare o tipo de suas chaves e valores antecipadamente:

```java
Map<String, Integer> phonesByNames = new HashMap<>();
```

Esta tabela de hash específica mapeia strings para inteiros, por exemplo. No entanto, como arrays não são nativos do Python, você continuará usando uma lista. Como efeito colateral, sua tabela de hash poderá aceitar tipos de dados arbitrários tanto para as chaves quanto para os valores, assim como o dicionário do Python.

Nota: O Python possui uma coleção eficiente de arrays, mas ela é destinada apenas a valores numéricos. Às vezes, pode ser conveniente para processar dados binários brutos.

Agora, adicione mais um caso de teste para inserir pares chave-valor em sua tabela de hash usando a conhecida sintaxe de colchetes:

```python
# test_hashtable.py

# ...

def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values
```

Primeiro, você cria uma tabela de hash com cem espaços vazios e, em seguida, a preenche com três pares de chaves e valores de vários tipos, incluindo strings, números de ponto flutuante e booleanos. Finalmente, você verifica se a tabela de hash contém os valores esperados em qualquer ordem. Observe que sua tabela de hash apenas lembra os valores, mas não as chaves associadas no momento!

A implementação mais direta e talvez um pouco ingênua que satisfaria este teste é a seguinte:

```python
# hashtable.py

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        self.values.append(value)
```

Ela ignora completamente a chave e simplesmente adiciona o valor à extrema direita da lista, aumentando seu comprimento. Você pode muito bem pensar imediatamente em outro caso de teste. Inserir elementos na tabela de hash não deve aumentar seu tamanho. Da mesma forma, remover um elemento não deve diminuir a tabela de hash, mas você apenas faz uma anotação mental disso, pois ainda não há capacidade de remover pares chave-valor.

Nota: Você também poderia escrever um teste de marcador de posição e dizer ao pytest para ignorá-lo incondicionalmente até mais tarde:

```python
import pytest

@pytest.mark.skip
def test_should_not_shrink_when_removing_elements():
    pass
```

Ele utiliza um dos decoradores fornecidos pelo pytest.

No mundo real, você gostaria de criar casos de teste separados com nomes descritivos dedicados a testar esses comportamentos. No entanto, como este é apenas um tutorial, você vai adicionar uma nova asserção à função existente por brevidade:

```python
# test_hashtable.py

# ...

def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert "hello" in hash_table.values
    assert 37 in hash_table.values
    assert True in hash_table.values

    assert len(hash_table) == 100
```

Agora você está na fase vermelha, então reescreva seu método especial para manter a capacidade fixa o tempo todo:

```python
# hashtable.py

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [None]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)
        self.values[index] = value
```

Você transforma uma chave arbitrária em um valor de hash numérico e usa o operador módulo para restringir o índice resultante dentro do espaço de endereçamento disponível. Ótimo! Seu relatório de teste acende novamente na cor verde.

Nota: O código acima depende da função de hash embutida do Python, que tem um elemento de aleatoriedade, como você já aprendeu. Portanto, seu teste pode falhar em casos raros quando duas chaves acabam produzindo um código de hash idêntico por coincidência. Como você lidará com colisões de códigos de hash mais tarde, pode desativar a randomização de hash ou usar uma semente previsível ao executar o pytest temporariamente:

    Windows
    Linux + macOS

(venv) C:\> set PYTHONHASHSEED=128
(venv) C:\> python -m pytest

Certifique-se de escolher uma semente de hash que não cause colisões em seus dados de amostra. Encontrar uma pode envolver um pouco de tentativa e erro. No meu caso, o valor 128 parecia funcionar bem.

Mas você consegue pensar em alguns casos extremos, talvez? E quanto à inserção de None em sua tabela de hash? Isso criaria um conflito entre um valor legítimo e o valor sentinela designado que você escolheu para indicar espaços em branco em sua tabela de hash. Você vai querer evitar isso.

Como sempre, comece escrevendo um caso de teste para

Mas você consegue pensar em alguns casos extremos, talvez? E quanto à inserção de `None` em sua tabela de hash? Isso criaria um conflito entre um valor legítimo e o valor sentinela designado que você escolheu para indicar espaços em branco em sua tabela de hash. Você vai querer evitar isso.

Como sempre, comece escrevendo um caso de teste para expressar o comportamento desejado:

```python
# test_hashtable.py

# ...

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values
```

Uma maneira de contornar isso seria substituir `None` em seu método `.__init__()` por outro valor único que os usuários provavelmente não inserirão. Por exemplo, você poderia definir uma constante especial criando um objeto completamente novo para representar espaços em branco em sua tabela de hash:

```python
# hashtable.py

BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]

    # ...
```

Você só precisa de uma única instância em branco para marcar os espaços como vazios. Naturalmente, você precisará atualizar um caso de teste mais antigo para voltar à fase verde:

```python
# test_hashtable.py

from hashtable import HashTable, BLANK

# ...

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3).values == [BLANK, BLANK, BLANK]

# ...
```

Em seguida, escreva um caso de teste positivo exercendo o caminho principal para lidar com a inserção de um valor `None`:

```python
def test_should_insert_none_value():
    hash_table = HashTable(capacity=100)
    hash_table["key"] = None
    assert None in hash_table.values
```

Você cria uma tabela de hash vazia com cem espaços e insere `None` associado a alguma chave arbitrária. Isso deverá funcionar perfeitamente se você estiver seguindo de perto as etapas até agora. Se não, olhe para as mensagens de erro, pois muitas vezes contêm pistas sobre o que deu errado. Alternativamente, verifique o código de exemplo disponível para download neste link:

Código Fonte: Clique aqui para baixar o código-fonte que você usará para construir uma tabela de hash em Python.

Na próxima subseção, você adicionará a capacidade de recuperar valores por suas chaves associadas.

Encontrar um Valor por Chave

Para recuperar um valor da tabela de hash, você desejará aproveitar a mesma sintaxe de colchetes como antes, mas sem usar a instrução de atribuição. Você também precisará de uma tabela de hash de exemplo. Para evitar duplicar o mesmo código de configuração em cada caso de teste individual em seu conjunto de testes, você pode encapsulá-lo em um fixture de teste fornecido pelo pytest:

```python
# test_hashtable.py

import pytest

# ...

@pytest.fixture
def hash_table():
    sample_data = HashTable(capacity=100)
    sample_data["hola"] = "hello"
    sample_data[98.6] = 37
    sample_data[False] = True
    return sample_data

def test_should_find_value_by_key(hash_table):
    assert hash_table["hola"] == "hello"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
```

Um fixture de teste é uma função anotada com o decorador @pytest.fixture. Ele retorna dados de exemplo para seus casos de teste, como uma tabela de hash populada com chaves e valores conhecidos. Seu pytest chamará automaticamente essa função para você e injetará seu resultado em qualquer função de teste que declare um argumento com o mesmo nome que seu fixture. Neste caso, a função de teste espera um argumento `hash_table`, que corresponde ao nome do seu fixture.

Para ser capaz de encontrar valores por chave, você pode implementar a busca de elementos por meio de outro método especial chamado `.__getitem__()` em sua classe `HashTable`:

```python
# hashtable.py

BLANK = object()

class HashTable:
    def __init__(self, capacity):
        self.values = capacity * [BLANK]

    def __len__(self):
        return len(self.values)

    def __setitem__(self, key, value):
        index = hash(key) % len(self)
        self.values[index] = value

    def __getitem__(self, key):
        index = hash(key) % len(self)
        return self.values[index]
```

Você calcula o índice de um elemento com base no código de hash da chave fornecida e retorna o que estiver sob esse índice. Mas e quanto às chaves ausentes? Até agora, você pode retornar uma instância em branco quando uma determinada chave ainda não foi usada, um resultado que não é muito útil. Para replicar como um dict do Python funcionaria nesse caso, você deve levantar uma exceção `KeyError`:

```python
# test_hashtable.py

# ...

def test_should_raise_error_on_missing_key():
    hash_table = HashTable(capacity=100)
    with pytest.raises(KeyError) as exception_info:
        hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"
```

Você cria uma tabela de hash vazia e tenta acessar um de seus valores por meio de uma chave ausente. O framework pytest inclui uma construção especial para testar exceções. Acima, você usa o gerenciador de contexto `pytest.raises` para esperar por um tipo específico de exceção dentro do bloco de código seguinte. Lidar com esse caso envolve adicionar uma instrução condicional ao seu método de acesso:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __getitem__(self, key):
        index = hash(key) % len(self)
        value = self.values[index]
        if value is BLANK:
            raise KeyError(key)
        return value
```

Se o valor no índice fornecido estiver em branco, você levanta a exceção. A propósito, você usa o operador `is` em vez do operador de teste de igualdade (`==`) para garantir que você está comparando as identidades e não os valores. Embora a implementação padrão do teste de igualdade em classes personalizadas recaia na comparação das identidades de suas instâncias, a maioria dos tipos de dados incorporados distingue entre os dois operadores e os implementa de maneira diferente.

Como agora você pode determinar se uma determinada chave tem um valor associado em sua tabela de hash, pode muito bem implementar o operador `in` para imitar um dicionário do Python. Lembre-se de escrever e cobrir esses casos de teste individualmente para respeitar os princípios do desenvolvimento orientado a testes:

```python
# test_hashtable.py

# ...

def test_should_find_key(hash_table):
    assert "hola" in hash_table

def test_should_not_find_key(hash_table):
    assert "missing_key" not in hash_table
```

Ambos os casos de teste aproveitam o fixture de teste que você preparou anteriormente e verificam o método especial `.__contains__()`, que você pode implementar da seguinte maneira:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True
```

Ao acessar a chave fornecida, se uma exceção `KeyError` for gerada, você a intercepta e retorna `False` para indicar uma chave ausente. Caso contrário, você combina o bloco try...except com uma cláusula else e retorna `True`. O tratamento de exceções é ótimo, mas às vezes pode ser inconveniente, é por isso que `dict.get()` permite que você especifique um valor padrão opcional. Você pode replicar o mesmo comportamento em sua tabela de hash personalizada:

```python
# test_hashtable.py

# ...

def test_should_get_value(hash_table):
    assert hash_table.get("hola") == "hello"

def test_should_get_none_when_missing_key(hash_table):
    assert hash_table.get("missing_key") is None

def test_should_get_default_value_when_missing_key(hash_table):
    assert hash_table.get("missing_key", "default") == "default"

def test_should_get_value_with_default(hash_table):
    assert hash_table.get("hola", "default") == "hello"
```

O código de `.get()` se parece com o método especial que você acabou de implementar:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default
```

Você tenta retornar o valor correspondente à chave fornecida. Em caso de exceção, você retorna o valor padrão, que é um argumento opcional. Quando o usuário deixa de especificá-lo, ele é igual a `None`.

Para completar, você adicionará a capacidade de excluir um par chave-valor de sua tabela de hash na próxima subseção.

Excluir um Par Chave-Valor

Dicionários em Python permitem que você exclua pares chave-valor previamente inseridos usando a palavra-chave integrada `del`, que remove informações tanto sobre a chave quanto sobre o valor. Veja como isso poderia funcionar com sua tabela de hash:

```python
# test_hashtable.py

# ...

def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert "hello" in hash_table.values

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert "hello" not in hash_table.values
```

Primeiro, você verifica se a tabela de hash de exemplo possui a chave e o valor desejados. Em seguida, você exclui ambos indicando apenas a chave e repete as asserções, mas com expectativas invertidas. Você pode fazer este teste passar da seguinte maneira:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __delitem__(self, key):
        index = hash(key) % len(self)
        del self.values[index]
```

Você calcula o índice associado a uma chave e remove o valor correspondente da lista incondicionalmente. No entanto, você se lembra imediatamente da sua nota mental anterior sobre afirmar que sua tabela de hash não deve encolher quando você exclui elementos dela. Portanto, você adiciona mais duas asserções:

```python
# test_hashtable.py

# ...

def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert "hello" in hash_table.values
    assert len(hash_table) == 100

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert "hello" not in hash_table.values
    assert len(hash_table) == 100
```

Isso garantirá que o tamanho da lista subjacente da sua tabela de hash permaneça inalterado. Agora, você precisa atualizar seu código para marcar um slot como em branco em vez de descartá-lo completamente:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __delitem__(self, key):
        index = hash(key) % len(self)
        self.values[index] = BLANK
```

Considerando que você está novamente na fase verde, pode aproveitar essa oportunidade para passar algum tempo refatorando. A mesma fórmula de índice aparece três vezes em lugares diferentes. Você pode extrair e simplificar o código:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __delitem__(self, key):
        self.values[self._index(key)] = BLANK

    def __setitem__(self, key, value):
        self.values[self._index(key)] = value

    def __getitem__(self, key):
        value = self.values[self._index(key)]
        if value is BLANK:
            raise KeyError(key)
        return value

    # ...

    def _index(self, key):
        return hash(key) % len(self)
```

De repente, após aplicar apenas esta pequena modificação, um padrão surge. Excluir um item é equivalente a inserir um objeto em branco. Portanto, você pode reescrever sua rotina de exclusão para tirar proveito do método mutador:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __delitem__(self, key):
        self[key] = BLANK

    # ...
```

Atribuir um valor por meio da sintaxe de colchetes delega para o método `.__setitem__()`. Tudo bem, isso é refatoração suficiente por enquanto. É muito mais importante pensar em outros casos de teste neste momento. Por exemplo, o que acontece quando você solicita excluir uma chave ausente? O dict do Python levanta uma exceção `KeyError` nesse caso, então você pode fazer o mesmo:

```python
# hashtable.py

# ...

def test_should_raise_key_error_when_deleting(hash_table):
    with pytest.raises(KeyError) as exception_info:
        del hash_table["missing_key"]
    assert exception_info.value.args[0] == "missing_key"
```

Cobrir este caso de teste é relativamente direto, pois você pode confiar no código que você escreveu ao implementar o operador `in`:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __delitem__(self, key):
        if key in self:
            self[key] = BLANK
        else:
            raise KeyError(key)

    # ...
```

Se você encontrar a chave em sua tabela de hash, você sobrescreve o valor associado com o valor sentinela para remover esse par. Caso contrário, você levanta uma exceção. Tudo bem, há mais uma operação básica de tabela de hash a ser coberta, o que você fará em seguida.

Atualizar o Valor de um Par Existente

O método de inserção já deve cuidar da atualização de um par chave-valor, então você apenas vai adicionar um caso de teste relevante e verificar se ele funciona conforme o esperado:

```python
# test_hashtable.py

# ...

def test_should_update_value(hash_table):
    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 100
```

Depois de modificar o valor, "hello", de uma chave existente e alterá-lo para "hallo", você também verifica se outros pares chave-valor, assim como o comprimento da tabela de hash, permanecem inalterados. Isso é tudo. Você já tem uma implementação básica de tabela de hash, mas ainda faltam algumas características extras que são relativamente simples de implementar.

Obter os Pares Chave-Valor

É hora de abordar a questão central. Os dicionários em Python permitem que você itere sobre suas chaves, valores ou pares chave-valor chamados de itens. No entanto, sua tabela de hash é realmente apenas uma lista de valores com indexação especial por cima. Se você quisesse recuperar as chaves originais inseridas em sua tabela de hash, não teria sorte, porque a implementação atual da tabela de hash não se lembrará delas.

Nesta subseção, você vai refatorar sua tabela de hash intensamente para adicionar a capacidade de reter chaves e valores. Tenha em mente que haverá várias etapas envolvidas, e muitos testes começarão a falhar como resultado disso. Se você quiser pular essas etapas intermediárias e ver o efeito, pule para a cópia defensiva.

Espere um minuto. Você continua lendo sobre pares chave-valor neste tutorial, então por que não substituir os valores por tuplas? Afinal, as tuplas são diretas em Python. Melhor ainda, você poderia usar tuplas nomeadas para tirar proveito de sua pesquisa de elementos nomeados. Mas primeiro, você precisa pensar em um caso de teste.

Nota: Lembre-se de focar na funcionalidade de alto nível voltada para o usuário ao elaborar um caso de teste. Não teste um pedaço de código que você pode antecipar com base em sua experiência de programador ou instinto. São os testes que devem impulsionar sua implementação no TDD, não o contrário.

Em primeiro lugar, você vai precisar de outro atributo em sua classe HashTable para armazenar os pares chave-valor:

```python
# test_hashtable.py

# ...

def test_should_return_pairs(hash_table):
    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs
```

A ordem dos pares chave-valor não é importante neste momento, então você pode assumir que eles podem ser obtidos em qualquer ordem sempre que solicitados. No entanto, em vez de introduzir outro campo na classe, você pode reutilizar .values renomeando-o para .pairs e fazendo outros ajustes necessários. Há alguns. Esteja ciente de que isso temporariamente fará com que alguns testes falhem até que você corrija a implementação.

Nota: Se você estiver usando um editor de código, poderá renomear uma variável ou um membro de classe com um único clique de um botão, aproveitando as capacidades de refatoração. No PyCharm, por exemplo, você pode clicar com o botão direito em uma variável, escolher Refatorar no menu de contexto e, em seguida, Renomear.... Ou você pode usar o atalho de teclado correspondente:
PyCharm's Rename Refactor

Essa é a maneira mais direta e confiável de mudar o nome de uma variável em seu projeto. O editor de código atualizará todas as referências da variável em todos os arquivos do seu projeto.

Quando você renomear .values para .pairs em hashtable.py e test_hashtable.py, então você também precisará atualizar o método especial .__setitem__(). Em particular, ele deve armazenar tuplas da chave e do valor associado agora:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __setitem__(self, key, value):
        self.pairs[self._index(key)] = (key, value)
```

Inserir um elemento em sua tabela de hash envolve a chave e o valor em uma tupla e, em seguida, coloca essa tupla no índice desejado em sua lista de pares. Observe que sua lista inicialmente conterá apenas objetos em branco em vez de tuplas, então você estará usando dois tipos de dados diferentes em sua lista de pares. Um é uma tupla, enquanto o outro pode ser qualquer coisa, exceto uma tupla, para denotar um slot em branco.

Devido a isso, você não precisa mais de uma constante de sentinela especial para marcar um slot como vazio. Você pode remover com segurança sua constante BLANK e substituí-la pelo None comum novamente onde necessário, então faça isso agora.

Nota: Remover código pode ser difícil de aceitar no início, mas menos é melhor! Como você pode ver, o desenvolvimento orientado por testes às vezes pode fazer você dar voltas.

Você pode dar mais um passo atrás para retomar o controle sobre a exclusão de um item:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __delitem__(self, key):
        if key in self:
            self.pairs[self._index(key)] = None
        else:
            raise KeyError(key)
```

Infelizmente, o método .__delitem__() não pode mais aproveitar a sintaxe de colchetes porque isso resultaria em envolver o valor de sentinela escolhido desnecessariamente em uma tupla. Você deve usar uma instrução de atribuição explícita aqui para evitar lógica desnecessariamente complicada no futuro.


A última peça importante do quebra-cabeça é atualizar o método .__getitem__():

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __getitem__(self, key):
        pair = self.pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair[1]
```

Você dá uma olhada em um índice, esperando encontrar um par chave-valor. Se não encontrar nada, você levanta uma exceção. Por outro lado, se ver algo interessante, você pega o segundo elemento da tupla no índice um, que corresponde ao valor mapeado. No entanto, você pode escrever isso de maneira mais elegante usando uma tupla nomeada, como sugerido anteriormente:

```python
# hashtable.py

from typing import NamedTuple, Any

class Pair(NamedTuple):
    key: Any
    value: Any

class HashTable:
    # ...

    def __setitem__(self, key, value):
        self.pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self.pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    # ...
```

A classe Pair consiste nos atributos .key e .value, que são livres para receber valores de qualquer tipo de dado. Ao mesmo tempo, sua classe herda todos os comportamentos regulares de uma tupla porque ela estende a classe pai NamedTuple. Observe que você precisa chamar explicitamente Pair() em sua chave e valor no método .__setitem__() para aproveitar o acesso nomeado do atributo em .__getitem__().

Nota: Apesar de usar um tipo de dado personalizado para representar pares chave-valor, você pode escrever seus testes para esperar instâncias de Pair ou tuplas regulares, graças à compatibilidade de ambos os tipos.

Naturalmente, você tem alguns casos de teste para atualizar neste ponto antes que o relatório possa ficar verde novamente. Leve o seu tempo e revise cuidadosamente sua suíte de testes. Alternativamente, consulte o código dos materiais de apoio se estiver se sentindo preso ou dê uma olhada aqui:

```python
# test_hashtable.py

# ...

def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 100

# ...

def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert ("hola", "hello") in hash_table.pairs
    assert len(hash_table) == 100

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert ("hola", "hello") not in hash_table.pairs
    assert len(hash_table) == 100
```

Haverá outro caso de teste que precisa de atenção especial. Especificamente, é sobre verificar se uma tabela de hash vazia não tem valores None quando é criada. Você acabou de substituir uma lista de valores por uma lista de pares. Para recuperar os valores, você pode usar uma compreensão de lista como esta:

```python
# test_hashtable.py

# ...

def test_should_not_contain_none_value_when_created():
    hash_table = HashTable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values
```

Se você estiver preocupado em incluir muita lógica no caso de teste, você está absolutamente certo. Afinal, você quer testar o comportamento da tabela de hash. Mas não se preocupe com isso por enquanto. Você vai revisitar este caso de teste em breve.

Use a Cópia Defensiva

Depois de retornar à fase verde, tente identificar possíveis casos especiais. Por exemplo, os `.pairs` são expostos como um atributo público que qualquer pessoa pode modificar intencional ou acidentalmente. Na prática, os métodos de acesso nunca devem vazar a implementação interna, mas sim criar cópias defensivas para proteger atributos mutáveis de modificações externas:

```python
# test_hashtable.py

# ...

def test_should_return_copy_of_pairs(hash_table):
    assert hash_table.pairs is not hash_table.pairs
```

Sempre que você solicita os pares chave-valor de uma tabela de hash, espera receber um objeto completamente novo com uma identidade única. Você pode esconder um campo privado atrás de uma propriedade em Python, então crie uma e substitua todas as referências a `.pairs` por `._pairs` apenas em sua classe HashTable. O sublinhado na frente é uma convenção de nomenclatura padrão em Python que indica implementação interna:

```python
# hashtable.py

# ...

class HashTable:
    def __init__(self, capacity):
        self._pairs = capacity * [None]

    def __len__(self):
        return len(self._pairs)

    def __delitem__(self, key):
        if key in self:
            self._pairs[self._index(key)] = None
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        self._pairs[self._index(key)] = Pair(key, value)

    def __getitem__(self, key):
        pair = self._pairs[self._index(key)]
        if pair is None:
            raise KeyError(key)
        return pair.value

    def __contains__(self, key):
        try:
            self[key]
        except KeyError:
            return False
        else:
            return True

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    @property
    def pairs(self):
        return self._pairs.copy()

    def _index(self, key):
        return hash(key) % len(self)
```

Quando você solicita uma lista de pares chave-valor armazenados em sua tabela de hash, obterá uma cópia rasa deles toda vez. Como você não terá uma referência para o estado interno da sua tabela de hash, ela permanecerá inalterada por possíveis alterações em sua cópia.

Nota: A ordem dos métodos de classe que você atingiu pode diferir ligeiramente da apresentada no bloco de código acima. Isso é aceitável porque a ordem dos métodos não importa do ponto de vista do Python. No entanto, é costume começar com métodos estáticos ou de classe, seguidos pela interface pública da sua classe, que você é mais propenso a consultar. A implementação interna deve aparecer geralmente no final.

Para evitar ter que pular pelo código, é uma boa ideia organizar os métodos de uma maneira que se assemelhe a uma história. Especificamente, uma função de nível superior deve ser listada antes das funções de nível inferior que são chamadas.

Para mimetizar ainda mais o `dict.items()` em sua propriedade, a lista resultante de pares não deve incluir espaços em branco. Em outras palavras, não deve haver valores `None` nessa lista:

```python
# test_hashtable.py

# ...

def test_should_not_include_blank_pairs(hash_table):
    assert None not in hash_table.pairs
```

Para atender a este teste, você pode filtrar os valores vazios adicionando uma condição à compreensão de lista em sua propriedade:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def pairs(self):
        return [pair for pair in self._pairs if pair]
```

Você não precisa de uma chamada explícita para `.copy()` porque a compreensão de lista cria uma nova lista. Para cada par na lista original dos pares chave-valor, você verifica se aquele par específico é verdadeiro e o mantém na lista resultante. No entanto, isso quebrará dois outros testes que você precisa atualizar agora:

```python
# test_hashtable.py

# ...

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3)._pairs == [None, None, None]

# ...

def test_should_insert_none_value():
    hash_table = HashTable(100)
    hash_table["key"] = None
    assert ("key", None) in hash_table.pairs
```

Isso não é ideal porque um dos seus testes busca a implementação interna em vez de se concentrar nas interfaces públicas. No entanto, esse tipo de teste é conhecido como teste de caixa branca, que tem seu lugar.

Obter as Chaves e Valores

Você se lembra do caso de teste que você modificou adicionando uma compreensão de lista para recuperar os valores de seus pares chave-valor? Bem, aqui está ele novamente se precisar refrescar a memória:

```python
# test_hashtable.py

# ...

def test_should_not_contain_none_value_when_created():
    hash_table = HashTable(capacity=100)
    values = [pair.value for pair in hash_table.pairs if pair]
    assert None not in values
```

A linha destacada parece exatamente o que você precisaria para implementar a propriedade `.values`, que você substituiu por `.pairs` anteriormente. Você pode atualizar a função de teste para tirar proveito de `.values` novamente:

```python
# test_hashtable.py

# ...

def test_should_not_contain_none_value_when_created():
    assert None not in HashTable(capacity=100).values
```

Pode parecer que foi um esforço desperdiçado. No entanto, esses valores agora são avaliados dinamicamente por meio de uma propriedade de getter, enquanto antes eram armazenados em uma lista de tamanho fixo. Para atender a este teste, você pode reutilizar parte de sua antiga implementação, que utiliza uma compreensão de lista:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def values(self):
        return [pair.value for pair in self.pairs]
```

Observe que você não precisa mais especificar a condição de filtragem opcional aqui, porque já há uma por trás da propriedade `.pairs`.

Puristas podem pensar em usar uma compreensão de conjunto em vez de uma compreensão de lista para comunicar a falta de garantias para a ordem dos valores. No entanto, isso resultaria na perda de informações sobre valores duplicados na tabela de hash. Proteja-se dessa possibilidade desde o início, escrevendo outro caso de teste:

```python
# test_hashtable.py

# ...

def test_should_return_duplicate_values():
    hash_table = HashTable(capacity=100)
    hash_table["Alice"] = 24
    hash_table["Bob"] = 42
    hash_table["Joe"] = 42
    assert [24, 42, 42] == sorted(hash_table.values)
```

Se você tiver uma tabela de hash com nomes e idades, por exemplo, e mais de uma pessoa tiver a mesma idade, então `.values` deve manter todos os valores de idade repetidos. Você pode classificar as idades para garantir execuções de teste repetíveis. Embora este caso de teste não exija escrever um novo código, ele protegerá contra regressões.

Vale a pena verificar os valores esperados, seus tipos e sua quantidade. No entanto, você não pode comparar duas listas diretamente porque os valores reais em uma tabela de hash podem aparecer em uma ordem imprevisível. Para desconsiderar a ordem em seu teste, você poderia converter ambas as listas em conjuntos ou classificá-las como antes. Infelizmente, os conjuntos removem duplicatas potenciais, enquanto a ordenação não é possível quando as listas contêm tipos incompatíveis.

Para verificar de forma confiável se duas listas têm exatamente os mesmos elementos de tipos arbitrários com duplicatas potenciais, ignorando a ordem, você pode usar o seguinte idiom Python:

```python
def have_same_elements(list1, list2):
    return all(element in list1 for element in list2)
```

Isso alavanca a função embutida `all()`, mas é bastante verboso. Você provavelmente está melhor usando o plugin pytest-unordered. Não se esqueça de instalá-lo primeiro em seu ambiente virtual:

    Windows
    Linux + macOS

```bash
(venv) C:\> python -m pip install pytest-unordered
```

Em seguida, importe a função `unordered()` para o seu conjunto de testes e use-a para envolver os valores da tabela de hash:

```python
# test_hashtable.py

import pytest
from pytest_unordered import unordered

from hashtable import HashTable

# ...

def test_should_get_values(hash_table):
    assert unordered(hash_table.values) == ["hello", 37, True]
```

Ao fazer isso, os valores são convertidos em uma lista não ordenada, que redefine o operador de teste de igualdade para que não leve em consideração a ordem ao comparar os elementos da lista. Além disso, os valores de uma tabela de hash vazia devem ser uma lista vazia, enquanto a propriedade `.values` deve sempre retornar uma nova cópia da lista:

```python
# test_hashtable.py

# ...

def test_should_get_values_of_empty_hash_table():
    assert HashTable(capacity=100).values == []

def test_should_return_copy_of_values(hash_table):
    assert hash_table.values is not hash_table.values
```

Por outro lado, as chaves da tabela de hash devem ser únicas, então faz sentido enfatizar isso retornando um conjunto em vez de uma lista de chaves. Afinal, os conjuntos são, por definição, coleções não ordenadas de itens sem duplicatas:

```python
# test_hashtable.py

# ...

def test_should_get_keys(hash_table):
    assert hash_table.keys == {"hola", 98.6, False}

def test_should_get_keys_of_empty_hash_table():
    assert HashTable(capacity=100).keys == set()

def test_should_return_copy_of_keys(hash_table):
    assert hash_table.keys is not hash_table.keys
```

Não há literal de conjunto vazio em Python, então você precisa chamar diretamente a função interna `set()` neste caso. A implementação da função de getter correspondente será familiar:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def keys(self):
        return {pair.key for pair in self.pairs}
```

Isso se assemelha à propriedade `.values`. A diferença é que você usa chaves de chaves em vez de colchetes e se refere ao atributo `.key` em vez de `.value` em sua tupla nomeada. Alternativamente, você poderia usar `pair[0]` se quisesse, mas pareceria menos legível.

Isso também lembra você sobre a necessidade de um caso de teste semelhante que você deixou de cobrir ao lidar com o atributo `.pairs`. Faz sentido retornar um conjunto de pares para manter a consistência:

```python
# test_hashtable.py

# ...

def test_should_return_pairs(hash_table):
    assert hash_table.pairs == {
        ("hola", "hello"),
        (98.6, 37),
        (False, True)
    }

def test_should_get_pairs_of_empty_hash_table():
    assert HashTable(capacity=100).pairs == set()
```

Portanto, a propriedade `.pairs` também usará uma compreensão de conjunto daqui para frente:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def pairs(self):
        return {pair for pair in self._pairs if pair}
```

Você não precisa se preocupar em perder nenhuma informação, porque cada par chave-valor é único. Neste ponto, você deve estar novamente na fase verde.

Observe que você pode aproveitar a propriedade `.pairs` para converter sua tabela de hash em um dicionário comum e usar `.keys` e `.values` para testar isso:

```python
def test_should_convert_to_dict(hash_table):
    dictionary = dict(hash_table.pairs)
    assert set(dictionary.keys()) == hash_table.keys
    assert set(dictionary.items()) == hash_table.pairs
    assert list(dictionary.values()) == unordered(hash_table.values)
```

Para desconsiderar a ordem dos elementos, lembre-se de envolver as chaves do dicionário e os pares chave-valor com conjuntos antes de fazer a comparação. Em contraste, os valores de sua tabela de hash são obtidos como uma lista, então certifique-se de usar a função `unordered()` para comparar listas ignorando a ordem dos elementos.

Ok, sua tabela de hash está realmente começando a tomar forma agora!

Relatar o Comprimento da Tabela de Hash

Há um pequeno detalhe que você deixou intencionalmente quebrado por simplicidade até agora. É o comprimento da sua tabela de hash, que atualmente relata sua capacidade máxima mesmo quando há apenas slots vazios. Felizmente, não é preciso muito esforço para corrigir isso. Encontre a função chamada test_should_report_capacity(), renomeie conforme mostrado abaixo, e verifique se o comprimento de uma tabela de hash vazia é igual a zero em vez de cem:

```python
# test_hashtable.py

# ...

def test_should_report_length_of_empty_hash_table():
    assert len(HashTable(capacity=100)) == 0
```

Para tornar a capacidade independente do comprimento, modifique seu método especial .__len__() para que ele se refira à propriedade pública com pares filtrados em vez da lista privada de todos os slots:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __len__(self):
        return len(self.pairs)

    # ...
```

Você acabou de remover o sublinhado inicial do nome da variável. Mas essa pequena mudança está fazendo com que vários testes terminem abruptamente com um erro e alguns falhem.

Nota: Testes que falham são menos graves porque suas assertivas avaliam para Falso, enquanto erros indicam comportamento totalmente inesperado em seu código.

Parece que a maioria dos casos de teste sofre do mesmo erro não tratado devido à divisão por zero ao mapear a chave para um índice. Isso faz sentido porque ._index() usa o comprimento da tabela de hash para encontrar o resto da divisão da chave hash pelo número de slots disponíveis. No entanto, o comprimento da tabela de hash agora tem um significado diferente. Você precisa levar o comprimento da lista interna:

```python
# hashtable.py

class HashTable:
    # ...

    def _index(self, key):
        return hash(key) % len(self._pairs)
```

Isso está muito melhor agora. Os três casos de teste que ainda falham usam suposições erradas sobre o comprimento da tabela de hash. Altere essas suposições para que os testes passem:

```python
# test_hashtable.py

# ...

def test_should_insert_key_value_pairs():
    hash_table = HashTable(capacity=100)

    hash_table["hola"] = "hello"
    hash_table[98.6] = 37
    hash_table[False] = True

    assert ("hola", "hello") in hash_table.pairs
    assert (98.6, 37) in hash_table.pairs
    assert (False, True) in hash_table.pairs

    assert len(hash_table) == 3

# ...

def test_should_delete_key_value_pair(hash_table):
    assert "hola" in hash_table
    assert ("hola", "hello") in hash_table.pairs
    assert len(hash_table) == 3

    del hash_table["hola"]

    assert "hola" not in hash_table
    assert ("hola", "hello") not in hash_table.pairs
    assert len(hash_table) == 2

# ...

def test_should_update_value(hash_table):
    assert hash_table["hola"] == "hello"

    hash_table["hola"] = "hallo"

    assert hash_table["hola"] == "hallo"
    assert hash_table[98.6] == 37
    assert hash_table[False] is True
    assert len(hash_table) == 3
```

Você está de volta ao jogo, mas o ZeroDivisionError foi um sinal de alerta que deveria imediatamente fazer você querer adicionar casos de teste adicionais:

```python
# test_hashtable.py

# ...

def test_should_not_create_hashtable_with_zero_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=0)

def test_should_not_create_hashtable_with_negative_capacity():
    with pytest.raises(ValueError):
        HashTable(capacity=-100)
```

Criar uma HashTable com capacidade não positiva não faz muito sentido. Como você teria um contêiner com um comprimento negativo? Portanto, você deve levantar uma exceção se alguém tentar isso, seja intencionalmente ou por acidente. A maneira padrão de indicar argumentos de entrada incorretos em Python é levantar uma exceção ValueError:

```python
# hashtable.py

# ...

class HashTable:
    def __init__(self, capacity):
        if capacity < 1:
            raise ValueError("A capacidade deve ser um número positivo")
        self._pairs = capacity * [None]

    # ...
```

Se você for diligente, provavelmente também deverá verificar tipos de argumentos inválidos, mas isso está além do escopo deste tutorial. Você pode tratá-lo como um exercício voluntário.

Em seguida, adicione outro cenário para testar o comprimento de uma tabela de hash não vazia fornecida como um fixture pelo pytest:

```python
# test_hashtable.py

# ...

def test_should_report_length(hash_table):
    assert len(hash_table) == 3
```

Existem três pares chave-valor, então o comprimento da tabela de hash também deve ser três. Este teste não deve exigir código adicional. Finalmente, como você está na fase de refatoração agora, pode adicionar um pouco de açúcar sintático introduzindo a propriedade .capacity e usando-a sempre que possível:

```python
# test_hashtable.py

# ...

def test_should_report_capacity_of_empty_hash_table():
    assert HashTable(capacity=100).capacity == 100

def test_should_report_capacity(hash_table):
    assert hash_table.capacity == 100
```

A capacidade é constante e determinada no momento da criação da tabela de hash. Você pode derivá-la do comprimento da lista subjacente de pares:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def capacity(self):
        return len(self._pairs)

    def _index(self, key):
        return hash(key) % self.capacity
```

Ao introduzir novo vocabulário em seu domínio de problema, isso o ajuda a descobrir novas oportunidades para nomenclaturas mais precisas e inequívocas. Por exemplo, você viu a palavra "pairs" sendo usada de forma intercambiável para se referir tanto aos pares chave-valor reais armazenados em sua tabela de hash quanto a uma lista interna de slots para pares. Pode ser uma boa oportunidade para refatorar seu código mudando `._pairs` para `._slots` em todos os lugares.

Então, um dos seus casos de teste anteriores comunicará sua intenção com mais clareza:

```python
# test_hashtable.py

# ...

def test_should_create_empty_value_slots():
    assert HashTable(capacity=3)._slots == [None, None, None]
```

Talvez faça ainda mais sentido renomear este teste substituindo a palavra "value" por "pair":

```python
# test_hashtable.py

# ...

def test_should_create_empty_pair_slots():
    assert HashTable(capacity=3)._slots == [None, None, None]
```

Você pode pensar que tais reflexões filosóficas não são necessárias. No entanto, quanto mais descritivos forem seus nomes, mais legível será seu código — se não para os outros, certamente para você no futuro. Existem até livros e piadas sobre isso. Seus testes são uma forma de documentação, então vale a pena manter o mesmo nível de atenção aos detalhes para eles como para o código em teste.

Tornar a Tabela de Hash Iterável
Python permite que você itere sobre um dicionário através das chaves, dos valores ou dos pares chave-valor conhecidos como itens. Você deseja o mesmo comportamento em sua tabela de hash personalizada, então você começa esboçando alguns casos de teste:

# test_hashtable.py

# ...

def test_should_iterate_over_keys(hash_table):
    for key in hash_table.keys:
        assert key in ("hola", 98.6, False)

def test_should_iterate_over_values(hash_table):
    for value in hash_table.values:
        assert value in ("hello", 37, True)

def test_should_iterate_over_pairs(hash_table):
    for key, value in hash_table.pairs:
        assert key in hash_table.keys
        assert value in hash_table.values
A iteração por chaves, valores ou pares chave-valor funciona automaticamente com a implementação atual porque os conjuntos e listas subjacentes já podem lidar com isso. Por outro lado, para tornar instâncias da sua classe HashTable iteráveis, você deve definir outro método especial, que permitirá que você coopere diretamente com os loops for:

# test_hashtable.py

# ...

def test_should_iterate_over_instance(hash_table):
    for key in hash_table:
        assert key in ("hola", 98.6, False)
Ao contrário do que acontecia antes, você passa uma referência à instância HashTable aqui, mas o comportamento é o mesmo que se você estivesse iterando sobre a propriedade .keys. Este comportamento é compatível com o dict integrado no Python.

O método especial necessário, .__iter__(), deve retornar um objeto iterador, que o loop usa internamente:

# hashtable.py

# ...

class HashTable:
    # ...

    def __iter__(self):
        yield from self.keys
Este é um exemplo de um iterador gerador, que aproveita a palavra-chave yield em Python.

Nota: A expressão yield from delega a iteração para um sub-gerador, que pode ser outro objeto iterável, como uma lista ou um conjunto.

A palavra-chave yield permite que você defina um iterador in-place usando um estilo funcional sem criar outra classe. O método especial chamado .__iter__() é chamado pelo loop for quando ele começa.

Bem, neste ponto, apenas algumas características não essenciais estão faltando na sua tabela de hash.

Representar a Tabela de Hash em Texto
A próxima parte que você vai implementar nesta seção tornará sua tabela de hash visualmente agradável quando impressa na saída padrão. A representação textual de sua tabela de hash se parecerá com um literal de dicionário Python:

```python
# test_hashtable.py

# ...

def test_should_use_dict_literal_for_str(hash_table):
    assert str(hash_table) in {
        "{'hola': 'hello', 98.6: 37, False: True}",
        "{'hola': 'hello', False: True, 98.6: 37}",
        "{98.6: 37, 'hola': 'hello', False: True}",
        "{98.6: 37, False: True, 'hola': 'hello'}",
        "{False: True, 'hola': 'hello', 98.6: 37}",
        "{False: True, 98.6: 37, 'hola': 'hello'}",
    }
```

O literal usa chaves, vírgulas e dois-pontos, enquanto chaves e valores têm suas representações respectivas. Por exemplo, strings são envolvidas em apóstrofos simples. Como você não conhece a ordem exata dos pares chave-valor, verifica se a representação de string da sua tabela de hash está de acordo com uma das possíveis permutações de pares.

Para fazer com que sua classe funcione com a função interna str(), você deve implementar o método especial correspondente em HashTable:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __str__(self):
        pairs = []
        for key, value in self.pairs:
            pairs.append(f"{key!r}: {value!r}")
        return "{" + ", ".join(pairs) + "}"
```

Você itera sobre chaves e valores através da propriedade .pairs e usa f-strings para formatar os pares individuais. Observe a flag de conversão !r na string de modelo, que força a chamada de repr() em vez do padrão str() em chaves e valores. Isso garante uma representação mais explícita, que varia entre os tipos de dados. Por exemplo, ela envolve strings em apóstrofos simples.

A diferença entre str() e repr() é mais sutil. Em geral, ambos são destinados a converter objetos em strings. No entanto, enquanto você pode esperar que str() retorne um texto amigável para humanos, repr() frequentemente retorna um trecho de código Python válido que você pode avaliar para recriar o objeto original:

```python
>>> from fractions import Fraction
>>> quarto = Fraction("1/4")

>>> str(quarto)
'1/4'

>>> repr(quarto)
'Fraction(1, 4)'

>>> eval(repr(quarto))
Fraction(1, 4)
```

Neste exemplo, a representação de string de uma fração Python é '1/4', mas a representação de string canônica do mesmo objeto representa uma chamada à classe Fraction.

Você pode alcançar um efeito semelhante em sua classe HashTable. Infelizmente, seu inicializador de classe não permite criar novas instâncias a partir de valores no momento. Você resolverá isso introduzindo um método de classe que permitirá criar instâncias da HashTable a partir de dicionários Python:

```python
# test_hashtable.py

# ...

def test_should_create_hashtable_from_dict():
    dicionario = {"hola": "hello", 98.6: 37, False: True}

    hash_table = HashTable.from_dict(dicionario)

    assert hash_table.capacity == len(dicionario) * 10
    assert hash_table.keys == set(dicionario.keys())
    assert hash_table.pairs == set(dicionario.items())
    assert unordered(hash_table.values) == list(dicionario.values())
```

Isso se integra bem à sua conversão anterior, que estava na direção oposta. No entanto, você precisará assumir uma capacidade suficientemente grande para a tabela de hash conter todos os pares chave-valor do dicionário original. Uma estimativa razoável parece ser dez vezes o número de pares. Você pode codificar isso por enquanto:

Isso se integra bem com a sua conversão anterior, que estava na direção oposta. No entanto, você precisará assumir uma capacidade suficientemente grande para a tabela de hash conter todos os pares chave-valor do dicionário original. Uma estimativa razoável parece ser dez vezes o número de pares. Você pode codificar isso por enquanto:

```python
# hashtable.py

# ...

class HashTable:

    @classmethod
    def from_dict(cls, dictionary):
        hash_table = cls(len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
```

Você cria uma nova tabela de hash e define sua capacidade usando um fator arbitrário. Em seguida, você insere pares chave-valor copiando-os do dicionário passado como argumento para o método. Você pode permitir a substituição da capacidade padrão, se desejar, então adicione um caso de teste semelhante:

```python
# test_hashtable.py

# ...

def test_should_create_hashtable_from_dict_with_custom_capacity():
    dicionario = {"hola": "hello", 98.6: 37, False: True}

    hash_table = HashTable.from_dict(dicionario, capacity=100)

    assert hash_table.capacity == 100
    assert hash_table.keys == set(dicionario.keys())
    assert hash_table.pairs == set(dicionario.items())
    assert unordered(hash_table.values) == list(dicionario.values())
```

Para tornar a capacidade opcional, você pode aproveitar a avaliação de curto-circuito de expressões booleanas:

```python
# hashtable.py

# ...

class HashTable:

    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary) * 10)
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table
```

Se a capacidade não for especificada, você recorre ao comportamento padrão, que multiplica o comprimento do dicionário por dez. Com isso, você finalmente consegue fornecer uma representação de string canônica para suas instâncias de HashTable:

```python
# test_hashtable.py

# ...

def test_should_have_canonical_string_representation(hash_table):
    assert repr(hash_table) in {
        "HashTable.from_dict({'hola': 'hello', 98.6: 37, False: True})",
        "HashTable.from_dict({'hola': 'hello', False: True, 98.6: 37})",
        "HashTable.from_dict({98.6: 37, 'hola': 'hello', False: True})",
        "HashTable.from_dict({98.6: 37, False: True, 'hola': 'hello'})",
        "HashTable.from_dict({False: True, 'hola': 'hello', 98.6: 37})",
        "HashTable.from_dict({False: True, 98.6: 37, 'hola': 'hello'})",
    }
```

Como antes, você verifica todas as possíveis permutações de ordem de atributos na representação resultante. A representação de string canônica de uma tabela de hash parece quase a mesma que com str(), mas também envolve o literal de dict em uma chamada ao seu novo método de classe .from_dict(). A implementação correspondente delega para o método especial .__str__() chamando a função interna str():

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __repr__(self):
        cls = self.__class__.__name__
        return f"{cls}.from_dict({str(self)})"
```

Observe que você não codifica o nome da classe, para evitar problemas se escolher renomear sua classe posteriormente.

Seu protótipo de tabela de hash está quase pronto, pois você implementou quase todos os recursos essenciais e não essenciais da lista mencionada na introdução desta seção. Você acabou de adicionar a capacidade de criar uma tabela de hash a partir de um dict Python e forneceu representações de string para suas instâncias. O último e final é garantir que as instâncias da tabela de hash possam ser comparadas por valor.

Testar a Igualdade de Tabelas de Hash
Tabelas de hash são como conjuntos no sentido de que não impõem nenhuma ordem específica para seus conteúdos. Na verdade, tabelas de hash e conjuntos têm mais em comum do que você pode pensar, pois ambos são apoiados por uma função de hash. É a função de hash que torna os pares chave-valor em uma tabela de hash não ordenados. No entanto, lembre-se de que, a partir do Python 3.6, o dict realmente mantém a ordem de inserção como um detalhe de implementação.

Duas tabelas de hash devem ser consideradas iguais se e somente se tiverem o mesmo conjunto de pares chave-valor. No entanto, o Python compara as identidades dos objetos por padrão porque não sabe interpretar valores de tipos de dados personalizados. Assim, duas instâncias de sua tabela de hash sempre seriam consideradas desiguais mesmo que compartilhassem o mesmo conjunto de pares chave-valor.

Para corrigir isso, você pode implementar o operador de teste de igualdade (==) fornecendo o método especial .__eq__() em sua classe HashTable. Além disso, o Python chamará esse método para avaliar o operador de não igualdade (!=) a menos que você também implemente .__ne__() explicitamente.

Você deseja que a tabela de hash seja igual a ela mesma, à sua cópia ou a outra instância com os mesmos pares chave-valor, independentemente de sua ordem. Por outro lado, uma tabela de hash não deve ser igual a uma instância com um conjunto diferente de pares chave-valor ou um tipo de dado completamente diferente:

```python
# test_hashtable.py

# ...

def test_should_compare_equal_to_itself(hash_table):
    assert hash_table == hash_table

def test_should_compare_equal_to_copy(hash_table):
    assert hash_table is not hash_table.copy()
    assert hash_table == hash_table.copy()

def test_should_compare_equal_different_key_value_order(hash_table):
    h1 = HashTable.from_dict({"a": 1, "b": 2, "c": 3})
    h2 = HashTable.from_dict({"b": 2, "a": 1, "c": 3})
    assert h1 == h2

def test_should_compare_unequal(hash_table):
    other = HashTable.from_dict({"different": "value"})
    assert hash_table != other

def test_should_compare_unequal_another_data_type(hash_table):
    assert hash_table != 42
```

Você usa .from_dict(), introduzido na subseção anterior, para popular rapidamente novas tabelas de hash com valores. Você pode aproveitar o mesmo método de classe para fazer uma nova cópia de uma instância de tabela de hash. Aqui está o código que atende a esses casos de teste:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return set(self.pairs) == set(other.pairs)

    # ...

    def copy(self):
        return HashTable.from_dict(dict(self.pairs), self.capacity)
```

O método especial .__eq__() recebe algum objeto como argumento para comparar. Se esse objeto acontecer de ser a instância atual de HashTable, então você retorna True porque a mesma identidade implica igualdade de valor. Caso contrário, você prossegue comparando os tipos e os conjuntos de pares chave-valor. A conversão para conjuntos ajuda a tornar a ordem irrelevante mesmo se você decidir transformar .pairs em outra lista ordenada no futuro.

A propósito, a cópia resultante deve ter não apenas os mesmos pares chave-valor, mas também a mesma capacidade da tabela de hash de origem. Ao mesmo tempo, duas tabelas de hash com capacidades diferentes ainda devem ser consideradas iguais:

```python
# test_hashtable.py

# ...

def test_should_copy_keys_values_pairs_capacity(hash_table):
    copy = hash_table.copy()
    assert copy is not hash_table
    assert set(hash_table.keys) == set(copy.keys)
    assert unordered(hash_table.values) == copy.values
    assert set(hash_table.pairs) == set(copy.pairs)
    assert hash_table.capacity == copy.capacity

def test_should_compare_equal_different_capacity():
    data = {"a": 1, "b": 2, "c": 3}
    h1 = HashTable.from_dict(data, capacity=50)
    h2 = HashTable.from_dict(data, capacity=100)
    assert h1 == h2
```

Esses dois testes funcionarão com sua implementação atual de HashTable, então você não precisa codificar nada extra.

Seu protótipo de tabela de hash personalizada ainda está faltando alguns recursos não essenciais que o dicionário integrado fornece. Você pode tentar adicioná-los como um exercício. Por exemplo, você poderia replicar outros métodos dos dicionários Python, como dict.clear() ou dict.update(). Além disso, você pode implementar um dos operadores bitwise suportados por dict desde o Python 3.9, que permite uma operação de união.

Bem feito! Esta é a suíte de testes concluída para o tutorial, e sua tabela de hash passou em todos os testes unitários. Dê a si mesmo uma merecida palmada nas costas, porque foi um trabalho excelente. Ou será que foi?

Suponha que você reduza a capacidade de sua tabela de hash para considerar apenas os pares inseridos. A seguinte tabela de hash deve acomodar todos os três pares chave-valor armazenados no dicionário de origem:

```python
>>> from hashtable import HashTable
>>> source = {"hola": "hello", 98.6: 37, False: True}
>>> hash_table = HashTable.from_dict(source, capacity=len(source))
>>> str(hash_table)
'{False: True}'
```

No entanto, quando você revela as chaves e valores da tabela de hash resultante, às vezes você descobre que há menos itens. Para tornar este trecho de código repetível, execute-o com a randomização de hash desativada, configurando a variável de ambiente PYTHONHASHSEED para 0.

Na maioria das vezes, você acabará perdendo informações mesmo que haja espaço suficiente disponível na tabela de hash. Isso ocorre porque a maioria das funções de hash não são perfeitas, causando colisões de hash, que você aprenderá a resolver em seguida.

Resolver Colisões de Código Hash
Nesta seção, você explorará as duas estratégias mais comuns para lidar com colisões de código hash e as implementará em sua classe HashTable. Se você quiser seguir os exemplos abaixo, não se esqueça de definir a variável PYTHONHASHSEED como 0 para desativar a randomização de hash do Python.

Até agora, você já deve ter uma boa ideia do que é uma colisão de código hash. Isso acontece quando duas chaves produzem o mesmo código hash, levando valores distintos a colidirem entre si no mesmo índice na tabela de hash. Por exemplo, em uma tabela de hash com cem slots, as chaves "fácil" e "difícil" compartilham o mesmo índice quando a randomização de hash está desativada:

```python
>>> hash("fácil") % 100
43

>>> hash("difícil") % 100
43
```

Até agora, sua tabela de hash não pode detectar tentativas de armazenar valores diferentes no mesmo slot:

```python
>>> from hashtable import HashTable

>>> tabela_hash = HashTable(capacidade=100)
>>> tabela_hash["fácil"] = "Exige pouco esforço"
>>> tabela_hash["difícil"] = "Requer muita habilidade"

>>> print(tabela_hash)
{'difícil': 'Requer muita habilidade'}

>>> tabela_hash["fácil"]
'Requer muita habilidade'
```

Você não apenas acaba sobrescrevendo o par identificado pela chave "fácil", mas, pior ainda, recuperar o valor desta chave agora inexistente fornece uma resposta incorreta!

Existem três estratégias disponíveis para abordar colisões de código hash:

Estratégia	Descrição
Hashing Perfeito	Escolha uma função de hash perfeita para evitar colisões de hash desde o início.
Endereçamento Aberto	Espalhe os valores colididos de uma maneira previsível que permita recuperá-los posteriormente.
Endereçamento Fechado	Mantenha os valores colididos em uma estrutura de dados separada para pesquisar posteriormente.
Enquanto o hashing perfeito é possível apenas quando você conhece todos os valores antecipadamente, os outros dois métodos de resolução de colisões de código hash são mais práticos, então você os examinará mais de perto neste tutorial. Observe que o endereçamento aberto pode ser representado por vários algoritmos específicos, incluindo:

- Cuckoo hashing
- Double hashing
- Hopscotch hashing
- Linear probing
- Quadratic probing
- Robin Hood hashing

Por outro lado, o endereçamento fechado é mais conhecido pelo encadeamento separado. Além disso, há também o hashing coalescido, que combina as ideias por trás do endereçamento aberto e fechado em um único algoritmo.

Para seguir o desenvolvimento orientado por testes, você precisará projetar primeiro um caso de teste. Mas como testar uma colisão de código hash? A função embutida do Python usa randomização de hash por padrão para alguns de seus tipos de dados, o que torna extremamente difícil prever seu comportamento. Escolher manualmente uma semente de hash com a variável de ambiente PYTHONHASHSEED seria impraticável e tornaria seus casos de teste frágeis.

A melhor maneira de contornar isso é usar uma biblioteca de simulação, como o unittest.mock do Python:

```python
from unittest.mock import patch

@patch("builtins.hash", return_value=42)
def test_should_detect_hash_collision(hash_mock):
    assert hash("foobar") == 42
```

O patch substitui temporariamente um objeto por outro. Por exemplo, você pode substituir a função hash() padrão por uma falsa que sempre retorna o mesmo valor esperado, tornando seus testes repetíveis. Essa substituição só tem efeito durante a chamada da função, após o qual a hash() original é restaurada.

Você pode aplicar o decorador @patch para toda a função de teste ou limitar o escopo do objeto simulado com um gerenciador de contexto:

```python
from unittest.mock import patch

def test_should_detect_hash_collision():
    assert hash("foobar") not in [1, 2, 3]
    with patch("builtins.hash", side_effect=[1, 2, 3]):
        assert hash("foobar") == 1
        assert hash("foobar") == 2
        assert hash("foobar") == 3
```

Com um gerenciador de contexto, você pode acessar tanto a função hash() embutida quanto sua versão simulada dentro do mesmo caso de teste. Você até poderia ter várias versões da função simulada se desejar. O parâmetro side_effect permite especificar uma exceção a ser levantada ou uma sequência de valores que seu objeto simulado retornará em invocações consecutivas.

Na parte restante deste tutorial, você continuará adicionando mais recursos à sua classe HashTable sem seguir estritamente o desenvolvimento orientado por testes. Novos testes serão omitidos por brevidade, enquanto a modificação da classe fará com que alguns dos testes existentes falhem. No entanto, você encontrará uma suíte de testes funcional nos materiais complementares disponíveis para download.

Encontre Chaves Colididas Através de Linear Probing
Pare por um momento para entender a teoria por trás das colisões de códigos hash. Quando se trata de lidar com elas, o linear probing é uma das técnicas mais antigas, diretas e eficazes ao mesmo tempo. Ele exige algumas etapas extras para as operações de inserção, consulta, exclusão e atualização, as quais você está prestes a aprender.

Considere uma tabela de hash de exemplo representando o glossário Python com acrônimos comuns. Ela tem uma capacidade total de dez slots, mas quatro deles já estão ocupados pelos seguintes pares chave-valor:

```
Índice   Chave   Valor
0        
1   BDFL   Benevolent Dictator For Life
2        
3   REPL   Read–Evaluate–Print Loop
4        
5        
6        
7        
8   PEP   Python Enhancement Proposal
9   WSGI   Web Server Gateway Interface
```

Agora, você deseja adicionar outro termo ao seu glossário para definir o acrônimo MRO, que significa ordem de resolução de método. Você calcula o código hash da chave e o trunca com o operador módulo para obter um índice entre zero e nove:

```python
>>> hash("MRO")
8199632715222240545

>>> hash("MRO") % 10
5
```

Em vez de usar o operador módulo, você poderia truncar o código hash com uma máscara adequada, que é como o dict interno do Python funciona.

Ótimo! Há um espaço livre em sua tabela de hash no índice cinco, onde você pode inserir um novo par chave-valor:

```
Índice   Chave   Valor
0        
1   BDFL   Benevolent Dictator For Life
2        
3   REPL   Read–Evaluate–Print Loop
4        
5   MRO   Method Resolution Order
6        
7        
8   PEP   Python Enhancement Proposal
9   WSGI   Web Server Gateway Interface
```

Até agora, tudo bem. Sua tabela de hash ainda tem 50% de espaço livre, então você continua adicionando mais termos até tentar inserir o acrônimo EAFP. Acontece que o código hash de EAFP se reduz a um, que é o índice de um slot ocupado pelo termo BDFL:

```python
>>> hash("EAFP")
-159847004290706279

>>> hash("BDFL")
-6396413444439073719

>>> hash("EAFP") % 10
1

>>> hash("BDFL") % 10
1
```

A probabilidade de duas chaves diferentes produzirem códigos hash colidentes é relativamente pequena. No entanto, projetar esses códigos hash em uma pequena faixa de índices de array é uma história diferente. Com o linear probing, você pode detectar e mitigar tais colisões armazenando os pares chave-valor colidentes lado a lado:

```
Índice   Chave   Valor
0        
1   BDFL   Benevolent Dictator For Life
2   EAFP   Easier To Ask For Forgiveness Than Permission
3   REPL   Read–Evaluate–Print Loop
4        
5   MRO   Method Resolution Order
6        
7        
8   PEP   Python Enhancement Proposal
9   WSGI   Web Server Gateway Interface
```

Embora as chaves BDFL e EAFP resultem no mesmo índice igual a um, apenas o primeiro par chave-valor inserido acaba ocupando-o. Qualquer par que venha em segundo lugar será colocado ao lado do índice ocupado. Portanto, o linear probing torna a tabela de hash sensível à ordem de inserção.

Nota: Quando você usa linear probing ou outros métodos de resolução de colisão de hash, você não pode depender apenas do código hash para encontrar o slot correspondente. Você também precisa comparar as chaves.

Considere adicionar outro acrônimo, ABC, para classes abstratas base, cujo código hash se reduz ao índice oito. Desta vez, você não pode inseri-lo na posição seguinte, pois já está ocupado por WSGI. Em circunstâncias normais, você continuaria procurando por um slot livre mais abaixo, mas, como chegou ao último índice, deve voltar e inserir o novo acrônimo no índice zero:

```
Índice   Chave   Valor
0   ABC   Abstract Base Class
1   BDFL   Benevolent Dictator For Life
2   EAFP   Easier To Ask For Forgiveness Than Permission
3   REPL   Read–Evaluate–Print Loop
4        
5   MRO   Method Resolution Order
6        
7        
8   PEP   Python Enhancement Proposal
9   WSGI   Web Server Gateway Interface
```

Para procurar pares chave-valor armazenados na tabela de hash dessa forma, siga um algoritmo semelhante. Comece olhando o índice esperado primeiro. Por exemplo, para encontrar o valor associado à chave ABC, calcule seu código hash e mapeie-o para um índice:

```python
>>> hash("ABC")
-4164790459813301872

>>> hash("ABC") % 10
8
```

Há um par chave-valor armazenado no índice oito, mas tem uma chave diferente igual a PEP, então você o ignora aumentando o índice. Novamente, esse slot é ocupado por um termo não relacionado, WSGI, então você volta e encontra o par correspondente com uma chave correspondente no índice zero. Essa é a sua resposta.

Em geral, existem três condições possíveis de parada para a operação de pesquisa:

1. Você encontrou uma chave correspondente.
2. Você esgotou todos os slots sem encontrar a chave correspondente.
3. Você encontrou um slot vazio, o que também indica uma chave ausente.

O último ponto torna a exclusão de um par chave-valor existente mais complicada. Se você acabou de remover uma entrada da tabela de hash, então você introduziria um slot em branco, o que interromperia a pesquisa ali, independentemente de quaisquer colisões anteriores. Para tornar os pares chave-valor colidentes alcançáveis novamente, você teria que ou reidratá-los ou usar uma estratégia de exclusão preguiçosa.

Esta última é menos difícil de implementar, mas tem o custo adicional de aumentar o número de etapas de pesquisa necessárias. Basicamente, em vez de excluir um par chave-valor, você o substitui por um valor sentinela, representado por uma cruz vermelha (❌) abaixo, o que torna possível encontrar entradas que haviam colidido anteriormente. Suponha que você queira excluir os termos BDFL e PEP:

```
Índice   Chave   Valor
0   ABC   Abstract Base Class
1   ❌    
2   EAFP   Easier To Ask For Forgiveness Than Permission
3   REPL   Read–Evaluate–Print Loop
4        
5   MRO   Method Resolution Order
6        
7        
8   ❌    
9   WSGI   Web Server Gateway Interface
```

Você substituiu os pares chave-valor correspondentes por duas instâncias do valor sentinela. Mais tarde, quando você procura pela chave ABC, por exemplo, você bate no sentinela no índice oito, depois continua até WSGI e finalmente chega ao índice zero com a chave correspondente. Sem um dos sentinelas, você interromperia a busca muito antes, concluindo falsamente que não há tal chave.

Nota: A capacidade da sua tabela de hash permanece inalterada, pois você está livre para sobrescrever sentinelas ao inserir novos pares chave-valor. Por outro lado, se você preencher a tabela de hash e excluir a maioria de seus elementos, você praticamente acabará com o algoritmo de pesquisa linear.

Até agora, você aprendeu sobre inserção, exclusão e busca. No entanto, há uma ressalva sobre a atualização do valor de uma entrada existente em uma tabela de hash com sondagem linear. Ao procurar um par para atualizar, você só deve pular o slot se estiver ocupado por outro par com uma chave diferente ou se contiver um valor sentinela. Por outro lado, se o slot estiver vazio ou tiver uma chave correspondente, você deve definir o novo valor.

Na próxima subseção, você vai modificar a sua classe HashTable para usar a sondagem linear na resolução de colisões de hash.

Usar a sondagem linear na classe HashTable

Após um breve desvio para a teoria da sondagem linear, você está de volta à codificação agora. Como a sondagem linear será usada em todas as quatro operações CRUD básicas na tabela de hash, ajuda escrever um método auxiliar em sua classe para encapsular a lógica de visitar os slots da tabela de hash:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def _probe(self, key):
        index = self._index(key)
        for _ in range(self.capacity):
            yield index, self._slots[index]
            index = (index + 1) % self.capacity
```

Dado uma chave, você começa usando o código de hash correspondente para encontrar seu índice esperado na tabela de hash. Em seguida, você percorre todos os slots disponíveis na tabela de hash, começando pelo índice calculado. Em cada etapa, você retorna o índice atual e o par associado, que pode estar vazio ou marcado como deletado. Depois, você aumenta o índice, voltando à origem, se necessário.

A seguir, você pode reescrever o método .__setitem__(). Não se esqueça da necessidade de um novo valor sentinela. Este valor permitirá diferenciar entre slots que nunca foram ocupados e aqueles que colidiram antes, mas agora estão deletados:

```python
# hashtable.py

DELETED = object()

# ...

class HashTable:
    # ...

    def __setitem__(self, key, value):
        for index, pair in self._probe(key):
            if pair is DELETED: continue
            if pair is None or pair.key == key:
                self._slots[index] = Pair(key, value)
                break
        else:
            raise MemoryError("Not enough capacity")
```

Se o slot estiver vazio ou contiver um par com a chave correspondente, você reatribui um novo par chave-valor no índice atual e interrompe a sondagem linear. Caso contrário, se outro par ocupar aquele slot e tiver uma chave diferente, ou o slot estiver marcado como deletado, você avança até encontrar um slot livre ou esgotar todos os slots disponíveis. Se ficar sem slots disponíveis, você levanta uma exceção MemoryError para indicar a capacidade insuficiente da tabela de hash.

Nota: Coincidentemente, o método .__setitem__() também abrange a atualização do valor de um par existente. Como os pares são representados por tuplas imutáveis, você substitui o par inteiro com a chave correspondente e não apenas sua componente de valor.

Obter e excluir pares chave-valor de uma tabela de hash usando sondagem linear funciona quase da mesma forma:

Obter e excluir pares chave-valor de uma tabela de hash usando sondagem linear funciona quase da mesma forma:

```python
# hashtable.py

DELETED = object()

# ...

class HashTable:
    # ...

    def __getitem__(self, key):
        for _, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                return pair.value
        raise KeyError(key)

    def __delitem__(self, key):
        for index, pair in self._probe(key):
            if pair is None:
                raise KeyError(key)
            if pair is DELETED:
                continue
            if pair.key == key:
                self._slots[index] = DELETED
                break
        else:
            raise KeyError(key)
```

A única diferença está nas linhas destacadas. Para excluir um par, você precisa saber onde ele está localizado na tabela de hash para substituí-lo pelo valor sentinela. Por outro lado, você está apenas interessado no valor correspondente ao procurar por chave. Se essa duplicação de código incomodar, você pode tentar refatorá-lo como um exercício. No entanto, tê-lo escrito explicitamente ajuda a destacar o ponto.

Nota: Esta é uma implementação clássica da tabela de hash, que sonda elementos comparando chaves usando o operador de teste de igualdade (==). No entanto, é uma operação potencialmente custosa, que implementações da vida real evitam armazenando o código de hash, juntamente com chaves e valores, em triplas em vez de pares. Os códigos de hash são baratos de comparar, por outro lado.

Você pode aproveitar o contrato de hash-igual para acelerar as coisas. Se dois códigos de hash forem diferentes, então eles são garantidos de se originarem de chaves diferentes, então não há necessidade de realizar um custoso teste de igualdade em primeiro lugar. Esse truque reduz dramaticamente o número de comparações de chave.

Há mais um detalhe importante a ser observado. Os slots da tabela de hash não podem mais estar em apenas dois estados, ou seja, vazio ou ocupado. Inserir o valor sentinela na tabela de hash para marcar um slot como deletado bagunça as propriedades .pairs, .keys e .values da tabela de hash e relata o comprimento incorretamente. Para corrigir isso, você precisa filtrar os valores None e DELETED ao retornar pares chave-valor:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def pairs(self):
        return {
            pair for pair in self._slots
            if pair not in (None, DELETED)
        }
```

Com essa pequena atualização, sua tabela de hash agora deve ser capaz de lidar com colisões de hash espalhando os pares colididos e procurando por eles de maneira linear:

```python
>>> from unittest.mock import patch
>>> from hashtable import HashTable

>>> with patch("builtins.hash", return_value=24):
...     hash_table = HashTable(capacity=100)
...     hash_table["easy"] = "Requires little effort"
...     hash_table["difficult"] = "Needs much skill"

>>> hash_table._slots[24]
Pair(key='easy', value='Requires little effort')

>>> hash_table._slots[25]
Pair(key='difficult', value='Needs much skill')
```

Apesar de terem o mesmo código de hash igual a vinte e quatro, ambas as chaves colididas, "easy" e "difficult", aparecem uma ao lado da outra na lista ._slots. Observe que elas são listadas na mesma ordem em que foram adicionadas à tabela de hash. Experimente trocar a ordem de inserção ou alterar a capacidade da tabela de hash e observe como isso afeta os slots.

Até agora, a capacidade da tabela de hash permanece fixa. Antes de implementar a sondagem linear, você permanecia alheio e continuava sobrescrevendo valores colididos. Agora, você pode detectar quando não há mais espaço em sua tabela de hash e levantar uma exceção correspondente. No entanto, não seria melhor permitir que a tabela de hash ajustasse dinamicamente sua capacidade conforme necessário?

Deixe a Tabela de Hash Redimensionar Automaticamente

Existem duas estratégias diferentes quando se trata de redimensionar uma tabela de hash. Você pode esperar até o último momento e redimensionar a tabela de hash apenas quando ela estiver cheia, ou pode fazê-lo rapidamente após atingir um determinado limite. Ambas as formas têm seus prós e contras. A estratégia preguiçosa é, sem dúvida, mais fácil de implementar, então você dará uma olhada mais de perto nela primeiro. No entanto, ela pode levar a mais colisões e pior desempenho.

A única vez que você precisa aumentar o número de slots em sua tabela de hash é quando a inserção de um novo par falha, levantando a exceção MemoryError. Vá em frente e substitua a instrução raise por uma chamada a outro método auxiliar que você criará, seguida por uma chamada recursiva a .__setitem__() por meio da sintaxe de colchetes:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __setitem__(self, key, value):
        for index, pair in self._probe(key):
            if pair is DELETED: continue
            if pair is None or pair.key == key:
                self._slots[index] = Pair(key, value)
                break
        else:
            self._resize_and_rehash()
            self[key] = value
```

Quando você determina que todos os slots estão ocupados, por um par legítimo ou pelo valor sentinela, você deve alocar mais memória, copiar os pares existentes e tentar inserir esse novo par chave-valor novamente.

Nota: Colocar seus antigos pares chave-valor em uma tabela de hash maior fará com que eles hashem para slots totalmente diferentes. O rehashing tira vantagem dos slots extras que você acabou de criar, reduzindo o número de colisões na nova tabela de hash. Além disso, economiza espaço recuperando slots que costumavam ser marcados como deletados com o valor sentinela. Você não precisa se preocupar com colisões passadas, porque os pares chave-valor encontrarão novos slots de qualquer maneira.

Agora, implemente o redimensionamento e o rehashing da seguinte forma:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def _resize_and_rehash(self):
        copy = HashTable(capacity=self.capacity * 2)
        for key, value in self.pairs:
            copy[key] = value
        self._slots = copy._slots
```

Crie uma cópia local da tabela de hash. Como é difícil prever quantos slots adicionais você pode precisar, faça um palpite selvagem e dobre o tamanho da capacidade. Em seguida, itere sobre seu conjunto existente de pares chave-valor e os insira na cópia. Finalmente, reatribua o atributo ._slots em sua instância para que aponte para a lista ampliada de slots.

Sua tabela de hash agora pode aumentar dinamicamente de tamanho quando necessário, então teste-a. Crie uma tabela de hash vazia com uma capacidade de um e tente inserir alguns pares chave-valor nela:

```python
>>> from hashtable import HashTable
>>> hash_table = HashTable(capacity=1)
>>> for i in range(20):
...     num_pairs = len(hash_table)
...     num_empty = hash_table.capacity - num_pairs
...     print(
...         f"{num_pairs:>2}/{hash_table.capacity:>2}",
...         ("X" * num_pairs) + ("." * num_empty)
...     )
...     hash_table[i] = i
...
 0/ 1 .
 1/ 1 X
 2/ 2 XX
 3/ 4 XXX.
 4/ 4 XXXX
 5/ 8 XXXXX...
 6/ 8 XXXXXX..
 7/ 8 XXXXXXX.
 8/ 8 XXXXXXXX
 9/16 XXXXXXXXX.......
10/16 XXXXXXXXXX......
11/16 XXXXXXXXXXX.....
12/16 XXXXXXXXXXXX....
13/16 XXXXXXXXXXXXX...
14/16 XXXXXXXXXXXXXX..
15/16 XXXXXXXXXXXXXXX.
16/16 XXXXXXXXXXXXXXXX
17/32 XXXXXXXXXXXXXXXXX...............
18/32 XXXXXXXXXXXXXXXXXX..............
19/32 XXXXXXXXXXXXXXXXXXX.............
```

Ao inserir com sucesso vinte pares chave-valor, você nunca obteve erros. Com essa representação grosseira, você pode ver claramente o dobramento de slots, que ocorre quando a tabela de hash fica cheia e precisa de mais slots.

Graças ao redimensionamento automático que você acabou de implementar, você pode assumir uma capacidade padrão para novas tabelas de hash. Dessa forma, a criação de uma instância da classe HashTable não exigirá mais especificar a capacidade inicial, embora fazê-lo possa melhorar o desempenho. Uma escolha comum para a capacidade inicial é um pequeno poder de dois, como oito:

```python
# hashtable.py

# ...

class HashTable:
    @classmethod
    def from_dict(cls, dictionary, capacity=None):
        hash_table = cls(capacity or len(dictionary))
        for key, value in dictionary.items():
            hash_table[key] = value
        return hash_table

    def __init__(self, capacity=8):
        if capacity < 1:
            raise ValueError("A capacidade deve ser um número positivo")
        self._slots = capacity * [None]

    # ...
```

Isso torna possível criar tabelas de hash com uma chamada ao inicializador sem parâmetros HashTable(). Observe que você também pode atualizar seu método de classe HashTable.from_dict() para usar o comprimento do dicionário como a capacidade inicial. Anteriormente, você multiplicava o comprimento do dicionário por um fator arbitrário, o que era necessário para fazer seus testes passarem, devido a colisões de hash não tratadas.

Como mencionado anteriormente, há um problema com a estratégia de redimensionamento preguiçoso, e é a maior probabilidade de colisões. Você vai abordar isso em seguida.
Calcular o Fator de Carga

Esperar até que sua tabela de hash fique saturada não é o ideal. Você pode tentar uma estratégia mais ávida para redimensionar a tabela de hash antes de atingir sua capacidade total, evitando que as colisões aconteçam em primeiro lugar. Como decidir o melhor momento para redimensionar e refazer o hash? Use o fator de carga!

O fator de carga é a razão entre o número de slots atualmente ocupados, incluindo os deletados, para todos os slots na tabela de hash. Quanto maior o fator de carga, maior a chance de uma colisão de hash, resultando em pior desempenho na busca. Portanto, você quer que o fator de carga permaneça relativamente pequeno o tempo todo. Aumentar o tamanho da tabela de hash é necessário sempre que o fator de carga atingir um certo limite.

A escolha de um limite específico é um exemplo clássico do compromisso espaço-tempo na ciência da computação. Redimensionar a tabela de hash com mais frequência é mais barato e leva a um melhor desempenho com o custo de um maior consumo de memória. Por outro lado, esperar mais pode economizar memória, mas as buscas por chave serão mais lentas. O gráfico abaixo representa a relação entre a quantidade de memória alocada e o número médio de colisões:

Capacidade da Tabela de Hash vs Número Médio de Colisões
Os dados por trás deste gráfico medem o número médio de colisões causadas pela inserção de cem elementos em uma tabela de hash vazia com uma capacidade inicial de um. A medição foi repetida várias vezes para vários limites de fator de carga, nos quais a tabela de hash redimensionou-se em saltos discretos, dobrando sua capacidade.

A interseção de ambos os gráficos, que ocorre em torno de 0,75, indica o ponto ideal do limite, com a menor quantidade de memória e número de colisões. Usar um limite de fator de carga mais alto não fornece economias significativas de memória, mas aumenta exponencialmente o número de colisões. Um limite menor melhora o desempenho, mas por um alto custo de memória desperdiçada. Lembre-se de que você realmente só precisa de cem slots!

Você pode experimentar com diferentes limites de fator de carga, mas redimensionar a tabela de hash quando 60% de seus slots estão ocupados pode ser um bom ponto de partida. Veja como você pode implementar o cálculo do fator de carga em sua classe HashTable:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def load_factor(self):
        occupied_or_deleted = [slot for slot in self._slots if slot]
        return len(occupied_or_deleted) / self.capacity
```

Você começa filtrando slots que são verdadeiros, que seriam qualquer coisa exceto None, e depois pega a razão de acordo com a definição do fator de carga. Observe que se você decidir usar uma expressão de compreensão, ela deve ser uma compreensão de lista para contar todas as ocorrências de valores de sentinelas. Neste caso, usar uma compreensão de conjunto filtraria as marcações repetidas de pares excluídos, deixando apenas uma instância e resultando em um fator de carga incorreto.

Em seguida, modifique sua classe para aceitar um limite de fator de carga opcional e usá-lo para redimensionar e redefinir os slots:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if capacity < 1:
            raise ValueError("A capacidade deve ser um número positivo")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("O fator de carga deve ser um número entre (0, 1]")
        self._slots = capacity * [None]
        self._load_factor_threshold = load_factor_threshold

    # ...

    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        for index, pair in self._probe(key):
            if pair is DELETED: continue
            if pair is None or pair.key == key:
                self._slots[index] = Pair(key, value)
                break
```

O limite do fator de carga padrão é 0.6, o que significa que 60% de todos os slots estão ocupados. Você usa uma desigualdade fraca (>=) em vez de uma estrita (>) para levar em conta o limite do fator de carga em seu valor máximo, que nunca pode ser maior que um. Se o fator de carga for igual a um, então você também deve redimensionar a tabela de hash antes de inserir outro par chave-valor.

Brilhante! Sua tabela de hash acabou de ficar um pouco mais rápida. Isso conclui o exemplo de endereçamento aberto neste tutorial. A próxima etapa é resolver colisões de hash usando uma das técnicas de endereçamento fechado mais populares.

Isolar chaves colidentes com encadeamento separado

O encadeamento separado é outro método extremamente popular de resolução de colisões de hash, talvez ainda mais difundido do que a sonda linear. A ideia é agrupar itens semelhantes por uma característica comum em chamados "buckets" para reduzir o espaço de busca. Por exemplo, você pode imaginar colher frutas e coletá-las em cestas codificadas por cores:

Cestas Agrupadas por Cor
Frutas Agrupadas por Cor em Cada Cesta
Cada cesta contém frutas de cor aproximada. Portanto, quando você deseja uma maçã, por exemplo, só precisa procurar na cesta rotulada como vermelha. Em um mundo ideal, cada cesta deve conter no máximo um elemento, tornando a busca instantânea. Você pode pensar nos rótulos como códigos de hash e as frutas com a mesma cor como os pares de chave-valor colidentes.

Uma tabela de hash baseada em encadeamento separado é uma lista de referências para cestas, normalmente implementadas como listas encadeadas que formam correntes de elementos:

Correntes de Pares de Chave-Valor Colidentes
Correntes de Pares de Chave-Valor Colidentes
Cada lista encadeada contém pares de chave-valor cujas chaves compartilham o mesmo código de hash devido a uma colisão. Ao procurar um valor pela chave, você precisa localizar a cesta certa primeiro, depois percorrê-la usando uma busca linear para encontrar a chave correspondente e, finalmente, retornar o valor correspondente. A busca linear significa apenas percorrer cada item na cesta, um por um, até encontrar a chave certa.

Nota: Os elementos das listas encadeadas têm uma pequena sobrecarga de memória porque cada nó contém uma referência para o próximo elemento. Ao mesmo tempo, esse layout de memória torna a adição e remoção de elementos muito rápidas em comparação com um array regular.

Para adaptar sua classe HashTable para usar encadeamento separado, comece removendo o método ._probe() e substituindo os slots por cestas. Agora, em vez de ter um valor None ou um par em cada índice, você fará com que cada índice contenha uma cesta que pode estar vazia ou não. Cada cesta será uma lista encadeada:

```python
# hashtable.py

class Node:
    def __init__(self, key, value, next=None):
        self.key = key
        self.value = value
        self.next = next

class HashTable:
    DELETED = object()

    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if capacity < 1:
            raise ValueError("A capacidade deve ser um número positivo")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("O fator de carga deve ser um número entre (0, 1]")
        self._buckets = capacity * [None]
        self._load_factor_threshold = load_factor_threshold

    @property
    def load_factor(self):
        occupied_or_deleted = [bucket for bucket in self._buckets if bucket is not None]
        return len(occupied_or_deleted) / len(self._buckets)

    def _resize_and_rehash(self):
        new_capacity = len(self._buckets) * 2
        new_buckets = new_capacity * [None]

        for bucket in self._buckets:
            current = bucket
            while current:
                index = hash(current.key) % new_capacity
                new_buckets[index] = Node(current.key, current.value, new_buckets[index])
                current = current.next

        self._buckets = new_buckets

    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        index = hash(key) % len(self._buckets)
        if self._buckets[index] is None:
            self._buckets[index] = Node(key, value)
        else:
            current = self._buckets[index]
            while current.next:
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            current.next = Node(key, value)

    def __getitem__(self, key):
        index = hash(key) % len(self._buckets)
        current = self._buckets[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)

    def __delitem__(self, key):
        index = hash(key) % len(self._buckets)
        current = self._buckets[index]
        previous = None

        while current:
            if current.key == key:
                if previous is None:
                    self._buckets[index] = current.next
                else:
                    previous.next = current.next
                return
            previous, current = current, current.next

        raise KeyError(key)
```

Agora, a classe HashTable usa o método de encadeamento separado para lidar com colisões de hash. Os pares de chave-valor com chaves colidentes são armazenados em listas encadeadas dentro dos "buckets" correspondentes. A função `hash()` é usada para determinar o índice do "bucket" apropriado. O método `_resize_and_rehash()` é chamado automaticamente quando o fator de carga atinge um determinado limiar, aumentando a capacidade da tabela de hash e reorganizando os pares existentes.
Tradução:

As instâncias de `Deque` cuidam de atualizar suas referências internas quando você exclui um item por índice. Se você estivesse usando uma lista vinculada personalizada, teria que reconfigurar manualmente os pares de chave-valor colididos após cada modificação. Como antes, atualizar um par de chave-valor existente requer a substituição do antigo por um completamente novo, pois os pares de chave-valor são imutáveis.

Se deseja evitar repetições, tente refatorar os três métodos acima usando o padrão estrutural de correspondência, introduzido no Python 3.10. Você encontrará uma possível solução nos materiais acompanhantes.

Ok, agora você sabe como lidar com colisões de códigos hash, e está pronto para avançar. A próxima etapa é fazer com que sua tabela de hash retorne chaves e valores na ordem de inserção.
Tradução:

**Manter a Ordem de Inserção em uma Tabela de Hash**

Porque a estrutura de dados clássica de tabela de hash usa hash para distribuir as chaves uniformemente e, às vezes, pseudo-aleatoriamente, ela não pode garantir sua ordem. Como uma regra prática, você nunca deve assumir que os elementos da tabela de hash virão em uma ordem consistente quando você os solicitar. Mas às vezes pode ser útil ou até necessário impor uma ordem específica nos elementos.

Até o Python 3.6, a única maneira de impor uma ordem aos elementos de um dicionário era usar o encapsulamento `OrderedDict` da biblioteca padrão. Mais tarde, o tipo de dados dict incorporado começou a preservar a ordem de inserção dos pares chave-valor. Independentemente disso, ainda pode ser sábio assumir a falta de ordem dos elementos para tornar seu código compatível com versões mais antigas ou alternativas do Python.

Como replicar uma preservação de ordem de inserção semelhante em sua classe de tabela de hash personalizada? Uma maneira poderia ser lembrar a sequência de chaves conforme você as insere e iterar sobre essa sequência para retornar chaves, valores e pares. Comece declarando outro campo interno em sua classe:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __init__(self, capacity=8, load_factor_threshold=0.6):
        if capacity < 1:
            raise ValueError("Capacity must be a positive number")
        if not (0 < load_factor_threshold <= 1):
            raise ValueError("Load factor must be a number between (0, 1]")
        self._keys = []
        self._buckets = [deque() for _ in range(capacity)]
        self._load_factor_threshold = load_factor_threshold
```

É uma lista vazia de chaves que crescerá e encolherá conforme você modifica o conteúdo da tabela de hash:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    def __delitem__(self, key):
        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                del bucket[index]
                self._keys.remove(key)
                break
        else:
            raise KeyError(key)

    def __setitem__(self, key, value):
        if self.load_factor >= self._load_factor_threshold:
            self._resize_and_rehash()

        bucket = self._buckets[self._index(key)]
        for index, pair in enumerate(bucket):
            if pair.key == key:
                bucket[index] = Pair(key, value)
                break
        else:
            bucket.append(Pair(key, value))
            self._keys.append(key)
```

Você remove a chave quando não há mais um par chave-valor associado na tabela de hash. Por outro lado, você adiciona uma chave apenas quando insere um novo par chave-valor na tabela de hash pela primeira vez. Você não quer inserir uma chave quando faz uma atualização, porque isso resultaria em várias cópias da mesma chave.

A seguir, você pode alterar as três propriedades `.keys`, `.values` e `.pairs` para que sigam a mesma ordem das chaves inseridas:
Tradução:

A seguir, você pode alterar as três propriedades .keys, .values e .pairs para que sigam a mesma ordem das chaves inseridas:

```python
# hashtable.py

# ...

class HashTable:
    # ...

    @property
    def keys(self):
        return self._keys.copy()

    @property
    def values(self):
        return [self[key] for key in self.keys]

    @property
    def pairs(self):
        return [(key, self[key]) for key in self.keys]
```

Certifique-se de retornar uma cópia de suas chaves para evitar vazar a implementação interna. Além disso, observe que essas três propriedades agora retornam listas em vez de conjuntos porque você deseja que elas mantenham a ordem correta. Por sua vez, isso permite que você faça zip das chaves e valores para criar pares:

```python
>>> from hashtable import HashTable
>>> hash_table = HashTable.from_dict({
...     "hola": "hello",
...     98.6: 37,
...     False: True
... })

>>> hash_table.keys
['hola', 98.6, False]

>>> hash_table.values
['hello', 37, True]

>>> hash_table.pairs
[('hola', 'hello'), (98.6, 37), (False, True)]

>>> hash_table.pairs == list(zip(hash_table.keys, hash_table.values))
True
```

As chaves e os valores são sempre retornados na mesma ordem, para que, por exemplo, a primeira chave e o primeiro valor estejam mapeados entre si. Isso significa que você pode fazer zip neles, como no exemplo acima.

Agora você sabe como manter a ordem de inserção dos pares chave-valor na sua tabela de hash. Por outro lado, se você quiser classificá-los com critérios mais avançados, poderá seguir as mesmas técnicas de ordenação de um dicionário integrado. Não há código adicional para escrever neste ponto.
Tradução:

Use Chaves Hasháveis

Sua tabela de hash está completa e totalmente funcional agora. Ela pode mapear chaves arbitrários para valores usando a função hash() incorporada. Pode detectar e resolver colisões de códigos hash e até mesmo reter a ordem de inserção dos pares chave-valor. Teoricamente, você poderia usá-la em vez de dict do Python, sem notar muita diferença, exceto pelo desempenho inferior e, ocasionalmente, uma sintaxe mais detalhada.

Nota: Como mencionado anteriormente, raramente você precisará implementar uma estrutura de dados como uma tabela de hash você mesmo. O Python vem com muitas coleções úteis que têm desempenho incomparável e são testadas no campo por inúmeros desenvolvedores. Para estruturas de dados especializadas, você deve verificar o PyPI em busca de bibliotecas de terceiros antes de tentar criar a sua própria. Você economizará muito tempo e reduzirá significativamente o risco de bugs.

Até agora, você deu como certo que a maioria dos tipos integrados no Python pode funcionar como chaves de tabela de hash. No entanto, para usar qualquer implementação de tabela de hash na prática, você precisará restringir as chaves apenas a tipos hasháveis e entender as implicações ao fazer isso. Isso será especialmente útil quando você decidir incluir tipos de dados personalizados na equação.
Tradução:

Hashabilidade vs. Imutabilidade

Você aprendeu anteriormente que alguns tipos de dados, incluindo a maioria dos tipos de dados primitivos em Python, são hasháveis, enquanto outros não são. A principal característica da hashabilidade é a capacidade de calcular o código hash de um objeto específico:

```python
>>> hash(frozenset(range(10)))
3895031357313128696

>>> hash(set(range(10)))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    hash(set(range(10)))
TypeError: unhashable type: 'set'
```

Por exemplo, instâncias do tipo de dados frozenset em Python são hasháveis, enquanto conjuntos comuns não implementam a hashagem. A hashabilidade impacta diretamente se objetos de certos tipos podem se tornar chaves de dicionário ou membros de conjunto, já que ambas essas estruturas de dados usam internamente a função hash():

```python
>>> hashable = frozenset(range(10))
>>> {hashable: "conjunto de números"}
{frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9}): 'conjunto de números'}
>>> {hashable}
{frozenset({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})}

>>> inhashavel = set(range(10))
>>> {inhashavel: "conjunto de números"}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    {inhashavel: "conjunto de números"}
TypeError: unhashable type: 'set'
>>> {inhashavel}
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    {inhashavel}
TypeError: unhashable type: 'set'
```

Enquanto uma instância de frozenset é hashável, o conjunto correspondente com precisamente os mesmos valores não é. Esteja ciente de que ainda é possível usar um tipo de dado não hashável para os valores do dicionário. São as chaves do dicionário que devem ser capazes de calcular seus códigos hash correspondentes.

Nota: Quando você insere um objeto não hashável em um contêiner hashável, como um frozenset, esse contêiner também se torna não hashável.

A hashabilidade está intimamente relacionada à mutabilidade, ou à capacidade de alterar o estado interno de um objeto durante sua vida útil. A relação entre os dois é um pouco como mudar de endereço. Quando você se muda para outro lugar, você ainda é a mesma pessoa, mas seus velhos amigos podem ter dificuldade em tentar encontrar você.

Tipos não hasháveis em Python, como listas, conjuntos ou dicionários, acontecem de ser contêineres mutáveis, pois você pode modificar seus valores adicionando ou removendo elementos. Por outro lado, a maioria dos tipos de dados hasháveis integrados em Python são imutáveis. Isso significa que tipos mutáveis não podem ser hasháveis?

A resposta correta é que eles podem ser tanto mutáveis quanto hasháveis, mas raramente deveriam! Mutar uma chave resultaria na alteração de seu endereço de memória dentro de uma tabela de hash. Considere esta classe personalizada como exemplo:
Tradução:

A resposta correta é que eles podem ser tanto mutáveis quanto hasháveis, mas raramente deveriam ser! Mutar uma chave resultaria na alteração de seu endereço de memória dentro de uma tabela de hash. Considere esta classe personalizada como exemplo:

```python
>>> class Pessoa:
...     def __init__(self, nome):
...         self.nome = nome
```

Esta classe representa uma pessoa com um nome. O Python fornece uma implementação padrão para o método especial .__hash__() em suas classes, que simplesmente usa a identidade do objeto para derivar seu código hash:

```python
>>> hash(Pessoa("Joe"))
8766622471691

>>> hash(Pessoa("Joe"))
8766623682281
```

Cada instância individual da Pessoa tem um código hash único, mesmo quando é logicamente igual a outras instâncias. Para fazer com que o valor do objeto determine seu código hash, você pode substituir a implementação padrão de .__hash__() da seguinte forma:

```python
>>> class Pessoa:
...     def __init__(self, nome):
...         self.nome = nome
...
...     def __hash__(self):
...         return hash(self.nome)

>>> hash(Pessoa("Joe")) == hash(Pessoa("Joe"))
True
```

Você chama hash() no atributo .nome para garantir que instâncias da classe Pessoa com nomes iguais sempre tenham o mesmo código hash. Isso é conveniente para procurá-las em um dicionário, por exemplo.

Nota: Você pode marcar explicitamente sua classe como não hashável configurando seu atributo .__hash__ como None:

```python
>>> class Pessoa:
...     __hash__ = None
...
...     def __init__(self, nome):
...         self.nome = nome

>>> hash(Pessoa("Alice"))
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    hash(Pessoa("Alice"))
TypeError: unhashable type: 'Person'
```

Isso impedirá que o hash() funcione em instâncias da sua classe.

Outra característica de tipos hasháveis é a capacidade de comparar suas instâncias por valor. Lembre-se de que uma tabela de hash compara chaves com o operador de teste de igualdade (==), portanto, você deve implementar outro método especial, .__eq__(), em sua classe para permitir isso:

```python
>>> class Pessoa:
...     def __init__(self, nome):
...         self.nome = nome
...
...     def __eq__(self, outro):
...         if self is outro:
...             return True
...         if type(self) is not type(outro):
...             return False
...         return self.nome == outro.nome
...
...     def __hash__(self):
...         return hash(self.nome)
```

Este fragmento de código deve parecer familiar se você passou pelo teste de igualdade de tabelas de hash antes. Em resumo, você verifica se o outro objeto é exatamente a mesma instância, uma instância de outro tipo ou outra instância do mesmo tipo e valor igual ao atributo .nome.
Tradução:

Este fragmento de código deve parecer familiar se você passou pelo teste de igualdade de tabelas de hash antes. Em resumo, você verifica se o outro objeto é exatamente a mesma instância, uma instância de outro tipo, ou outra instância do mesmo tipo e valor igual ao atributo .nome.

Nota: Codificar métodos especiais como .__eq__() e .__hash__() pode ser repetitivo, tedioso e propenso a erros. Se você estiver no Python 3.7 ou superior, então você pode alcançar o mesmo efeito de forma mais compacta usando data classes:

```python
@dataclass(unsafe_hash=True)
class Pessoa:
    nome: str
```

Enquanto uma data class gera .__eq__() com base nos atributos de sua classe, você deve definir a opção unsafe_hash para habilitar a geração correta do método .__hash__().

Tendo implementado .__eq__() e .__hash__(), você pode usar instâncias da classe Pessoa como chaves de dicionário:

```python
>>> alice = Pessoa("Alice")
>>> bob = Pessoa("Bob")

>>> funcionarios = {alice: "gerente de projeto", bob: "engenheiro"}

>>> funcionarios[bob]
'engenheiro'

>>> funcionarios[Pessoa("Bob")]
'engenheiro'
```

Perfeito! Não importa se você encontra um funcionário pela referência bob que você criou anteriormente ou por uma instância completamente nova Pessoa("Bob"). Infelizmente, as coisas complicam quando Bob decide mudar seu nome para Bobby:

```python
>>> bob.nome = "Bobby"

>>> funcionarios[bob]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    funcionarios[bob]
KeyError: <__main__.Pessoa object at 0x7f607e325e40>

>>> funcionarios[Pessoa("Bobby")]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    funcionarios[Pessoa("Bobby")]
KeyError: <__main__.Pessoa object at 0x7f607e16ed10>

>>> funcionarios[Pessoa("Bob")]
Traceback (most recent call last):
  File "<input>", line 1, in <module>
    funcionarios[Pessoa("Bob")]
KeyError: <__main__.Pessoa object at 0x7f607e1769e0>
```

Você não tem mais uma maneira de recuperar o valor correspondente, mesmo que ainda esteja usando o objeto de chave original que você inseriu antes. O que é mais surpreendente, no entanto, é que você não pode acessar o valor por meio de um novo objeto de chave com o nome da pessoa atualizado ou com o antigo. Você consegue perceber por quê?

O código hash da chave original determinou em qual bucket o valor associado foi armazenado. Mutar o estado da sua chave fez com que seu código hash indicasse um bucket ou slot completamente diferente, que não contém o valor esperado. Mas usar uma chave com o nome antigo também não ajuda. Embora aponte para o bucket certo, a chave armazenada foi alterada, fazendo com que a comparação de igualdade entre "Bob" e "Bobby" avalie como Falso, em vez de corresponder.

Portanto, os códigos hash devem ser imutáveis para que o hashing funcione conforme o esperado. Como os códigos hash geralmente são derivados dos atributos de um objeto, seu estado deve ser fixo e nunca mudar ao longo do tempo. Na prática, isso também significa que os objetos destinados a serem chaves de tabelas de hash devem ser eles próprios imutáveis.

Para resumir, um tipo de dado hashável tem as seguintes características:

1. Possui um método .__hash__() para calcular o código hash da instância.
2. Possui um método .__eq__() para comparar instâncias por valor.
3. Possui códigos hash imutáveis, que não mudam durante a vida das instâncias.
4. Conforma-se ao contrato hash-equal.

A quarta e última característica dos tipos hasháveis é que eles devem cumprir o contrato hash-equal, sobre o qual você aprenderá mais na subseção seguinte. Em resumo, objetos com valores iguais devem ter códigos hash idênticos.
Tradução:

O Contrato Hash-Equal
Para evitar problemas ao usar classes personalizadas como chaves de tabelas de hash, elas devem cumprir o contrato hash-equal. Se houver uma coisa a lembrar sobre esse contrato, é que ao implementar .__eq__(), você sempre deve implementar um correspondente .__hash__(). A única vez que você não precisa implementar ambos os métodos é quando você usa um invólucro como uma data class ou uma tupla nomeada imutável que já faz isso por você.

Além disso, não implementar ambos os métodos pode ser aceitável, desde que você tenha certeza absoluta de que nunca usará objetos do seu tipo de dados como chaves de dicionário ou membros de conjunto. Mas você pode ter tanta certeza?

Nota: Se você não pode usar uma data class ou uma tupla nomeada e gostaria de comparar e fazer hash manualmente mais de um campo em uma classe, então os envolva em uma tupla:

```python
class Pessoa:
    def __init__(self, nome, data_nascimento, casado):
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.casado = casado

    def __hash__(self):
        return hash(self._campos)

    def __eq__(self, other):
        if self is other:
            return True
        if type(self) is not type(other):
            return False
        return self._campos == other._campos

    @property
    def _campos(self):
        return self.nome, self.data_nascimento, self.casado
```

Faz sentido definir uma propriedade privada para retornar essa tupla se houver relativamente muitos campos em sua classe.

Embora você possa implementar ambos os métodos da maneira que preferir, eles devem satisfazer o contrato hash-equal, que afirma que dois objetos iguais devem ter códigos hash iguais. Isso torna possível encontrar o bucket certo com base em uma chave fornecida. No entanto, o inverso não é verdadeiro, porque colisões ocasionalmente podem fazer com que o mesmo código hash seja compartilhado por valores desiguais. Você pode expressar isso de forma mais formal usando essas duas implicações:

1. a = b ⇒ hash(a) = hash(b)
2. hash(a) = hash(b) ⇏ a = b

O contrato hash-equal é unidirecional. Se duas chaves são logicamente iguais, então seus códigos hash também devem ser iguais. Por outro lado, se duas chaves compartilham o mesmo código hash, é provável que sejam a mesma chave, mas também é possível que sejam chaves diferentes. Você precisa compará-las para ter certeza se realmente correspondem. Pela lei da contraposição, você pode derivar outra implicação a partir da primeira:

3. hash(a) ≠ hash(b) ⇒ a ≠ b

Se você souber que duas chaves têm códigos hash diferentes, então não há sentido em compará-las. Isso pode ajudar a melhorar o desempenho, já que o teste de igualdade tende a ser custoso.

Alguns IDEs oferecem a geração automática dos métodos .__hash__() e .__eq__(), mas você precisa se lembrar de regenerá-los sempre que modificar os atributos da sua classe. Portanto, adote as data classes ou tuplas nomeadas do Python sempre que possível para garantir a implementação adequada de tipos hasháveis.
Conclusão
Neste ponto, você pode implementar uma tabela de hash do zero em Python, utilizando diferentes estratégias para resolver colisões de hash. Você sabe como fazer sua tabela de hash redimensionar e reorganizar dinamicamente para acomodar mais dados e como preservar a ordem de inserção de pares chave-valor. Ao longo do caminho, você praticou o desenvolvimento orientado por testes (TDD) adicionando recursos à sua tabela de hash passo a passo.

Além disso, você possui uma compreensão profunda da função hash() integrada do Python e pode criar uma própria. Você entende o contrato hash-equal, a diferença entre tipos de dados hasháveis e não hasháveis, e sua relação com tipos imutáveis. Você sabe como criar classes hasháveis personalizadas usando várias ferramentas em Python.

Neste tutorial, você aprendeu:

- Como uma tabela de hash difere de um dicionário.
- Como implementar uma tabela de hash do zero em Python.
- Como lidar com colisões de hash e outros desafios.
- Quais são as propriedades desejadas de uma função de hash.
- Como a função hash() do Python funciona nos bastidores.

Com esse conhecimento, você está preparado para responder à maioria das perguntas que pode encontrar em uma entrevista de emprego relacionada à estrutura de dados da tabela de hash.

Você pode baixar o código-fonte completo e os passos intermediários usados ao longo deste tutorial clicando no link abaixo:


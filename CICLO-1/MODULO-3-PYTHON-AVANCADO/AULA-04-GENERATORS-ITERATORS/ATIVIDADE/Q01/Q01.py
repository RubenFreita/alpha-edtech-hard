
class Fibonacci:
    def __init__(self, maximo=1000000):
        # Inicializa os dois primeiros numeros que são o caso base do fibonacci
        #nesse caso o elemento atual começa com 0 e o proximo elemento
        # começa com o numero 1 que será o proximo numero fibonacci
        self.elemento_atual, self.proximo_elemento = 0, 1
        # atribui o valor máximo do fibonacci
        self.maximo = maximo

    # método que retorna o objeto iterável, que no caso é ele mesmo
    # o self
    def __iter__(self):
        return self

    #função que irá percorrer o iterável avançar para o próximo elemento 
    #no iterável
    def __next__(self):
        # verifica que o elemento atual é maior que o maior elemento fibonacci
        # que foi passado pelo usuário se for ele retorna o 
        # Fim da iteração, raise StopIteration
        if self.elemento_atual > self.maximo:
            raise StopIteration

        # Salva o valor do elemento atual no valor a ser retornado na função
        valor_de_retorno = self.elemento_atual

        # atribui o próximo elemento que já foi calculado no init ou na última chamada da
        #  função next no elemento atual e calcula o próximo valor de fibonacci que será o 
        #o próximo elemento e o elemento atual
        self.elemento_atual, self.proximo_elemento = \
            self.proximo_elemento, self.elemento_atual + self.proximo_elemento

        #retorna o valor que foi salvo antes de calcular os novos valores de elemento atual
        # e proximo elemento
        return valor_de_retorno
        
# Executa nosso código
if __name__ == '__main__':
  # Cria nosso objeto iterável
    objeto_fibonacci = Fibonacci(maximo=1000000)

  # Itera nossa sequencia e mostra os resultados
    for fibonacci in objeto_fibonacci:
        print("Sequencia: {}".format(fibonacci))
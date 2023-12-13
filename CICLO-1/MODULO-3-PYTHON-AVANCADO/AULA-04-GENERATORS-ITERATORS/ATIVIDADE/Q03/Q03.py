class SquaresIterator:
    def __init__(self, max_num):
        self.max_num = max_num
        self.current = 0
        self.lista = []

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.max_num:
            result = self.current ** 2
            self.current += 1
            self.lista.append(result)
            return result
        else:
            raise StopIteration  # Sinaliza o final da iteração
        
    def __str__(self):
        return str(self.lista)


# Exemplo de uso
squares_iter = SquaresIterator(5)

#criando uma lista usando o iterator
lista = list(squares_iter)
print(type(lista))
print(lista)


print(type(squares_iter))
print(squares_iter)
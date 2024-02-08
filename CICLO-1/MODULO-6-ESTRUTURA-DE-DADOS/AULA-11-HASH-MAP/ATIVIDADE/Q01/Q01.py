# @title `Exemplo de Código` { display-mode: "form" }


class SistemaRastreamento:
    def __init__(self, size=10):
        self.size = size
        self.pedidos = {}  # Inicializa um hashmap para armazenar os pedidos
        self.buckets = [[] for _ in range(size)]
        self.qtd_items = 0

    def hash_function(self, key):
        # Uma função hash simples baseada no comprimento da chave
        return len(key) % self.size

    def adicionar_pedido(self, codigo, status):
        index = self.hash_function(codigo)
        bucket = self.buckets[index]
        found_key = False
        for item in bucket:
            if item[0] == codigo:

                print(f"Código de rastreamento {codigo} já existe.")
                found_key = True
                break
        if not found_key:
            self.qtd_items += 1
            bucket.append(
                (codigo, [status])
            )  # Cria uma nova lista de valores para uma nova chave
            print(f"Pedido {codigo} adicionado com status: {status}.")

    def atualizar_status(self, codigo, status):
        index = self.hash_function(codigo)
        bucket = self.buckets[index]
        found_key = False
        for item in bucket:
            if item[0] == codigo:
                item[1][
                    0
                ] = status  # Adiciona o valor à lista de valores para esta chave
                print(f"Status do pedido {codigo} atualizado para: {status}.")
                found_key = True
                break
        if not found_key:

            print(f"Pedido com código {codigo} não encontrado.")

    def consultar_status(self, codigo):
        index = self.hash_function(codigo)
        bucket = self.buckets[index]
        for item in bucket:
            if item[0] == codigo:

                return f"O status do pedido {codigo} é: " + item[1][0]
        return "Pedido não encontrado."

    def rehashing(self):
        if self.id >= self.size * 0.7:
            self.size *= 2

    def apagar_pedido(self, codigo):
        index = self.hash_function(codigo)
        bucket = self.buckets[index]
        found_key = False
        for i in range(len(bucket)):
            if bucket[i][0] == codigo:
                del bucket[i]

                return f"Pedido {codigo} apagado com sucesso."
        return f"Pedido {codigo} não encontrado."


# Exemplo de uso
sistema = SistemaRastreamento()
sistema.adicionar_pedido("123ABC", "Recebido")
sistema.atualizar_status("123ABC", "Em processamento")
sistema.adicionar_pedido("456DEF", "Recebido")  # pedido deve dar colisão
sistema.adicionar_pedido("1234", "Recebido")
sistema.adicionar_pedido("1EF", "Recebido")
sistema.adicionar_pedido("12DEF", "Recebido")
sistema.adicionar_pedido("F", "Recebido")
sistema.adicionar_pedido("IU", "Recebido")
print(sistema.consultar_status("123ABC"))  # Deve exibir "Em processamento"
print(sistema.consultar_status("456DEF"))

print(sistema.apagar_pedido("IU"))

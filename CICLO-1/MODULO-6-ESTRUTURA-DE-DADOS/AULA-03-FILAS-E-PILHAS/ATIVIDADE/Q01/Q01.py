import random
from prettytable import PrettyTable


class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        return self.itens.pop(0) if not self.is_empty() else None

    def front(self):
        return self.itens[0] if not self.is_empty() else None

    def is_empty(self):
        return len(self.itens) == 0

    def size(self):
        return len(self.itens)


class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome


class Atendimento:
    id = 0

    def __init__(self) -> None:
        self.fila_atendimento = Fila()
        self.cliente_em_atendimento = None

    def adicionar_cliente_fila(self, cliente: Cliente):
        self.id = Atendimento.id
        Atendimento.id += 1
        if self.cliente_em_atendimento == None:
            self.fila_atendimento.enqueue(
                {
                    "id": self.id,
                    "cliente": cliente,
                    "tempo_estimado_espera": self.fila_atendimento.size() * 10,
                    "tempo_real_espera": 0,
                    "tempo_atendimento": 0,
                    "tempo_espera_restante": self.fila_atendimento.size() * 10,
                }
            )
        else:
            self.fila_atendimento.enqueue(
                {
                    "id": self.id,
                    "cliente": cliente,
                    "tempo_estimado_espera": (self.fila_atendimento.size()) * 10
                    + self.cliente_em_atendimento["tempo_atendimento"],
                    "tempo_real_espera": 0,
                    "tempo_atendimento": 0,
                    "tempo_espera_restante": (self.fila_atendimento.size()) * 10
                    + self.cliente_em_atendimento["tempo_atendimento"],
                }
            )

        print(f"INFO: O cliente {cliente.nome} chegou na fila.")

    def atender_prox_cliente(self):
        self.cliente_em_atendimento = (
            self.fila_atendimento.dequeue()
            if not self.fila_atendimento.is_empty()
            else None
        )
        self.cliente_em_atendimento["tempo_atendimento"] = random.randint(1, 10)
        for i in self.fila_atendimento.itens:
            i["tempo_real_espera"] += self.cliente_em_atendimento["tempo_atendimento"]
            indice = self.fila_atendimento.itens.index(i)
            i["tempo_espera_restante"] = (
                10 * (indice) + self.cliente_em_atendimento["tempo_atendimento"]
            )
        print(
            f"INFO: O cliente {self.cliente_em_atendimento['cliente'].nome} foi chamado para sala de atendimento"
        )

    def fila_esta_vazia(self):
        return self.fila_atendimento.is_empty()

    def listar_clientes_fila(self):
        # Aqui eu instancio a tabela
        tabela = PrettyTable()
        tabela.title = "Fila De Atendimento"

        # Aqui eu defino os nomes das colunas
        tabela.field_names = [
            "Código",
            "Nome do Cliente",
            "Tempo Estimado de Espera",
            "Tempo de Espera Até o Momento",
            "Tempo de Espera Restante",
        ]

        # e aqui ele vai preenchendo as linhas dentro do for
        for cliente in self.fila_atendimento.itens:
            tabela.add_row(
                [
                    cliente["id"],
                    cliente["cliente"].nome,
                    str(cliente["tempo_estimado_espera"]) + " Minutos",
                    str(cliente["tempo_real_espera"]) + " Minutos",
                    str(cliente["tempo_espera_restante"]) + " Minutos",
                ]
            )

        print(tabela, end="\n\n")

    def informacoes_cliente_atendimento_atual(self):
        if self.cliente_em_atendimento != None:
            tabela = PrettyTable()

            tabela.title = "Cliente Em Atendimento"

            # Aqui eu defino os nomes das colunas
            tabela.field_names = [
                "Código",
                "Nome do Cliente",
                "Tempo de Atendimento",
                "Tempo Estimado de Espera",
                "Tempo de Espera Real",
            ]

            # e aqui ele vai preenchendo as linhas dentro do for
            tabela.add_row(
                [
                    self.cliente_em_atendimento["id"],
                    self.cliente_em_atendimento["cliente"].nome,
                    str(self.cliente_em_atendimento["tempo_atendimento"]) + " Minutos",
                    str(self.cliente_em_atendimento["tempo_estimado_espera"])
                    + " Minutos",
                    str(self.cliente_em_atendimento["tempo_real_espera"]) + " Minutos",
                ]
            )

            print(tabela, end="\n\n")
        else:
            print("\n======= Cliente Em Atendimento =======")
            print("INFO: Nenhum Cliente em Atendimento")


def adicionar_clientes_fila(clientes, atendimento: Atendimento):
    for i in clientes:
        atendimento.adicionar_cliente_fila(Cliente(i))
    # return atendimento


def atender_20_clientes(atendimento: Atendimento):
    for _ in range(20):
        if atendimento.fila_esta_vazia():
            print("INFO: Não há clientes na fila para atender.")
            atendimento.cliente_em_atendimento = None
        else:
            atendimento.atender_prox_cliente()


def menu(atendimento: Atendimento, clientes: list):
    atendimento = Atendimento()
    flag = False
    while True:
        print("\n======= Menu de Atendimento =======")
        print("1. Adicionar Cliente à Fila")
        print("2. Atender Próximo Cliente")
        print("3. Listar Clientes na Fila")
        print("4. Informações do Cliente em Atendimento")
        print("5. Adicionar 25 Clientes Aleatórios na Fila")
        print("6. Atender Próximos 20 Clientes da fila")
        print("0. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome_cliente = input("Digite o nome do cliente: ")
            atendimento.adicionar_cliente_fila(Cliente(nome_cliente))
        elif escolha == "2":
            if atendimento.fila_esta_vazia():
                print("INFO: Não há clientes na fila para atender.")
                atendimento.cliente_em_atendimento = None
            else:
                atendimento.atender_prox_cliente()
        elif escolha == "3":
            if atendimento.fila_esta_vazia():
                print("INFO: A fila está vazia.")
            else:
                atendimento.listar_clientes_fila()
        elif escolha == "4":
            atendimento.informacoes_cliente_atendimento_atual()
        elif escolha == "5":
            if flag == False:
                flag = True
                adicionar_clientes_fila(clientes, atendimento)
            else:
                print("INFO: Os clientes aleatórios já form adicionados na fila.")
        elif escolha == "6":
            atender_20_clientes(atendimento)
        elif escolha == "0":
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")


clientes = [
    "Ana",
    "Bruno",
    "Carla",
    "Daniel",
    "Eduarda",
    "Felipe",
    "Gabriela",
    "Heitor",
    "Isabela",
    "João",
    "Karina",
    "Lucas",
    "Mariana",
    "Nícolas",
    "Olívia",
    "Paulo",
    "Quezia",
    "Rafael",
    "Sofia",
    "Tiago",
    "Ursula",
    "Vítor",
    "Wesley",
    "Xuxa",
    "Yasmin",
]

if __name__ == "__main__":
    atendimento = Atendimento()
    # adicionar_clientes_fila(clientes, atendimento)

    # print("\n\nINFO: Mostrando Resultados Antes Do Primeiro Cliente Ser Atendido:")

    # atendimento.informacoes_cliente_atendimento_atual()
    # atendimento.listar_clientes_fila()

    # # For para atender 20 clientes
    # for _ in range(20):
    #     atendimento.atender_prox_cliente()

    # print("\n\nINFO: Mostrando Resultados Depois De Atender 20 Clientes:")

    # atendimento.informacoes_cliente_atendimento_atual()
    # atendimento.listar_clientes_fila()

    # print("INFO: Verificando se a fila está vazia.")
    # print(atendimento.fila_esta_vazia())

    # atendimento.adicionar_cliente_fila(Cliente("Ruben"))

    # atendimento.informacoes_cliente_atendimento_atual()
    # atendimento.listar_clientes_fila()
    # atendimento.atender_prox_cliente()
    # atendimento.listar_clientes_fila()
    menu(atendimento, clientes)

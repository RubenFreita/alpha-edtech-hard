class ContaBancaria:
    def __init__(self, saldo):
        self.__saldo = saldo  # Atributo protegido

    @property
    def saldo(self):
        return self.__saldo  # Método getter

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor

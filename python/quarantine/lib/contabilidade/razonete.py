#
# O :Razonete foi pensado para contar listas de :LancamentoContabil,
# uma para débitos e outra para créditos.
#
class Razonete:
    def __init__(self):
        super().__init__()
        self.debitos = []
        self.creditos = []

    def add_debito(self, debito):
        self.debitos.append(debito)

    def add_debitos(self, debitos):
        for debito in debitos:
            self.debitos.append(debito)

    def add_credito(self, credito):
        self.creditos.append(credito)

    def add_creditos(self, creditos):
        for credito in creditos:
            self.creditos.append(credito)

    def get_total_debitos(self):
        total_debitos = 0

        for debito in self.debitos:
            total_debitos += debito.valor

        return total_debitos

    def get_total_creditos(self):
        total_creditos = 0

        for credito in self.creditos:
            total_creditos += credito.valor

        return total_creditos

    def is_saldo_credor(self):
        return self.get_total_creditos() > self.get_total_debitos()

    def is_saldo_devedor(self):
        return self.get_total_creditos() < self.get_total_debitos()

    def __str__(self):
        repr = '\n\tRazonete:'
        repr += '\n\tTotal de débitos: {:.2f}\n\tTotal de créditos: {:.2f}'.format(
                self.get_total_debitos(),
                self.get_total_creditos())
        return repr

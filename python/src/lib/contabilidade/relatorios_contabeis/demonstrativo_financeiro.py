class DemonstrativoFinanceiro:
    def __init__(self, plano_de_contas):
        super().__init__()
        self.plano_de_contas = plano_de_contas


class DemonstrativoFinanceiroAnual:
    def __init__(self, plano_de_contas, ano):
        super().__init__(plano_de_contas)
        self.ano = ano

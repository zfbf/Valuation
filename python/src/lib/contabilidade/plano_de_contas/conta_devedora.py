from .conta import Conta
from ..natureza import Natureza


class ContaDevedora(Conta):
    def __init__(self, codigo, nome, parent=None):
        super().__init__(codigo, nome, Natureza.DEVEDORA, parent)
        self.codigo = codigo
        self.nome = nome

    def get_saldo(self):
        return super().get_total_debitos() - super().get_total_creditos()

    def increase_saldo(self, lancamento):
        super().add_debito(lancamento)

    def decrease_saldo(self, lancamento):
        super().add_credito(lancamento)

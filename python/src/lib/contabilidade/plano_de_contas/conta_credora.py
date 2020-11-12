from .conta import Conta
from ..natureza import Natureza


class ContaCredora(Conta):
    def __init__(self, codigo, nome, parent=None):
        super().__init__(codigo, nome, Natureza.CREDORA, parent)
        self.codigo = codigo
        self.nome = nome

    def get_saldo(self):
        return super().get_total_creditos() - super().get_total_debitos()

    def increase_saldo(self, lancamento):
        super().add_credito(lancamento)

    def decrease_saldo(self, lancamento):
        super().add_debito(lancamento)

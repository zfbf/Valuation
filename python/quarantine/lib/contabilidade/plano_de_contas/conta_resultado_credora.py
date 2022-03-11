from .grupo_contas import GrupoContas
from ..natureza import Natureza


class ContaResultadoCredora(GrupoContas):
    def __init__(self, codigo, nome, parent=None):
        super().__init__(codigo, nome, Natureza.CREDORA, parent)
        self.codigo = codigo
        self.nome = nome

    def get_saldo(self):
        creditos = 0
        debitos = 0

        for conta in self.contas:
            creditos += conta.get_total_creditos()
            debitos += conta.get_total_debitos()

        return creditos - debitos

    def increase_saldo(self, lancamento):
        super().add_credito(lancamento)

    def decrease_saldo(self, lancamento):
        super().add_debito(lancamento)

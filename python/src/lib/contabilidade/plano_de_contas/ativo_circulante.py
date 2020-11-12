from .conta_devedora import ContaDevedora
from .grupo_contas import GrupoContas
from ..natureza import Natureza


class AtivoCirculante(GrupoContas):
    def __init__(self, parent):
        super().__init__('circulante', 'Circulante', Natureza.DEVEDORA, parent)
        self.init_conta_caixa()

    def init_conta_caixa(self):
        self.add_conta(ContaDevedora('caixa', 'caixa', self))

    def rename_conta_caixa(self, nome):
        self.get_conta('caixa').rename_conta(nome)

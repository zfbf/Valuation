from .conta_devedora import ContaDevedora
from .grupo_contas import GrupoContas


class AtivoCirculante(GrupoContas):
    def __init__(self):
        super().__init__('ativo_circulante', 'Circulante')
        self.init_conta_caixa()

    def init_conta_caixa(self):
        self.add_conta(ContaDevedora('caixa', 'caixa'))

    def rename_conta_caixa(self, nome):
        self.get_conta('caixa').rename_conta(nome)

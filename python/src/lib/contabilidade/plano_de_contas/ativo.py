from .grupo_contas import GrupoContas
from .ativo_circulante import AtivoCirculante
from .ativo_nao_circulante import AtivoNaoCirculante


class Ativo(GrupoContas):
    def __init__(self):
        super().__init__('ativo', 'Ativo')
        self.circulante = AtivoCirculante()
        self.add_conta(self.circulante)
        self.nao_circulante = AtivoNaoCirculante()
        self.add_conta(self.nao_circulante)

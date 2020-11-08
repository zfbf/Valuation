from .grupo_contas import GrupoContas
from .ativo_circulante import AtivoCirculante
from .ativo_nao_circulante import AtivoNaoCirculante


class Ativo(GrupoContas):
    def __init__(self):
        super().__init__('ativo', 'Ativo', None)
        self.circulante = AtivoCirculante(self)
        self.add_conta(self.circulante)
        self.nao_circulante = AtivoNaoCirculante(self)
        self.add_conta(self.nao_circulante)

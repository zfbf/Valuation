from .grupo_contas import GrupoContas
from .passivo_circulante import PassivoCirculante
from .passivo_nao_circulante import PassivoNaoCirculante


class Passivo(GrupoContas):
    def __init__(self):
        super().__init__('passivo', 'Passivo', None)
        self.circulante = PassivoCirculante(self)
        self.add_conta(self.circulante)
        self.nao_circulante = PassivoNaoCirculante(self)
        self.add_conta(self.nao_circulante)

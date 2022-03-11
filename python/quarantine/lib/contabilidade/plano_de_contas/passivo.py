from abc import ABC, abstractmethod

from .grupo_contas import GrupoContas
from .passivo_circulante import PassivoCirculante
from .passivo_nao_circulante import PassivoNaoCirculante
from ..natureza import Natureza


class Passivo(GrupoContas, ABC):
    def __init__(self):
        super().__init__('passivo', 'Passivo', Natureza.CREDORA, None)
        self.circulante = self.build_passivo_circulante()
        self.add_conta(self.circulante)
        self.nao_circulante = self.build_passivo_nao_circulante()
        self.add_conta(self.nao_circulante)

    @abstractmethod
    def build_passivo_circulante(self):
        pass

    @abstractmethod
    def build_passivo_nao_circulante(self):
        pass

    def init_contas(self):
        self.circulante.init_contas()
        self.nao_circulante.init_contas()

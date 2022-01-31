from abc import ABC, abstractmethod

from .grupo_contas import GrupoContas
from .ativo_circulante import AtivoCirculante
from .ativo_nao_circulante import AtivoNaoCirculante
from ..natureza import Natureza


class Ativo(GrupoContas, ABC):
    def __init__(self):
        super().__init__('ativo', 'Ativo', Natureza.DEVEDORA, None)

    @abstractmethod
    def build_ativo_circulante(self):
        pass

    @abstractmethod
    def build_ativo_nao_circulante(self):
        pass

    def get_contas_disponibilidades(self):
        return self.circulante.get_contas_disponibilidades()

    def init_contas(self):
        self.circulante = self.build_ativo_circulante()
        self.add_conta(self.circulante)
        self.circulante.init_conta_caixa()
        self.circulante.init_contas()
        self.nao_circulante = self.build_ativo_nao_circulante()
        self.add_conta(self.nao_circulante)
        self.nao_circulante.init_contas()

from abc import ABC, abstractmethod

from .grupo_contas import GrupoContas
from ..natureza import Natureza


class AtivoNaoCirculante(GrupoContas, ABC):
    def __init__(self, parent):
        super().__init__('nao_circulante', 'Não Circulante',
                Natureza.DEVEDORA, parent)

    @abstractmethod
    def init_contas(self):
        pass

    @abstractmethod
    def get_conta_realizavel_a_longo_prazo(self):
        pass

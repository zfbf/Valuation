from abc import ABC, abstractmethod

from .grupo_contas import GrupoContas
from ..natureza import Natureza


class PassivoNaoCirculante(GrupoContas, ABC):
    def __init__(self, parent):
        super().__init__('nao_circulante', 'Não Circulante',
                Natureza.CREDORA, parent)

    @abstractmethod
    def init_contas(self):
        pass

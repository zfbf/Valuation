from abc import ABC, abstractmethod

from .grupo_contas import GrupoContas
from ..natureza import Natureza


class PassivoCirculante(GrupoContas, ABC):
    def __init__(self, parent):
        super().__init__('circulante', 'Circulante',
                Natureza.CREDORA, parent)

    @abstractmethod
    def init_contas(self):
        pass

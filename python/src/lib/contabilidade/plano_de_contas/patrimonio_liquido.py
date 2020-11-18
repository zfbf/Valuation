from abc import ABC, abstractmethod

from .grupo_contas import GrupoContas
from ..natureza import Natureza


class PatrimonioLiquido(GrupoContas, ABC):
    def __init__(self):
        super().__init__('patrimonio_liquido', 'Patrimônio Líquido',
                Natureza.CREDORA, None)

    @abstractmethod
    def init_contas(self):
        pass

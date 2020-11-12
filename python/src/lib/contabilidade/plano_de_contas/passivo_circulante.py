from .grupo_contas import GrupoContas
from ..natureza import Natureza


class PassivoCirculante(GrupoContas):
    def __init__(self, parent):
        super().__init__('circulante', 'Circulante',
                Natureza.CREDORA, parent)

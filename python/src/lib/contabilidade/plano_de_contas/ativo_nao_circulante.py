from .grupo_contas import GrupoContas
from ..natureza import Natureza


class AtivoNaoCirculante(GrupoContas):
    def __init__(self, parent):
        super().__init__('nao_circulante', 'Não Circulante',
                Natureza.DEVEDORA, parent)

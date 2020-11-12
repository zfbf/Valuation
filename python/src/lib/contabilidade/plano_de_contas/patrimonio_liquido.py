from .grupo_contas import GrupoContas
from ..natureza import Natureza


class PatrimonioLiquido(GrupoContas):
    def __init__(self):
        super().__init__('patrimonio_liquido', 'Patrimônio Líquido',
                Natureza.CREDORA, None)

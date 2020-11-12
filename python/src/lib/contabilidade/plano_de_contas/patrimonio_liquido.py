from .grupo_contas import GrupoContas


class PatrimonioLiquido(GrupoContas):
    def __init__(self):
        super().__init__('patrimonio_liquido', 'Patrimônio Líquido', None)

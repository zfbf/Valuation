from .grupo_contas import GrupoContas


class PassivoCirculante(GrupoContas):
    def __init__(self, parent):
        super().__init__('circulante', 'Circulante', parent)

from .grupo_contas import GrupoContas


class PassivoNaoCirculante(GrupoContas):
    def __init__(self, parent):
        super().__init__('nao_circulante', 'Não Circulante', parent)

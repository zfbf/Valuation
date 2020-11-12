from .grupo_contas import GrupoContas


class AtivoNaoCirculante(GrupoContas):
    def __init__(self, parent):
        super().__init__('nao_circulante', 'Não Circulante', parent)
        self.realizavel_longo_prazo = None
        

from ..ativo import Ativo
from .ativo_circulante import AtivoCirculanteDefault
from .ativo_nao_circulante import AtivoNaoCirculanteDefault


class AtivoDefault(Ativo):
    def __init__(self):
        super().__init__()

    def build_ativo_circulante(self):
        return AtivoCirculanteDefault(self)

    def build_ativo_nao_circulante(self):
        return AtivoNaoCirculanteDefault(self)

from ..ativo import Ativo
from .ativo_circulante import AtivoCirculanteIFRS
from .ativo_nao_circulante import AtivoNaoCirculanteIFRS


class AtivoIFRS(Ativo):
    def __init__(self):
        super().__init__()

    def build_ativo_circulante(self):
        return AtivoCirculanteIFRS(self)

    def build_ativo_nao_circulante(self):
        return AtivoNaoCirculanteIFRS(self)

from ..passivo import Passivo
from .passivo_circulante import PassivoCirculanteIFRS
from .passivo_nao_circulante import PassivoNaoCirculanteIFRS


class PassivoIFRS(Passivo):
    def __init__(self):
        super().__init__()

    def build_passivo_circulante(self):
        return PassivoCirculanteIFRS(self)

    def build_passivo_nao_circulante(self):
        return PassivoNaoCirculanteIFRS(self)

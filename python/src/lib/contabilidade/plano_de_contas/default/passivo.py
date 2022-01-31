from ..passivo import Passivo
from .passivo_circulante import PassivoCirculanteDefault
from .passivo_nao_circulante import PassivoNaoCirculanteDefault


class PassivoDefault(Passivo):
    def __init__(self):
        super().__init__()

    def build_passivo_circulante(self):
        return PassivoCirculanteDefault(self)

    def build_passivo_nao_circulante(self):
        return PassivoNaoCirculanteDefault(self)

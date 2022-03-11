from lib.contabilidade.plano_de_contas.passivo import Passivo
from .passivo_circulante_dummy import PassivoCirculanteDummy
from .passivo_nao_circulante_dummy import PassivoNaoCirculanteDummy


class PassivoDummy(Passivo):
    def __init__(self):
        super().__init__()

    def build_passivo_circulante(self):
        return PassivoCirculanteDummy(self)

    def build_passivo_nao_circulante(self):
        return PassivoNaoCirculanteDummy(self)

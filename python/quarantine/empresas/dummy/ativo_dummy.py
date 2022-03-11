from lib.contabilidade.plano_de_contas.ativo import Ativo
from .ativo_circulante_dummy import AtivoCirculanteDummy
from .ativo_nao_circulante_dummy import AtivoNaoCirculanteDummy


class AtivoDummy(Ativo):
    def __init__(self):
        super().__init__()

    def build_ativo_circulante(self):
        return AtivoCirculanteDummy(self)

    def build_ativo_nao_circulante(self):
        return AtivoNaoCirculanteDummy(self)

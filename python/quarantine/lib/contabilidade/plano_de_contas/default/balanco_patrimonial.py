from ..balanco_patrimonial import BalancoPatrimonial
from .ativo import AtivoDefault
from .passivo import PassivoDefault
from .patrimonio_liquido import PatrimonioLiquidoDefault


class BalancoPatrimonialDefault(BalancoPatrimonial):

    def build_ativo(self):
        self.ativo = AtivoDefault()

    def build_passivo(self):
        self.passivo = PassivoDefault()

    def build_patrimonio_liquido(self):
        self.patrimonio_liquido = PatrimonioLiquidoDefault()

from ..balanco_patrimonial import BalancoPatrimonial
from .ativo import AtivoIFRS
from .passivo import PassivoIFRS
from .patrimonio_liquido import PatrimonioLiquidoIFRS


class BalancoPatrimonialIFRS(BalancoPatrimonial):

    def build_ativo(self):
        self.ativo = AtivoIFRS()

    def build_passivo(self):
        self.passivo = PassivoIFRS()

    def build_patrimonio_liquido(self):
        self.patrimonio_liquido = PatrimonioLiquidoIFRS()

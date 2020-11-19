from .ativo_dummy import AtivoDummy
from .passivo_dummy import PassivoDummy
from .patrimonio_liquido_dummy import PatrimonioLiquidoDummy
from lib.contabilidade.plano_de_contas.plano_de_contas import PlanoDeContas


class PlanoDeContasDummy(PlanoDeContas):

    def build_ativo(self):
        self.ativo = AtivoDummy()

    def build_passivo(self):
        self.passivo = PassivoDummy()

    def build_patrimonio_liquido(self):
        self.patrimonio_liquido = PatrimonioLiquidoDummy()

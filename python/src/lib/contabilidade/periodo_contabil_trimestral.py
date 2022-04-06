from .plano_de_contas.ifrs.balanco_patrimonial import BalancoPatrimonialIFRS
from .plano_de_contas.dre import DRE
from .plano_de_contas.dfc import DFC
from .periodo_contabil import PeriodoContabil


#TODO: Tornar esta classe abstrata e implementar PeriodoContrabilTrimestral
#      PeriodoContabilAnual.

class PeriodoContabilTrimestral(PeriodoContabil):
    def __init__(self, ano, trimestre):
        super().__init__('{}T{}'.format(ano, trimestre))
        self.ano = ano
        self.trimestre = trimestre

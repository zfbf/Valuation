from .plano_de_contas.ifrs.balanco_patrimonial import BalancoPatrimonialIFRS
from .plano_de_contas.dre import DRE
from .plano_de_contas.dfc import DFC

#TODO: Tornar esta classe abstrata e implementar PeriodoContrabilTrimestral
#      PeriodoContabilAnual.

class PeriodoContabil():
    def __init__(self, identificador):
        super().__init__()
        self.identificador = identificador
        self.bp_ifrs = BalancoPatrimonialIFRS()
        self.dre = DRE()
        self.dfc = DFC()

    def get_identificador(self):
        return self.identificador

    def __str__(self):
        repr = "\nPeriodoContabil - {:s}".format(self.identificador)
        repr += "\n\tbp_ifrs: {}".format(self.bp_ifrs)
        repr += "\n\tdre: {}".format(self.dre)
        repr += "\n\tfc: {}".format(self.dfc)
        return repr

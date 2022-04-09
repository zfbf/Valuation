from datetime import date

from ..indice import Indice


class LiquidezImediata(Indice):
    def __init__(self, valuation, ano, trimestre):
        super().__init__('Liquidez Imediata', valuation, ano, trimestre)

    def get_valor(self):
        bp = super().get_periodo_contabil().bp_ifrs
        disponibilidades = bp.ativo.circulante.get_saldo_disponibilidades()
        passivo_circulante = bp.passivo.circulante
        liquidez_imediata = disponibilidades / passivo_circulante.get_saldo()
        return liquidez_imediata

    def str_comp(self):
        ativo_circulante = self.get_periodo_contabil().bp_ifrs.ativo.circulante
        repr = '\n\tativo_circulante: {}'.format(ativo_circulante)
        return repr

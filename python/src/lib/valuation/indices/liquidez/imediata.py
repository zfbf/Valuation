from datetime import date

from ..indice import Indice


class LiquidezImediata(Indice):
    def __init__(self, periodo_contabil):
        super().__init__('Liquidez Imediata')
        self.periodo_contabil = periodo_contabil

    def get_valor(self):
        bp = self.periodo_contabil.bp_ifrs
        disponibilidades = bp.ativo.circulante.get_saldo_disponibilidades()
        passivo_circulante = bp.passivo.circulante
        liquidez_imediata = disponibilidades / passivo_circulante.get_saldo()
        return liquidez_imediata

    def str_comp(self):
        ativo_circulante = self.periodo_contabil.bp_ifrs.ativo.circulante
        repr = '\n\tativo_circulante: {}'.format(ativo_circulante)
        return repr

from datetime import date

from ..indice import Indice


class LiquidezImediata(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Imediata', valuation)

    # Disponibilidades / Passivo Circulante
    def get_valor(self, ano, trimestre):
        bp = super().get_periodo_contabil(ano, trimestre).bp_ifrs
        disponibilidades = bp.ativo.circulante.get_saldo_disponibilidades()
        passivo_circulante = bp.passivo.circulante
        liquidez_imediata = disponibilidades / passivo_circulante.get_saldo()
        return liquidez_imediata

    def str_comp(self, ano, trimestre):
        pass

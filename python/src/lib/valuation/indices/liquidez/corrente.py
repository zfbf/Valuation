from datetime import date

from ..indice import Indice


class LiquidezCorrente(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Corrente', valuation)

    # (Ativo Circulante) / Passivo Circulante
    def get_valor(self, ano, trimestre):
        bp = self.get_periodo_contabil(ano, trimestre).bp_ifrs
        ativo_circulante = bp.ativo.circulante
        passivo_circulante = bp.passivo.circulante
        liquidez_corrente = (ativo_circulante.get_saldo() /
                passivo_circulante.get_saldo())
        return liquidez_corrente

    def str_comp(self, ano, trimestre):
        pass

from datetime import date

from ..indice import Indice


class LiquidezSeca(Indice):
    def __init__(self, periodo_contabil):
        super().__init__('Liquidez Seca')
        self.periodo_contabil = periodo_contabil

    def get_valor(self):
        bp = self.periodo_contabil.bp_ifrs
        ativo_circulante = bp.ativo.circulante
        saldo_estoques = ativo_circulante.get_saldo_estoques()
        passivo_circulante = bp.passivo.circulante
        liquidez_seca = ((ativo_circulante.get_saldo() - saldo_estoques) /
                passivo_circulante.get_saldo())
        return liquidez_seca

    def str_comp(self):
        ativo_circulante = self.periodo_contabil.bp_ifrs.ativo.circulante
        repr = '\n\tativo_circulante: {}'.format(ativo_circulante)
        return repr

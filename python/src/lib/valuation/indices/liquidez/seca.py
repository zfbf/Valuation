from ..indice import Indice


class LiquidezSeca(Indice):
    def __init__(self, valuation, ano, trimestre):
        super().__init__('Liquidez Seca', valuation, ano, trimestre)

    def get_valor(self):
        bp = self.get_periodo_contabil().bp_ifrs
        ativo_circulante = bp.ativo.circulante
        saldo_estoques = ativo_circulante.get_saldo_estoques()
        passivo_circulante = bp.passivo.circulante
        liquidez_seca = ((ativo_circulante.get_saldo() - saldo_estoques) /
                passivo_circulante.get_saldo())
        return liquidez_seca

    def str_comp(self):
        ativo_circulante = self.get_periodo_contabil().bp_ifrs.ativo.circulante
        repr = '\n\tativo_circulante: {}'.format(ativo_circulante)
        return repr

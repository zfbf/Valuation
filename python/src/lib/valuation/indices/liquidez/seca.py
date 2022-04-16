from ..indice import Indice


class LiquidezSeca(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Seca', valuation)

    # (Ativo Circulante - Estoques) / Passivo Circulante
    def get_valor(self, ano, trimestre):
        periodo_contabil = self.get_periodo_contabil(ano, trimestre)
        bp = periodo_contabil.bp_ifrs
        ativo_circulante = bp.ativo.circulante
        saldo_estoques = ativo_circulante.get_saldo_estoques()
        passivo_circulante = bp.passivo.circulante
        liquidez_seca = ((ativo_circulante.get_saldo() - saldo_estoques) /
                passivo_circulante.get_saldo())
        return liquidez_seca

    def str_comp(self, ano, trimestre):
        pass

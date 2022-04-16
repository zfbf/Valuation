from datetime import date

from ..indice import Indice


class LiquidezGeral(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Geral', valuation)

    # (Ativo Circulante + Realizãvel a Longo Prazo) / Passivo
    def get_valor(self, ano, trimestre):
        periodo_contabil = self.get_periodo_contabil(ano, trimestre)
        ativo = periodo_contabil.bp_ifrs.ativo
        saldo_ac = ativo.circulante.get_saldo()
        saldo_rlp = ativo.nao_circulante.get_saldo_realizavel_a_longo_prazo()
        passivo = periodo_contabil.bp_ifrs.passivo
        saldo_pc = passivo.circulante.get_saldo()
        saldo_pnc = passivo.nao_circulante.get_saldo()
        liquidez_geral = ((saldo_ac + saldo_rlp) / (saldo_pc + saldo_pnc))
        return liquidez_geral

    def str_comp(self, ano, trimestre):
        pass

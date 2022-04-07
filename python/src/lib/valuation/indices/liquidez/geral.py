from datetime import date

from ..indice import Indice


class LiquidezGeral(Indice):
    def __init__(self, periodo_contabil):
        super().__init__('Liquidez Geral')
        self.periodo_contabil = periodo_contabil

    def get_valor(self):
        ativo = self.periodo_contabil.bp_ifrs.ativo
        saldo_ac = ativo.circulante.get_saldo()
        saldo_rlp = ativo.nao_circulante.get_saldo_realizavel_a_longo_prazo()
        passivo = self.periodo_contabil.bp_ifrs.passivo
        saldo_pc = passivo.circulante.get_saldo()
        saldo_pnc = passivo.nao_circulante.get_saldo()
        liquidez_geral = ((saldo_ac + saldo_rlp) / (saldo_pc + saldo_pnc))
        return liquidez_geral

    def str_comp(self):
        ativo_circulante = self.periodo_contabil.bp_ifrs.ativo.circulante
        repr = '\n\tativo_circulante: {}'.format(ativo_circulante)
        return repr

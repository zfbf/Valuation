from datetime import date

from ..indice import Indice


class PrazoMedioRecebimento(Indice):
    def __init__(self, periodo_contabil):
        super().__init__('Prazo Médio de Recebimento')
        self.periodo_contabil = periodo_contabil

    def get_valor(self):
        pmr = 365 / self.get_giro()
        return pmr

    def get_giro(self):
        dre = self.periodo_contabil.dre
        receita_operacional_liquida = dre.receita_liquida_operacional
        bp = self.periodo_contabil.bp_ifrs
        contas_a_receber = bp.ativo.circulante.get_conta('contas_a_receber')
        giro = (receita_operacional_liquida.get_saldo()
                    / contas_a_receber.get_saldo())
        return giro

    def str_comp(self):
        ativo_circulante = self.periodo_contabil.bp_ifrs.ativo.circulante
        repr = '\n\tativo_circulante: {}'.format(ativo_circulante)
        return repr

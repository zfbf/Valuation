from .prazo_medio import PrazoMedio


class PrazoMedioRecebimento(PrazoMedio):
    def __init__(self, valuation):
        super().__init__('Prazo Médio de Recebimento', valuation)

    def get_giro(self, ano, trimestre):
        periodo_contabil = self.get_periodo_contabil(ano, trimestre)
        dre = periodo_contabil.dre
        receita_operacional_liquida = dre.receita_liquida_operacional
        bp = periodo_contabil.bp_ifrs
        contas_a_receber = bp.ativo.circulante.get_conta('contas_a_receber')
        giro = (receita_operacional_liquida.get_saldo()
                    / contas_a_receber.get_saldo())
        return giro

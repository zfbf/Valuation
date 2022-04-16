from .prazo_medio import PrazoMedio


class PrazoMedioRecebimento(PrazoMedio):
    def __init__(self, valuation, ano, trimestre):
        super().__init__('Prazo Médio de Recebimento', valuation, ano, trimestre)

    def get_giro(self):
        dre = self.get_periodo_contabil().dre
        receita_operacional_liquida = dre.receita_liquida_operacional
        bp = self.get_periodo_contabil().bp_ifrs
        contas_a_receber = bp.ativo.circulante.get_conta('contas_a_receber')
        giro = (receita_operacional_liquida.get_saldo()
                    / contas_a_receber.get_saldo())
        return giro

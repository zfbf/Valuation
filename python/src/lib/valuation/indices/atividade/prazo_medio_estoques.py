from .prazo_medio import PrazoMedio


class PrazoMedioEstoques(PrazoMedio):
    def __init__(self, valuation):
        super().__init__('Prazo Médio de Estoques', valuation)

    def get_saldo_estoques_medio(self, ano, trimestre):
        periodo_contabil_base = self.get_periodo_contabil(ano, trimestre)
        periodo_contabil_ano_anterior = self.get_periodo_contabil_ano_anterior(
                ano, trimestre)
        estoque_inicial = (periodo_contabil_ano_anterior
                .bp_ifrs.ativo.circulante.get_conta('estoques').get_saldo())
        estoque_final = (periodo_contabil_base.bp_ifrs.ativo
                .circulante.get_conta('estoques').get_saldo())
        estoque_medio = (estoque_inicial + estoque_final) / 2
        return estoque_medio

    def get_giro(self, ano, trimestre):
        estoques_medio = self.get_saldo_estoques_medio(ano, trimestre)
        periodo_contabil_base = self.get_periodo_contabil(ano, trimestre)
        cpv = periodo_contabil_base.dre.custo_produtos_vendidos.get_saldo()
        giro = cpv / estoques_medio
        return giro

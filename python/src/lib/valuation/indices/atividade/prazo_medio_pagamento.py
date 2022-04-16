from datetime import date

from .prazo_medio import PrazoMedio


class PrazoMedioPagamento(PrazoMedio):
    def __init__(self, valuation):
        super().__init__('Prazo Médio de Pagamento', valuation)

    def get_saldo_compras(self, ano, trimestre):
        periodo_contabil_base = self.get_periodo_contabil(ano, trimestre)
        periodo_contabil_ano_anterior = self.get_periodo_contabil_ano_anterior(
                ano, trimestre)
        estoque_inicial = (periodo_contabil_ano_anterior
                .bp_ifrs.ativo.circulante.get_conta('estoques').get_saldo())
        estoque_final = (periodo_contabil_base.bp_ifrs.ativo
                .circulante.get_conta('estoques').get_saldo())
        cpv = periodo_contabil_base.dre.custo_produtos_vendidos.get_saldo()
        compras = estoque_inicial + cpv - estoque_final
        return compras

    def get_saldo_fornecedores(self, ano, trimestre):
        periodo_contabil_base = self.get_periodo_contabil(ano, trimestre)
        fornecedores = (periodo_contabil_base.bp_ifrs.passivo
                .circulante.get_conta('fornecedores'))
        return fornecedores.get_saldo()

    def get_giro(self, ano, trimestre):
        compras = self.get_saldo_compras(ano, trimestre)
        fornecedores = self.get_saldo_fornecedores(ano, trimestre)
        giro = compras / fornecedores
        return giro

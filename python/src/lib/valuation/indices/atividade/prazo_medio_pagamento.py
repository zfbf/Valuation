from datetime import date

from .prazo_medio import PrazoMedio


class PrazoMedioPagamento(PrazoMedio):
    def __init__(self, valuation, ano, trimestre):
        super().__init__('Prazo Médio de Pagamento', valuation, ano, trimestre)

    def get_saldo_compras(self):
        estoque_inicial = (self.get_periodo_contabil_ano_anterior()
                .bp_ifrs.ativo.circulante.get_conta('estoques').get_saldo())
        estoque_final = (self.get_periodo_contabil().bp_ifrs.ativo
                .circulante.get_conta('estoques').get_saldo())
        cpv = self.get_periodo_contabil().dre.custo_produtos_vendidos.get_saldo()
        compras = estoque_inicial + cpv - estoque_final
        return compras

    def get_saldo_fornecedores(self):
        fornecedores = (self.get_periodo_contabil().bp_ifrs.passivo
                .circulante.get_conta('fornecedores'))
        return fornecedores.get_saldo()

    def get_giro(self):
        giro = self.get_saldo_compras() / self.get_saldo_fornecedores()
        return giro

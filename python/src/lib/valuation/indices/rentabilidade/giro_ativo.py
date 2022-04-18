from ..indice import Indice


class GiroAtivo(Indice):
    def __init__(self, valuation):
        super().__init__('Giro Ativo', valuation)

    def get_saldo_ativo_medio(self, ano, trimestre):
        periodo_contabil_base = self.get_periodo_contabil(ano, trimestre)
        periodo_contabil_ano_anterior = self.get_periodo_contabil_ano_anterior(
                ano, trimestre)
        ativo_inicial = periodo_contabil_ano_anterior.bp_ifrs.ativo.get_saldo()
        ativo_final = periodo_contabil_base.bp_ifrs.ativo.get_saldo()
        ativo_medio = (ativo_inicial + ativo_final) / 2
        return ativo_medio

    def get_giro(self, ano, trimestre):
        ativo_medio = self.get_saldo_ativo_medio(ano, trimestre)
        periodo_contabil_base = self.get_periodo_contabil(ano, trimestre)
        receita_operacional = (periodo_contabil_base.dre.
                                    receita_liquida_operacional.get_saldo())
        giro = receita_operacional / ativo_medio
        return giro

    def get_valor(self, ano, trimestre):
        return self.get_giro(ano, trimestre)

    def str_comp(self, ano, trimestre):
        repr = '\n\tgiro: {}'.format(self.get_giro(ano, trimestre))
        return repr

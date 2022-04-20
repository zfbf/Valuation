from datetime import date

from ..indice import Indice


class MargemLiquida(Indice):
    def __init__(self, valuation):
        super().__init__('Margem Liquida', valuation)

    def get_valor(self, ano, trimestre):
        dre = self.get_periodo_contabil(ano, trimestre).dre
        saldo_lucro_liquido = dre.lucro_oper_continuadas.get_saldo()
        saldo_receita_liquida = dre.receita_liquida_operacional.get_saldo()
        margem_liquida = saldo_lucro_liquido / saldo_receita_liquida
        return margem_liquida

    def str_comp(self, ano, trimestre):
        pass

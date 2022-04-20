from datetime import date

from ..indice import Indice


class MargemOperacional(Indice):
    def __init__(self, valuation):
        super().__init__('Margem Operacional', valuation)

    def get_valor(self, ano, trimestre):
        dre = self.get_periodo_contabil(ano, trimestre).dre
        saldo_lucro_operacional = dre.lajir.get_saldo()
        saldo_receita_liquida = dre.receita_liquida_operacional.get_saldo()
        margem_operacional = saldo_lucro_operacional / saldo_receita_liquida
        return margem_operacional

    def str_comp(self, ano, trimestre):
        pass

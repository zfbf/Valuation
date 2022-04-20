from datetime import date

from ..indice import Indice


class MargemBruta(Indice):
    def __init__(self, valuation):
        super().__init__('Margem Bruta', valuation)

    def get_valor(self, ano, trimestre):
        dre = self.get_periodo_contabil(ano, trimestre).dre
        lucro_bruto = dre.lucro_bruto
        receita_liquida = dre.receita_liquida_operacional
        margem_bruta = lucro_bruto.get_saldo() / receita_liquida.get_saldo()
        return margem_bruta

    def str_comp(self, ano, trimestre):
        pass

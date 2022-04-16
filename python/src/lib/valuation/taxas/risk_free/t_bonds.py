from datetime import date

from ..taxa import Taxa


class TBonds(Taxa):
    def __init__(self, serie_historica):
        super().__init__('T-Bonds')
        self.serie_historica = serie_historica

    def get_ano_default(self):
        return date.today().year

    def get_mes_default(self):
        return date.today().month

    def get_dia_default(self):
        return date.today().day

    def get_taxa(self, ano=None, mes=None, dia=None):
        if ano is None:
            ano = self.get_ano_default()

        if mes is None:
            mes = self.get_mes_default()

        if dia is None:
            dia = self.get_dia_default()

        return -1

    def str_comp(self):
        repr = '\n\tsérie histórica: {}'.format(self.serie_historica)
        return repr

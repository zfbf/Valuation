from abc import abstractmethod

from ..indice import Indice


class PrazoMedio(Indice):
    def __init__(self, nome, valuation, ano, trimestre):
        super().__init__(nome, valuation, ano, trimestre)

    def get_valor(self):
        prazo = 365 / self.get_giro()
        return prazo

    @abstractmethod
    def get_giro(self):
        pass

    def str_comp(self):
        ativo_circulante = self.get_periodo_contabil().bp_ifrs.ativo.circulante
        repr = '\n\tgiro: {}'.format(self.get_giro())
        repr += '\nativo_circulante: {}'.format(ativo_circulante)
        return repr

from abc import abstractmethod

from ..indice import Indice


class PrazoMedio(Indice):
    def __init__(self, nome, valuation):
        super().__init__(nome, valuation)

    def get_valor(self, ano, trimestre):
        giro = self.get_giro(ano, trimestre)
        prazo = 365 / giro
        return prazo

    @abstractmethod
    def get_giro(self, ano, trimestre):
        pass

    def str_comp(self, ano, trimestre):
        repr = '\n\tgiro: {}'.format(self.get_giro(ano, trimestre))
        return repr

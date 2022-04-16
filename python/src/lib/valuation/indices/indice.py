from abc import ABC, abstractmethod


class Indice(ABC):
    def __init__(self, nome, valuation):
        super().__init__()
        self.nome = nome
        self.valuation = valuation

    @abstractmethod
    def get_valor(self, ano, trimestre):
        pass

    def get_periodo_contabil(self, ano, trimestre):
        identificador = '{}T{}'.format(ano, trimestre)
        return self.valuation.get_periodo(identificador)

    def get_periodo_contabil_ano_anterior(self, ano, trimestre):
        return self.get_periodo_contabil(ano - 1, trimestre)

    def __str__(self):
        try:
            ano = self.valuation.periodos[-1].ano
            trimestre = self.valuation.periodos[-1].trimestre
            repr = '{} - {} {}T{}'.format(self.nome, self.valuation.empresa,
                    ano, trimestre)
            repr += '\n\tvalor: {}'.format(self.get_valor(ano, trimestre))
            repr += self.str_comp(ano, trimestre)
        except:
            pass
        finally:
            return repr

    @abstractmethod
    def str_comp(self, ano, trimestre):
        pass

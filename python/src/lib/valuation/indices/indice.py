from abc import ABC, abstractmethod


class Indice(ABC):
    def __init__(self, nome, valuation, ano, trimestre):
        super().__init__()
        self.nome = nome
        self.valuation = valuation
        self.ano = ano
        self.trimestre = trimestre

    @abstractmethod
    def get_valor(self):
        pass

    def get_periodo_contabil(self, ano=None, trimestre=None):
        if ano is None:
            ano = self.ano

        if trimestre is None:
            trimestre = self.trimestre

        identificador = '{}T{}'.format(ano, trimestre)
        return self.valuation.get_periodo(identificador)

    def get_periodo_contabil_ano_anterior(self):
        return self.get_periodo_contabil(self.ano - 1, self.trimestre)

    def __str__(self):
        lines = [
            'Nome: {} - {}T{}',
            'Valor: {}'
        ]

        repr = '\n\t'.join(lines).format(
            self.nome,
            self.ano,
            self.trimestre,
            self.get_valor()
        )

        repr += self.str_comp()
        return repr

    @abstractmethod
    def str_comp(self):
        pass

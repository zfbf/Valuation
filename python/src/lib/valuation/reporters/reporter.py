import os
from abc import ABC, abstractmethod
from ..valuation import Valuation

#
# Nice explanation about optional arguments:
# https://realpython.com/python-optional-arguments/
#
class Reporter(ABC):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    @abstractmethod
    def execute(self, **kwargs):
        pass

    def get_output_dir(self):
        output_dir = os.environ['VALUATION_OUTPUT_DIR']
        return output_dir

    def get_ano_tri_frac_index(self, ano_inicial, trimestre_inicial, ano_final,
            trimestre_final):
        ano_array = []
        trimestre_array = []
        ano_frac_array = []
        trimestre = trimestre_inicial

        for ano in range(ano_inicial, ano_final + 1):
            while ((ano < ano_final and trimestre <= 4) or
                   (ano == ano_final and trimestre <= trimestre_final)):
                ano_frac = ano + (trimestre * 3/12)
                ano_array.append(ano)
                ano_frac_array.append(ano_frac)
                trimestre_array.append(trimestre)
                trimestre += 1

            trimestre = 1

        ano_tri_frac_array = [[ano, trimestre, ano_frac] for (ano, trimestre,
                ano_frac) in zip(ano_array, trimestre_array, ano_frac_array)]
        return ano_tri_frac_array

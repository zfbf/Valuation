from abc import ABC, abstractmethod

#
# Cálculo do ROIC:
#   https://www.treasy.com.br/blog/retorno-sobre-o-capital-investido-roic/
#

#TODO: Implementar WACC
#      - criar passos para calcular o WACC
# OBS: WACC não precisa guardar o nome da empresa.
# Pode-se tornar esta classe abstrata e implementar
# WaccTrimestral e WaccAnual

class Taxa(ABC):
    def __init__(self, nome):
        super().__init__()
        self.nome = nome

    @abstractmethod
    def get_taxa(self, ano=None, mes=None, dia=None):
        pass

    @abstractmethod
    def get_ano_default(self):
        pass

    @abstractmethod
    def get_mes_default(self):
        pass

    @abstractmethod
    def get_dia_default(self):
        pass

    def __str__(self):
        lines = [
            'Nome: {}',
            'Taxa: {}'
        ]

        repr = '\n\t'.join(lines).format(
            self.nome,
            self.get_taxa()
        )

        repr += self.str_comp()
        return repr

    @abstractmethod
    def str_comp(self):
        pass

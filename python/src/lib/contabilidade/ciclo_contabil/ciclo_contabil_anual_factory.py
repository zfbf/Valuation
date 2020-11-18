from abc import ABC, abstractmethod

from lib.contabilidade.ciclo_contabil.ciclo_contabil_anual import CicloContabilAnual


class CicloContabilAnualFactory(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_empty_plano_de_contas(self):
        pass

    @abstractmethod
    def feed_plano_de_contas(self, plano_de_contas, ano):
        pass

    def execute(self, ano):
        plano_de_contas = self.get_empty_plano_de_contas()
        self.feed_plano_de_contas(plano_de_contas, ano)
        ciclo_contabil_anual = CicloContabilAnual(ano, plano_de_contas)
        return ciclo_contabil_anual

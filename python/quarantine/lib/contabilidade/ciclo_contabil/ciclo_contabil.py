from abc import ABC, abstractmethod


class CicloContabil(ABC):
    def __init__(self, plano_de_contas):
        super().__init__()
        self.plano_de_contas = plano_de_contas
        self.partidas_dobradas = []

    @abstractmethod
    def get_identificador(self):
        pass

    @abstractmethod
    def get_data_inicio(self):
        pass

    @abstractmethod
    def get_data_fim(self):
        pass

    def add_partida_dobrada(self, partida_dobrada):
        self.partidas_dobradas.add(partida_dobrada)

    def __str__(self):
        repr = "\nExercício Social - {:s}".format(self.get_identificador())
        repr += "\n\tInício: {}".format(self.get_data_inicio().strftime('%d/%m/%Y'))
        repr += "\n\tInício: {}".format(self.get_data_fim().strftime('%d/%m/%Y'))
        repr += "\n\tPlano de Contas: {}".format(self.plano_de_contas)
        return repr

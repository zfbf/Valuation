from abc import ABC, abstractmethod


class Valuation(ABC):
    def __init__(self, empresa):
        super().__init__()
        self.empresa = empresa
        self.periodos = []
        self.init()

    @abstractmethod
    def init(self):
        pass

    def get_empresa(self):
        return self.empresa

    def set_periodos(self, periodos):
        self.periodos = periodos

    def append_periodo(self, periodo):
        self.periodos.append(periodo)

    def get_periodos(self):
        return self.periodos

    def get_periodo(self, identificador):
        target = None

        for periodo in self.periodos:
            if periodo.identificador == identificador:
                target = periodo
                break

        return target

    def __str__(self):
        repr = 'Valuation - {}'.format(self.get_empresa())
        repr += '\n\tTotal de períodos: {}'.format(len(self.get_periodos()))
        ultimo_periodo = self.periodos[-1]
        repr += '\n\tÚltimo período: {}'.format(ultimo_periodo['identificador'])
        repr += '\n\t{}'.format(ultimo_periodo['bp'])
        repr += '\n\t{}'.format(ultimo_periodo['dre'].lucro_liquido)
        return repr

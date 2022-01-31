class PeriodoContabil():
    def __init__(self, identificador):
        super().__init__()
        self.identificador = identificador
        self.bp = None
        self.dre = None
        self.fc = None

    def get_identificador(self):
        return self.identificador

    def __str__(self):
        repr = "\nPeriodoContabil - {:s}".format(self.identificador)
        repr += "\n\tbp: {}".format(self.bp)
        repr += "\n\tdre: {}".format(self.dre)
        repr += "\n\tfc: {}".format(self.fc)
        return repr

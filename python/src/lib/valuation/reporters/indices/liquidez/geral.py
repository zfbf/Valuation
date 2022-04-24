from ..indice_reporter import IndiceReporter


class IndiceLiquidezGeralReporter(IndiceReporter):
    def __init__(self):
        super().__init__()

    #
    # Verificar os argumentos: ano_inicial, trimestre_inicial, ano_final,
    #                          trimestre_final, modo, outros
    # OBS: Caso outros seja um então o modo será de apenas comparação.
    #      Caso outros seja entre 2 e um número mínimo parametrizáve, então
    #           o modo será a média
    #      #      Caso outros seja entre 2 e um número mínimo parametrizáve, então
    #           o modo será a média
    #
    def execute(self, valuation, **kwargs):
        modo = self.guess_modo(kwargs)
        print('modo: {}'.format(modo))
        return 1

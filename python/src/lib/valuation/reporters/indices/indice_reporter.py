from ..reporter import Reporter


class IndiceReporter(Reporter):
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
    #
    def execute(self, valuation, **kwargs):
        modo = self.guess_modo(kwargs)
        print('modo: {}'.format(modo))
        return 1

    def guess_modo(self, kwargs):
        modo = 'SEM_COMPARACAO'

        if 'modo' in kwargs:
            modo = kwargs['modo']
        else:
            if 'outros' in kwargs:
                outros = kwargs['outros']
                tam = len(outros)

                if tam == 1:
                     modo = 'COMPARACAO_SIMPLES'
                elif tam > 1:
                    if tam < 5:
                        modo = 'COMPARACAO_POR_MEDIA'
                    else:
                        modo = 'COMPARACAO_POR_QUARTIS'

        return modo

    def ensure_args_inicio_fim(self, valuation, kwargs):
        if not 'ano_inicial' in kwargs:
            kwargs['ano_inicial'] = valuation.periodos[0].ano + 1

        if not 'trimestre_inicial' in kwargs:
            kwargs['trimestre_inicial'] = valuation.periodos[0].trimestre

        if not 'ano_final' in kwargs:
            kwargs['ano_final'] = valuation.periodos[-1].ano

        if not 'trimestre_final' in kwargs:
            kwargs['trimestre_final'] = valuation.periodos[-1].trimestre

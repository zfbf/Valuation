from ..indice_reporter import IndiceReporter


class IndiceLiquidezGeralReporter(IndiceReporter):
    def __init__(self, valuation):
        super().__init__('Índice de Liquidez Geral', valuation)

    #
    # Verificar os argumentos: ano_inicial, trimestre_inicial, ano_final,
    #                          trimestre_final, modo, outros
    # OBS: Caso outros seja um então o modo será de apenas comparação.
    #      Caso outros seja entre 2 e um número mínimo parametrizáve, então
    #           o modo será a média
    #      #      Caso outros seja entre 2 e um número mínimo parametrizáve, então
    #           o modo será a média
    #
    def execute(self, **kwargs):
        modo = self.guess_modo(kwargs)
        self.ensure_args_inicio_fim(kwargs)
        report = {}

        try:
            report['ano_inicial'] = kwargs['ano_inicial']
            report['trimestre_inicial'] = kwargs['trimestre_inicial']
            report['ano_final'] = kwargs['ano_final']
            report['trimestre_final'] = kwargs['trimestre_final']
            report['modo'] = modo
            #print('report: {}'.format(report))

            indices_liquidez = self.valuation.get_indices_liquidez(
                    report['ano_inicial'],
                    report['trimestre_inicial'],
                    report['ano_final'],
                    report['trimestre_final'])

            empresa_base = {'nome': self.valuation.empresa,
                    'liquidez_geral': indices_liquidez['liquidez_geral']}
            report['empresa_base'] = empresa_base
            report['ano'] = indices_liquidez['ano']
            report['trimestre'] = indices_liquidez['trimestre']
            report['ano_frac'] = indices_liquidez['ano_frac']

            if modo == 'COMPARACAO_SIMPLES':
                self.feed_comparacao_simples(report, kwargs['outros'])

            #print('type(report): {}'.format(type(report)))
            #print('len(report): {}'.format(len(report)))
            #print('report: {}'.format(report))
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.execute() = #except Exception'

            if self.valuation is None:
                msg += '\n\tvaluation is none'
            else:
                msg += '\n\ttype(valuation): {}'.format(type(self.valuation))
                msg += '\n\tempresa: {}'.format(type(self.valuation.empresa))
                msg += '\n\tmodo: {}'.format(modo)

            raise Exception(msg) from e

        return report

    def feed_comparacao_simples(self, report, outros):
        #print('feed_comparacao_simples')
        #print('report: {}'.format(report))
        #print('type(outros): {}'.format(type(outros)))
        #print('outros: {}'.format(outros))
        outras_empresas = []

        try:
            for outro_valuation in outros:
                indices_liquidez = outro_valuation.get_indices_liquidez(
                        report['ano_inicial'],
                        report['trimestre_inicial'],
                        report['ano_final'],
                        report['trimestre_final'])
                empresa = {'nome': outro_valuation.empresa,
                           'liquidez_geral': indices_liquidez['liquidez_geral']}
                outras_empresas.append(empresa)

            report['outras_empresas'] = outras_empresas
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.execute() = #except Exception'
            msg += '\n\treport: {}'.format(report)

            if outros is not None:
                msg += '\n\ttype(outros): {}'.format(type(outros))
                msg += '\n\tlen(outros): {}'.format(len(outros))
                msg += '\n\ttype(outros[0]): {}'.format(type(outros[0]))

            raise Exception(msg) from e

        return report

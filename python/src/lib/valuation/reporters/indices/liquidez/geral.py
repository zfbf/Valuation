import os
import numpy as np
from ..indice_reporter import IndiceReporter


class IndiceLiquidezGeralReporter(IndiceReporter):
    def __init__(self, valuation):
        super().__init__('Índice de Liquidez Geral', valuation)

    #
    # Verificar os argumentos: ano_inicial, trimestre_inicial, ano_final,
    #                          trimestre_final, modo, outros, export
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
        outros = None

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

            if 'outros' in kwargs:
                outros = kwargs['outros']
                self.feed_comparacao_simples(report, outros )
                self.feed_estatisticas(report)

            save_to_latex = kwargs.get('save_to_latex', False)

            if save_to_latex:
                self.save_to_latex(report)

            #print('type(report): {}'.format(type(report)))
            #print('len(report): {}'.format(len(report)))
            #print('report: {}'.format(report))
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.execute() = #except Exception'

            if self.valuation is None:
                msg += '\n\tvaluation is none'
            else:
                msg += '\n\ttype(valuation): {}'.format(type(self.valuation))
                msg += '\n\tempresa: {}'.format(self.valuation.empresa)
                msg += '\n\tmodo: {}'.format(modo)

                if (outros is not None):
                    msg += '\n\tlen(outros): {}'.format(len(outros))
                else:
                    msg += '\n\toutros is None'

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

    def feed_estatisticas(self, report):
        #print('feed_estatisticas')
        try:
            indices_liq_geral = report['empresa_base']['liquidez_geral']
            report['empresa_base']['estatisticas'] = {
                'min': np.min(indices_liq_geral),
                'max': np.max(indices_liq_geral),
                'media': np.mean(indices_liq_geral),
                'quartil_1': np.percentile(indices_liq_geral, 25),
                'quartil_2': np.percentile(indices_liq_geral, 50),
                'quartil_3': np.percentile(indices_liq_geral, 75)
            }

            indices_outras_empresas_seq_list_list = [indice['liquidez_geral']
                    for indice in report['outras_empresas']]
            indices_outras_empresas_paralel_list_tuple = list(zip(
                    *indices_outras_empresas_seq_list_list))
            aux = indices_outras_empresas_paralel_list_tuple

            report['estatisticas'] = {
                'min': [np.min(a) for a in aux],
                'max': [np.max(a) for a in aux],
                'media': [np.mean(a) for a in aux],
                'quartil_1': [np.percentile(a, 25) for a in aux],
                'quartil_2': [np.percentile(a, 50) for a in aux],
                'quartil_3': [np.percentile(a, 75) for a in aux]
            }

            #print('type(indices_outras_empresas): {}'.format(type(
            #        indices_outras_empresas)))
            #print('len(indices_outras_empresas): {}'.format(len(
            #        indices_outras_empresas)))

            for outra_empresa in report['outras_empresas']:
                indices_liq_geral = outra_empresa['liquidez_geral']
                outra_empresa['estatisticas'] = {
                    'min': np.min(indices_liq_geral),
                    'max': np.max(indices_liq_geral),
                    'media': np.mean(indices_liq_geral),
                    'quartil_1': np.percentile(indices_liq_geral, 25),
                    'quartil_2': np.percentile(indices_liq_geral, 50),
                    'quartil_3': np.percentile(indices_liq_geral, 75)
                }
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.feed_estatisticas()'
            msg += ' = #except Exception'
            msg += '\n\treport: {}'.format(report)

            if outros is not None:
                msg += '\n\ttype(outros): {}'.format(type(outros))
                msg += '\n\tlen(outros): {}'.format(len(outros))
                msg += '\n\ttype(outros[0]): {}'.format(type(outros[0]))

            raise Exception(msg) from e

        return report

    def save_to_latex(self, report):
        print('save_to_latex')

        try:
            output_dir = self.get_output_dir()
            print('output_dir: {}'.format(output_dir))
            directories = [self.valuation.empresa, 'tex', 'indices', 'liquidez',
                           'geral']
            aux_dir = os.path.join(output_dir, *directories)
            print('aux_dir: {}'.format(aux_dir))
            #os.makedirs(aux_dir)

            ano_frac = report['ano_frac']
            liq_geral = report['empresa_base']['liquidez_geral']
            nome = report['empresa_base']['nome']
            desc = '{} - min: {}, max: {}'.format(nome,
                    report['empresa_base']['estatisticas']['min'],
                    report['empresa_base']['estatisticas']['max'])
            file_name = os.path.join(aux_dir, '{}.dat'.format(nome))
            self.save_to_latex_aux(file_name, ano_frac, liq_geral, desc)

            for empresa in report['outras_empresas']:
                liq_geral = empresa['liquidez_geral']
                nome = empresa['nome']
                desc = '{} - min: {}, max: {}'.format(nome,
                        empresa['estatisticas']['min'],
                        empresa['estatisticas']['max'])
                file_name = os.path.join(aux_dir, '{}.dat'.format(nome))
                self.save_to_latex_aux(file_name, ano_frac, liq_geral, desc)

            estatistica_dict = report['estatisticas']

            for estatistica_key in estatistica_dict.keys():
                estatistica = estatistica_dict[estatistica_key]
                file_name = os.path.join(aux_dir, '{}.dat'.format(estatistica_key))
                self.save_to_latex_aux(file_name, ano_frac, estatistica)
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.save_to_latex()'
            msg += ' = #except Exception'
            msg += '\n\treport: {}'.format(report)
            raise Exception(msg) from e

        return report

    def save_to_latex_aux(self, file_name, ano_frac, liq_geral, desc=None):
        lines = ['x_0 f(x)']
        lines.append('#{}'.format(desc))

        for x, y in zip(ano_frac, liq_geral):
            lines.append('{} {}'.format(x, y))

        f = open(file_name, 'w')
        f.write('\n'.join(lines))
        f.close()

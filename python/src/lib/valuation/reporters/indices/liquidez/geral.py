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
        print('IndiceLiquidezGeralReporter.execute')
        d = kwargs
        print('\n\n'.join('{}:\n\t{}'.format(k, v) for k, v in d.items()))

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
                self.feed_comparacao_simples(report, outros)
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
        print('feed_comparacao_simples')
        print('report:')
        d = report
        print('\n\n'.join('{}:\n\t{}'.format(k, v) for k, v in d.items()))
        print('type(outros): {}'.format(type(outros)))
        print('len(outros): {}'.format(len(outros)))
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
            msg += '\n\treport ano inicial: {}'.format(report['ano_inicial'])

            if outros is not None:
                msg += '\n\ttype(outros): {}'.format(type(outros))
                msg += '\n\tlen(outros): {}'.format(len(outros))
                msg += '\n\ttype(outros[0]): {}'.format(type(outros[0]))

            raise Exception(msg) from e

        print('No final de feed_comparacao_simples')
        print('report:')
        d = report
        print('\n\n'.join('{}:\n\t{}'.format(k, v) for k, v in d.items()))

        return report

    def feed_estatisticas(self, report):
        print('feed_estatisticas')
        outras_empresas = None

        try:
            emp_base_liq_geral = report['empresa_base']['liquidez_geral']
            emp_base_liq_geral = [i for i in emp_base_liq_geral if i]

            report['empresa_base']['estatisticas'] = {
                'min': np.min(emp_base_liq_geral),
                'max': np.max(emp_base_liq_geral),
                'media': np.mean(emp_base_liq_geral),
                'quartil_1': np.percentile(emp_base_liq_geral, 25),
                'quartil_2': np.percentile(emp_base_liq_geral, 50),
                'quartil_3': np.percentile(emp_base_liq_geral, 75)
            }

            outras_empresas = report.get('outras_empresas', None)

            if outras_empresas is not None:
                indices_outras_empresas_seq_list_list = [indice['liquidez_geral']
                        for indice in outras_empresas]
                indices_outras_empresas_paralel_list_tuple = list(zip(
                        *indices_outras_empresas_seq_list_list))
                corte_transversal_array = \
                        indices_outras_empresas_paralel_list_tuple

                min_array = []
                max_array = []
                media_array = []
                quartil_1_array = []
                quartil_2_array = []
                quartil_3_array = []

                for corte_transversal in corte_transversal_array:
                    (min, max, media) = (None, None, None)
                    (q1, q2, q3) = (None, None, None)
                    aux = [i for i in corte_transversal if i]

                    if len(aux) > 0:
                        min = np.min(aux)
                        max = np.max(aux)
                        media = np.mean(aux)
                        quartil_1 = np.percentile(aux, 25)
                        quartil_2 = np.percentile(aux, 50)
                        quartil_3 = np.percentile(aux, 75)

                    min_array.append(min)
                    max_array.append(max)
                    media_array.append(media)
                    quartil_1_array.append(q1)
                    quartil_2_array.append(q2)
                    quartil_3_array.append(q3)

                report['estatisticas'] = {
                    'min': min_array,
                    'max': max_array,
                    'media': media_array,
                    'quartil_1': quartil_1_array,
                    'quartil_2': quartil_2_array,
                    'quartil_3': quartil_3_array
                }

                #print('type(indices_outras_empresas): {}'.format(type(
                #        indices_outras_empresas)))
                #print('len(indices_outras_empresas): {}'.format(len(
                #        indices_outras_empresas)))

                for outra_empresa in outras_empresas:
                    outra_emp_liq_geral = outra_empresa['liquidez_geral']
                    outra_emp_liq_geral = [i for i in outra_emp_liq_geral if i]
                    outra_empresa['estatisticas'] = {
                        'min': np.min(outra_emp_liq_geral),
                        'max': np.max(outra_emp_liq_geral),
                        'media': np.mean(outra_emp_liq_geral),
                        'quartil_1': np.percentile(outra_emp_liq_geral, 25),
                        'quartil_2': np.percentile(outra_emp_liq_geral, 50),
                        'quartil_3': np.percentile(outra_emp_liq_geral, 75)
                    }
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.feed_estatisticas()'
            msg += ' = #except Exception'
            msg += '\n\treport ano inicial: {}'.format(report['ano_inicial'])

            if outras_empresas is not None:
                msg += '\n\ttype(outras_empresas): {}'.format(type(outras_empresas))
                msg += '\n\tlen(outras_empresas): {}'.format(len(outras_empresas))
                msg += '\n\ttype(outras_empresas[0]): {}'.format(type(outras_empresas[0]))
            else:
                msg += '\n\toutras_empresas is None'

            raise Exception(msg) from e

        return report

    def save_to_latex(self, report):
        print('save_to_latex')
        outras_empresas = None

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

            outras_empresas = report.get('outras_empresas', [])
            #print('outras_empresas: {}'.format(outras_empresas))
            #d = report
            #print('\n\n'.join('{}:\n\t{}'.format(k, v) for k, v in d.items()))

            for empresa in outras_empresas:
                liq_geral = empresa['liquidez_geral']
                nome = empresa['nome']
                desc = '{} - min: {}, max: {}'.format(nome,
                        empresa['estatisticas']['min'],
                        empresa['estatisticas']['max'])
                file_name = os.path.join(aux_dir, '{}.dat'.format(nome))
                self.save_to_latex_aux(file_name, ano_frac, liq_geral, desc)

            estatistica_dict = report.get('estatisticas', {})

            for estatistica_key in estatistica_dict.keys():
                estatistica = estatistica_dict[estatistica_key]
                file_name = os.path.join(aux_dir, '{}.dat'.format(estatistica_key))
                self.save_to_latex_aux(file_name, ano_frac, estatistica)
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.save_to_latex()'
            msg += ' = #except Exception'
            msg += '\n\treport ano inicial: {}'.format(report['ano_inicial'])
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

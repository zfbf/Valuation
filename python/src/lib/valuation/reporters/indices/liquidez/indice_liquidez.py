from abc import ABC, abstractmethod
import os
import numpy as np
from ..indice_reporter import IndiceReporter


class IndiceLiquidezReporter(IndiceReporter, ABC):
    def __init__(self, name, indice_key, valuation):
        super().__init__(name, indice_key, valuation)

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
        print('IndiceLiquidezReporter.execute')
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

            self.inject_empresa_base_data(report)

            if 'outros' in kwargs:
                outros = kwargs['outros']
                self.inject_outras_empresas_data(report, outros)
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

    def inject_empresa_base_data(self, report):
        indices_liquidez = self.get_indices(self.valuation, report)
        indice_key = self.indice_key
        empresa_base = {'nome': self.valuation.empresa,
                indice_key: indices_liquidez[indice_key]}
        report['empresa_base'] = empresa_base
        report['ano'] = indices_liquidez['ano']
        report['trimestre'] = indices_liquidez['trimestre']
        report['ano_frac'] = indices_liquidez['ano_frac']

    @abstractmethod
    def get_indices(self, valuation, report):
        pass

    def inject_outras_empresas_data(self, report, outros_valuations):
        print('IndiceLiquidezReporter.inject_outras_empresas_data')
        print('report:')
        d = report
        print('\n\n'.join('{}:\n\t{}'.format(k, v) for k, v in d.items()))
        print('type(outros_valuations): {}'.format(type(outros_valuations)))
        print('len(outros_valuations): {}'.format(len(outros_valuations)))
        outras_empresas = []

        try:
            indice_key = self.indice_key
            for outro_valuation in outros_valuations:
                indices_liquidez = self.get_indices(outro_valuation, report)
                empresa = {'nome': outro_valuation.empresa,
                           indice_key: indices_liquidez[indice_key]}
                outras_empresas.append(empresa)

            report['outras_empresas'] = outras_empresas
        except Exception as e:
            msg = 'IndiceLiquidezlReporter.execute() = #except Exception'
            msg += '\n\treport ano inicial: {}'.format(report['ano_inicial'])

            if outros_valuations is not None:
                msg += '\n\ttype(outros_valuations): {}'.format(
                        type(outros_valuations))
                msg += '\n\tlen(outros_valuations): {}'.format(
                        len(outros_valuations))
                msg += '\n\ttype(outros_valuations[0]): {}'.format(
                        type(outros_valuations[0]))

            raise Exception(msg) from e

        print('No final de inject_outras_empresas_data')
        print('report:')
        d = report
        print('\n\n'.join('{}:\n\t{}'.format(k, v) for k, v in d.items()))

        return report

    def feed_estatisticas(self, report):
        print('feed_estatisticas')
        outras_empresas = None

        try:
            indice_key = self.indice_key
            ind_liq_emp_base = report['empresa_base'][indice_key]
            ind_liq_emp_base = [i for i in ind_liq_emp_base if i]

            report['empresa_base']['estatisticas'] = {
                'min': np.min(ind_liq_emp_base),
                'max': np.max(ind_liq_emp_base),
                'media': np.mean(ind_liq_emp_base),
                'quartil_1': np.percentile(ind_liq_emp_base, 25),
                'quartil_2': np.percentile(ind_liq_emp_base, 50),
                'quartil_3': np.percentile(ind_liq_emp_base, 75)
            }

            outras_empresas = report.get('outras_empresas', None)

            if outras_empresas is not None:
                indices_outras_empresas_seq_list_list = [indice[indice_key]
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
                        q1 = np.percentile(aux, 25)
                        q2 = np.percentile(aux, 50)
                        q3 = np.percentile(aux, 75)

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
                    (min, max, media) = (None, None, None)
                    (q1, q2, q3) = (None, None, None)

                    ind_liq_outra_emp = outra_empresa[indice_key]
                    ind_liq_outra_emp = [i for i in ind_liq_outra_emp if i]

                    if len(ind_liq_outra_emp) > 0:
                        min = np.min(ind_liq_outra_emp)
                        max = np.max(ind_liq_outra_emp),
                        media = np.mean(ind_liq_outra_emp)
                        quartil_1 = np.percentile(ind_liq_outra_emp, 25),
                        quartil_2 = np.percentile(ind_liq_outra_emp, 50),
                        quartil_3 = np.percentile(ind_liq_outra_emp, 75)

                    outra_empresa['estatisticas'] = {
                        'min': min,
                        'max': max,
                        'media': media,
                        'quartil_1': q1,
                        'quartil_2': q2,
                        'quartil_3': q3
                    }
        except Exception as e:
            msg = 'IndiceLiquidezReporter.feed_estatisticas()'
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
            directories = ([self.valuation.empresa, 'tex'] +
                    self.get_tex_subdirectories())
            aux_dir = os.path.join(output_dir, *directories)
            print('aux_dir: {}'.format(aux_dir))
            #os.makedirs(aux_dir)

            if not os.path.exists(aux_dir):
                os.makedirs(aux_dir)

            ano_frac = report['ano_frac']
            indice_key = self.indice_key
            liq_geral = report['empresa_base'][indice_key]
            nome = report['empresa_base']['nome']
            desc = '{}.{} - min: {}, max: {}'.format(
                    indice_key,
                    nome,
                    report['empresa_base']['estatisticas']['min'],
                    report['empresa_base']['estatisticas']['max'])
            file_name = os.path.join(aux_dir, '{}.dat'.format(nome))
            self.save_to_latex_aux(file_name, ano_frac, liq_geral, desc)

            outras_empresas = report.get('outras_empresas', [])
            #print('outras_empresas: {}'.format(outras_empresas))
            #d = report
            #print('\n\n'.join('{}:\n\t{}'.format(k, v) for k, v in d.items()))

            for empresa in outras_empresas:
                liq_geral = empresa[indice_key]
                nome = empresa['nome']
                desc = '{}.{} - min: {}, max: {}'.format(
                        indice_key,
                        nome,
                        empresa['estatisticas']['min'],
                        empresa['estatisticas']['max'])
                file_name = os.path.join(aux_dir, '{}.dat'.format(nome))
                self.save_to_latex_aux(file_name, ano_frac, liq_geral, desc)

            estatistica_dict = report.get('estatisticas', {})

            for estatistica_key in estatistica_dict.keys():
                estatistica = estatistica_dict[estatistica_key]
                desc = '{}.{} - min: {}, max: {}'.format(
                        indice_key,
                        estatistica_key,
                        np.min([i for i in estatistica if i]),
                        np.max([i for i in estatistica if i]))
                file_name = os.path.join(aux_dir, '{}.dat'.format(estatistica_key))
                self.save_to_latex_aux(file_name, ano_frac, estatistica, desc)
        except Exception as e:
            msg = 'IndiceLiquidezGeralReporter.save_to_latex()'
            msg += ' = #except Exception'
            msg += '\n\treport ano inicial: {}'.format(report['ano_inicial'])
            raise Exception(msg) from e

        return report

    @abstractmethod
    def get_tex_subdirectories(self):
        pass

    def save_to_latex_aux(self, file_name, ano_frac, indice_liquidez, desc=None):
        lines = ['x_0 f(x)']
        lines.append('#{}'.format(desc))

        for x, y in zip(ano_frac, indice_liquidez):
            if y:
                lines.append('{} {}'.format(x, y))

        f = open(file_name, 'w')
        f.write('\n'.join(lines))
        f.close()

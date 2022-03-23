from datetime import datetime
import unittest

from .iochpe_dados_trimestrais_anualizados import Iochpe2009T12021T4


class TestIochpeDadosTrimestraisAnualizados(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.iochpe_dta = Iochpe2009T12021T4()
        self.iochpe_dta.prepare()

    def test_get_identificador(self):
        identificador = self.iochpe_dta.get_identificador()
        self.assertIsNotNone(identificador)
        self.assertEqual(identificador, 'Iochpe_2009T1_2021T4')

    def test_import_from_excel(self):
        df = self.iochpe_dta.import_from_excel()
        self.assertIsNotNone(df)
        print('df.shape: {}'.format(df.shape))
        print('filtered df: \n{}'.format(
                df.filter(axis='columns',
                          items=['codigo_0', 'codigo_1', 'codigo_2',
                                 'codigo_3', 'conta',    '2010T1',
                                 '2010T2',   '2021T1',   '2021T2'])))

    def test_prepare(self):
        self.iochpe_dta.prepare()
        print('iochpe_dta.df.shape: \n{}'.format(self.iochpe_dta.df.shape))
        df2 = self.iochpe_dta.df
        print('filtered df2: \n{}'.format(df2.filter(
                axis='columns',
                items=['codigo_0', 'codigo_1', 'codigo_2',
                       'codigo_3', 'conta',    '2010T1',
                       '2010T2',   '2021T1',   '2021T2'])))
        print('df2.index.names: \n{}'.format(df2.index.names))
        print('df2.index.values: \n{}'.format(df2.index.values))
        print('df2.index: \n{}'.format(df2.index))
        print('df2.shape: \n{}'.format(df2.shape))

    def test_query(self):
        print('\ntest_query')
        filter = ('bp', 'ativo', 'circulante')
        result  = self.iochpe_dta.query(filter)
        print('result: \n{}'.format(result))
        print('filtered result to {}: \n{}'.format(filter, result.filter(
                axis='columns',
                items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo(self):
        print('\ntest_query_ativo')
        filter = ('bp', 'ativo')
        result  = self.iochpe_dta.query(filter)

        if TestIochpeDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(filter, result.filter(
                    axis='columns',
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo_nao_circulante(self):
        print('\ntest_query_ativo_nao_circulante')
        index = ('bp', 'ativo', 'nao_circulante')
        result = self.iochpe_dta.query(index)

        if TestIochpeDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(index, result.filter(
                    axis='columns',
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

            index = ('bp', 'ativo', 'nao_circulante', 'intangiveis_liquido')
            identificador_periodo = '2020T4'
            saldo = self.iochpe_dta.get_valor(index, identificador_periodo)

            print('index: {}\n\tidentificador_periodo: {}\n\tsaldo: {}'.format(
                    index,
                    identificador_periodo,
                    saldo))

            df = self.iochpe_dta.df
            print('type(df) : {}'.format(type(df)))
            result = df.loc[index, identificador_periodo]
            s = '\n\t'.join(['index: {}',
                             'identificador_periodo: {}',
                             'type(result): {}',
                             'result:\n{}',
                             'result[0]:\n{}',
                             'result[-1]:\n{}'])
            print(s.format(index,
                           identificador_periodo,
                           type(result),
                           result,
                           result[0],
                           result[-1]))

    def test_get_valor(self):
        print('\ntest_get_valor')
        index = ('bp', 'ativo', 'circulante', 'caixa_e_equivalentes')
        periodo = '2010T4'
        result = self.iochpe_dta.get_valor(index, periodo)
        print('result: \n{}'.format(result))
        self.assertEqual(57639000, result)

    def test_get_project_path(self):
        project_path = self.iochpe_dta.get_project_path()
        print('project_path: {}'.format(project_path))
        self.assertIsNotNone(project_path)

    def test_get_dados_empresa_file_path(self):
        iochpe_dados_path = self.iochpe_dta.get_dados_empresa_file_path()
        print('iochpe_dados_path: {}'.format(iochpe_dados_path))
        self.assertIsNotNone(iochpe_dados_path)

    def test_get_dados_empresa_file_name(self):
        iochpe_dados_file_name = self.iochpe_dta.get_dados_empresa_file_name()
        print('iochpe_dados_file_name: {}'.format(iochpe_dados_file_name))
        self.assertIsNotNone(iochpe_dados_file_name)
        self.assertEqual(iochpe_dados_file_name,
                'economatica_Iochpe_trimestral_anualizado_2009-2021.xls')

    def test_get_codigos_periodos(self):
        codigos_periodos = self.iochpe_dta.get_codigos_periodos()
        self.assertIsNotNone(codigos_periodos)
        self.assertEqual(52, len(codigos_periodos))

    @unittest.skipUnless(print_to_stdout, 'making_clean_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print(self.iochpe_dta)

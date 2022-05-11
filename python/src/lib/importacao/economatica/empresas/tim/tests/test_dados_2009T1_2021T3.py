from datetime import datetime
import unittest

from ..dados_2009T1_2021T3 import Tim2009T12021T3


class TestTimDadosTrimestraisAnualizados(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.tim_dta = Tim2009T12021T3()
        self.tim_dta.prepare()

    def test_get_identificador(self):
        identificador = self.tim_dta.get_identificador()
        self.assertIsNotNone(identificador)
        self.assertEqual(identificador, 'Tim_2009T1_2021T3')

    def test_import_from_excel(self):
        df = self.tim_dta.import_from_excel()
        self.assertIsNotNone(df)
        print('df.shape: {}'.format(df.shape))
        print('filtered df: \n{}'.format(
                df.filter(axis='columns',
                          items=['codigo_0', 'codigo_1', 'codigo_2',
                                 'codigo_3', 'conta',    '2010T1',
                                 '2010T2',   '2021T1',   '2021T2'])))

    def test_prepare(self):
        self.tim_dta.prepare()
        print('tim_dta.df.shape: \n{}'.format(self.tim_dta.df.shape))
        df2 = self.tim_dta.df
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
        filter = 'bp.ativo.circulante'
        result  = self.tim_dta.query(filter)
        print('result: \n{}'.format(result))
        print('filtered result to {}: \n{}'.format(filter, result.filter(
                items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo(self):
        print('\ntest_query_ativo')
        filter = 'bp.ativo'
        result  = self.tim_dta.query(filter)

        if TestTimDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(filter, result.filter(
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo_nao_circulante(self):
        print('\ntest_query_ativo_nao_circulante')
        index = 'bp.ativo.nao_circulante'
        result = self.tim_dta.query(index)

        if TestTimDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(index, result.filter(
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

            index = 'bp.ativo.nao_circulante.intangiveis_liquido'
            identificador_periodo = '2020T4'
            saldo = self.tim_dta.get_valor(index, identificador_periodo)

            print('index: {}\n\tidentificador_periodo: {}\n\tsaldo: {}'.format(
                    index,
                    identificador_periodo,
                    saldo))

            df = self.tim_dta.df
            print('type(df) : {}'.format(type(df)))
            result = df.loc[index, identificador_periodo]
            s = '\n\t'.join(['index: {}',
                             'identificador_periodo: {}',
                             'type(result): {}',
                             'result:\n{}'])
            print(s.format(index,
                           identificador_periodo,
                           type(result),
                           result))

    def test_get_valor(self):
        print('\ntest_get_valor')
        index = 'bp.ativo.circulante.caixa_e_equivalentes'
        periodo = '2020T4'
        result = self.tim_dta.get_valor(index, periodo)
        print('result: \n{}'.format(result))
        self.assertEqual(2575291000, result)

    def test_get_project_path(self):
        project_path = self.tim_dta.get_project_path()
        print('project_path: {}'.format(project_path))
        self.assertIsNotNone(project_path)

    def test_get_dados_empresa_file_path(self):
        print('Dentro de test_get_dados_empresa_file_path')
        tim_dados_path = self.tim_dta.get_dados_empresa_file_path()
        print('tim_dados_path: {}'.format(tim_dados_path))
        self.assertIsNotNone(tim_dados_path)

    def test_get_dados_empresa_file_name(self):
        tim_dados_file_name = self.tim_dta.get_dados_empresa_file_name()
        print('tim_dados_file_name: {}'.format(tim_dados_file_name))
        self.assertIsNotNone(tim_dados_file_name)
        self.assertEqual(tim_dados_file_name,
                'economatica_Tim_2009T1-2021T3.xls')

    def test_get_codigos_periodos(self):
        codigos_periodos = self.tim_dta.get_codigos_periodos()
        self.assertIsNotNone(codigos_periodos)
        self.assertEqual(51, len(codigos_periodos))

    @unittest.skipUnless(print_to_stdout, 'making_clean_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print(self.tim_dta)

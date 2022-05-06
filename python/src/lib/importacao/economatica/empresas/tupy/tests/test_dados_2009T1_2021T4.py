from datetime import datetime
import unittest

from ..dados_2009T1_2021T4 import Tupy2009T12021T4


class TestTupyDadosTrimestraisAnualizados(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.tupy_dta = Tupy2009T12021T4()
        self.tupy_dta.prepare()

    def test_get_identificador(self):
        identificador = self.tupy_dta.get_identificador()
        self.assertIsNotNone(identificador)
        self.assertEqual(identificador, 'Tupy_2009T1_2021T4')

    def test_import_from_excel(self):
        df = self.tupy_dta.import_from_excel()
        self.assertIsNotNone(df)
        print('df.shape: {}'.format(df.shape))
        print('filtered df: \n{}'.format(
                df.filter(axis='columns',
                          items=['codigo_0', 'codigo_1', 'codigo_2',
                                 'codigo_3', 'conta',    '2010T1',
                                 '2010T2',   '2021T1',   '2021T2'])))

    def test_prepare(self):
        self.tupy_dta.prepare()
        print('tupy_dta.df.shape: \n{}'.format(self.tupy_dta.df.shape))
        df2 = self.tupy_dta.df
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
        result  = self.tupy_dta.query(filter)
        print('result: \n{}'.format(result))
        print('filtered result to {}: \n{}'.format(filter, result.filter(
                items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo(self):
        print('\ntest_query_ativo')
        filter = 'bp.ativo'
        result  = self.tupy_dta.query(filter)

        if TestTupyDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(filter, result.filter(
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo_nao_circulante(self):
        print('\ntest_query_ativo_nao_circulante')
        index = 'bp.ativo.nao_circulante'
        result = self.tupy_dta.query(index)

        if TestTupyDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(index, result.filter(
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

            index = 'bp.ativo.nao_circulante.intangiveis_liquido'
            identificador_periodo = '2020T4'
            saldo = self.tupy_dta.get_valor(index, identificador_periodo)

            print('index: {}\n\tidentificador_periodo: {}\n\tsaldo: {}'.format(
                    index,
                    identificador_periodo,
                    saldo))

            df = self.tupy_dta.df
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
        index = ('bp', 'ativo', 'circulante', 'caixa_e_equivalentes')
        periodo = '2010T4'
        result = self.tupy_dta.get_valor(index, periodo)
        print('result: \n{}'.format(result))
        self.assertTrue(result != 0, result)

    def test_get_project_path(self):
        project_path = self.tupy_dta.get_project_path()
        print('project_path: {}'.format(project_path))
        self.assertIsNotNone(project_path)

    def test_get_dados_empresa_file_path(self):
        tupy_dados_path = self.tupy_dta.get_dados_empresa_file_path()
        print('tupy_dados_path: {}'.format(tupy_dados_path))
        self.assertIsNotNone(tupy_dados_path)

    def test_get_dados_empresa_file_name(self):
        tupy_dados_file_name = self.tupy_dta.get_dados_empresa_file_name()
        print('tupy_dados_file_name: {}'.format(tupy_dados_file_name))
        self.assertIsNotNone(tupy_dados_file_name)
        self.assertEqual(tupy_dados_file_name,
                'economatica_Tupy_2009T1-2021T4.xls')

    def test_get_codigos_periodos(self):
        codigos_periodos = self.tupy_dta.get_codigos_periodos()
        self.assertIsNotNone(codigos_periodos)
        self.assertEqual(52, len(codigos_periodos))

    @unittest.skipUnless(print_to_stdout, 'making_clean_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print(self.tupy_dta)

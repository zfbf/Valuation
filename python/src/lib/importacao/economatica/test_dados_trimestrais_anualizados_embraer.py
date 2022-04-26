from datetime import datetime
import unittest

from .empresas.embraer.dados_2009T1_2021T4 import Embraer2009T12021T4


class TestEmbraerDadosTrimestraisAnualizados(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.embraer_dta = Embraer2009T12021T4()
        self.embraer_dta.prepare()

    def test_get_identificador(self):
        identificador = self.embraer_dta.get_identificador()
        self.assertIsNotNone(identificador)
        self.assertEqual(identificador, 'Embraer_2009T1_2021T4')

    def test_import_from_excel(self):
        print('\nDentro de test_import_from_excel()')
        df = self.embraer_dta.import_from_excel()
        self.assertIsNotNone(df)
        print('df.shape: {}'.format(df.shape))
        print('df.index: {}'.format(df.index))
        print('filtered df: \n{}'.format(
                df.filter(axis='columns',
                          items=['id',        'conta',     '2010T1',
                                 '2010T2',    '2021T3',    '2021T4'])))

    def test_prepare(self):
        print('\nDentro de test_prepare()')
        self.embraer_dta.prepare()
        print('embraer_dta.df.shape: \n{}'.format(self.embraer_dta.df.shape))
        df2 = self.embraer_dta.df
        print('filtered df2: \n{}'.format(df2.filter(
                axis='columns',
                items=['codigo_0', 'codigo_1', 'codigo_2',
                       'codigo_3', 'conta',    '2010T1',
                       '2010T2',   '2021T3',   '2021T4'])))
        print('df2.index.names: \n{}'.format(df2.index.names))
        print('df2.index.values: \n{}'.format(df2.index.values))
        print('df2.index: \n{}'.format(df2.index))
        print('df2.shape: \n{}'.format(df2.shape))

    def test_query(self):
        print('\ntest_query')
        id = 'bp.ativo.circulante'
        result = self.embraer_dta.query(id)
        print('result: \n{}'.format(result))
        print('filtered result to {}: \n{}'.format(id, result.filter(
                items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo(self):
        print('\ntest_query_ativo')
        id = 'bp.ativo'
        result  = self.embraer_dta.query(id)

        if TestEmbraerDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(id, result.filter(
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

    def test_query_ativo_nao_circulante(self):
        print('\ntest_query_ativo_nao_circulante')
        id = 'bp.ativo.nao_circulante'
        result = self.embraer_dta.query(id)

        if TestEmbraerDadosTrimestraisAnualizados.print_to_stdout:
            print('result: \n{}'.format(result))
            print('filtered result to {}: \n{}'.format(id, result.filter(
                    items=['conta', '2010T1', '2010T2', '2021T1', '2021T2'])))

            id = 'bp.ativo.nao_circulante.intangiveis_liquido'
            identificador_periodo = '2020T4'
            saldo = self.embraer_dta.get_valor(id, identificador_periodo)

            print('id: {}\n\tidentificador_periodo: {}\n\tsaldo: {}'.format(
                    id,
                    identificador_periodo,
                    saldo))

            df = self.embraer_dta.df
            print('type(df) : {}'.format(type(df)))
            result = df.loc[id, identificador_periodo]
            s = '\n\t'.join(['id: {}',
                             'identificador_periodo: {}',
                             'type(result): {}',
                             'result:\n{}'])
            print(s.format(id,
                           identificador_periodo,
                           type(result),
                           result))

    def test_get_valor(self):
        print('\ntest_get_valor')
        index = 'bp.ativo.circulante.caixa_e_equivalentes'
        periodo = '2010T4'

        for i in range(1000):
            result = self.embraer_dta.get_valor(index, periodo)

        print('result: \n{}'.format(result))
        self.assertEqual(2321199000, result)

    def test_get_project_path(self):
        project_path = self.embraer_dta.get_project_path()
        print('project_path: {}'.format(project_path))
        self.assertIsNotNone(project_path)

    def test_get_dados_empresa_file_path(self):
        embraer_dados_path = self.embraer_dta.get_dados_empresa_file_path()
        print('embraer_dados_path: {}'.format(embraer_dados_path))
        self.assertIsNotNone(embraer_dados_path)

    def test_get_dados_empresa_file_name(self):
        embraer_dados_file_name = self.embraer_dta.get_dados_empresa_file_name()
        print('embraer_dados_file_name: {}'.format(embraer_dados_file_name))
        self.assertIsNotNone(embraer_dados_file_name)
        self.assertEqual(embraer_dados_file_name,
                'economatica_Embraer_2009T1-2021T4.xls')

    def test_get_codigos_periodos(self):
        codigos_periodos = self.embraer_dta.get_codigos_periodos()
        self.assertIsNotNone(codigos_periodos)
        self.assertEqual(52, len(codigos_periodos))

    @unittest.skipUnless(print_to_stdout, 'making_clean_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print(self.embraer_dta)

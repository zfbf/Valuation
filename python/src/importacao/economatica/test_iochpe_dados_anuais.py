from datetime import datetime
import unittest

from .iochpe_dados_anuais import IochpeDadosAnuais


class TestIochpeDadosAnuais(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.iochpe_da = IochpeDadosAnuais(2009, 2020)

    def test_get_identificador(self):
        identificador = self.iochpe_da.get_identificador()
        self.assertIsNotNone(identificador)
        self.assertEqual(identificador, 'Iochpe_2009_2020')

    def test_import_from_excel(self):
        df = self.iochpe_da.import_from_excel()
        self.assertIsNotNone(df)
        print('df.shape: {}'.format(df.shape))
        print('df.tail: {}'.format(df.tail))

    def test_get_project_path(self):
        project_path = self.iochpe_da.get_project_path()
        print('project_path: {}'.format(project_path))
        self.assertIsNotNone(project_path)

    def test_get_dados_empresa_file_path(self):
        iochpe_dados_path = self.iochpe_da.get_dados_empresa_file_path()
        print('iochpe_dados_path: {}'.format(iochpe_dados_path))
        self.assertIsNotNone(iochpe_dados_path)

    def test_get_dados_empresa_file_name(self):
        iochpe_dados_file_name = self.iochpe_da.get_dados_empresa_file_name()
        print('iochpe_dados_file_name: {}'.format(iochpe_dados_file_name))
        self.assertIsNotNone(iochpe_dados_file_name)
        self.assertEqual(iochpe_dados_file_name,
                         'economatica_Iochpe_anual_2009-2020.xls')

    @unittest.skipUnless(print_to_stdout, 'making_clean_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print(self.iochpe_da)

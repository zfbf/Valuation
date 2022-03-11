from datetime import datetime
import unittest

from .ciclo_contabil_anual import CicloContabilAnual
from ..plano_de_contas.plano_de_contas import DummyPlanoDeContas


class TestCicloContabil(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        plano_de_contas = DummyPlanoDeContas()
        self.ciclo_contabil = CicloContabilAnual(2019, plano_de_contas)

    def test_get_identificador(self):
        self.assertIsNotNone(self.ciclo_contabil.get_identificador())
        self.assertEqual(self.ciclo_contabil.get_identificador(), '2019')

    def test_get_data_inicio(self):
        cc = self.ciclo_contabil
        self.assertIsNotNone(cc.get_data_inicio())
        self.assertEqual(cc.get_data_inicio().day, 1)
        self.assertEqual(cc.get_data_inicio().month, 1)
        self.assertEqual(cc.get_data_inicio().year, 2019)

    @unittest.skipUnless(print_to_stdout, 'making_clean_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print(self.ciclo_contabil)

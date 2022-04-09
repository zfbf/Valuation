import unittest

from ..test_indice import TestIndice
from .geral import LiquidezGeral


class TestLiquidezGeral(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_geral = LiquidezGeral(
                TestLiquidezGeral.valuation, 2020, 4)

    def test_get_valor(self):
        valor = self.liquidez_geral.get_valor()
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_geral: {}'.format(self.liquidez_geral))

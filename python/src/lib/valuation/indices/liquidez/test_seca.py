import unittest

from ..test_indice import TestIndice
from .seca import LiquidezSeca


class TestLiquidezSeca(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_seca = LiquidezSeca(
                TestLiquidezSeca.valuation, 2020, 4)

    def test_get_valor(self):
        valor = self.liquidez_seca.get_valor()
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_seca: {}'.format(self.liquidez_seca))

import unittest

from ..test_indice import TestIndice
from .imediata import LiquidezImediata


class TestLiquidezImediata(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_imediata = LiquidezImediata(
                TestLiquidezImediata.valuation, 2020, 4)

    def test_get_valor(self):
        valor = self.liquidez_imediata.get_valor()
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

    def tearDown(self):
        self.liquidez_imediata = None

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_imediata: {}'.format(self.liquidez_imediata))

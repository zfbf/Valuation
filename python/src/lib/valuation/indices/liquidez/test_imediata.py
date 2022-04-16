import unittest

from ..test_indice import TestIndice
from .imediata import LiquidezImediata


class TestLiquidezImediata(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_imediata = LiquidezImediata(
                TestLiquidezImediata.valuation)

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.liquidez_imediata.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

        if TestLiquidezImediata.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.liquidez_imediata, ano,
                    trimestre, valor))

    def tearDown(self):
        self.liquidez_imediata = None

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_imediata: {}'.format(self.liquidez_imediata))

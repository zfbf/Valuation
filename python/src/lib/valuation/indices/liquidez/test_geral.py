import unittest

from ..test_indice import TestIndice
from .geral import LiquidezGeral


class TestLiquidezGeral(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_geral = LiquidezGeral(TestLiquidezGeral.valuation)

    def test_get_valor_2011T4(self):
        ano = 2011
        trimestre = 4
        valor = self.liquidez_geral.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

        if TestLiquidezGeral.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.liquidez_geral, ano,
                    trimestre, valor))

    def test_get_valor_2020T4(self):
        ano = 2020
        trimestre = 4
        valor = self.liquidez_geral.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

        if TestLiquidezGeral.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.liquidez_geral, ano,
                    trimestre, valor))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_geral: {}'.format(self.liquidez_geral))

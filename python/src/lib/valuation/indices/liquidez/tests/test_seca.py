import unittest

from ...test_indice import TestIndice
from ..seca import LiquidezSeca


class TestLiquidezSeca(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_seca = LiquidezSeca(TestLiquidezSeca.valuation)

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.liquidez_seca.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

        if TestLiquidezSeca.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.liquidez_seca, ano,
                    trimestre, valor))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_seca: {}'.format(self.liquidez_seca))

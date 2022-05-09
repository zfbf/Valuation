import unittest

from ...test_indice import TestIndice
from ..corrente import LiquidezCorrente


class TestLiquidezCorrente(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_corrente = LiquidezCorrente(
                TestLiquidezCorrente.valuation)

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.liquidez_corrente.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

        if TestLiquidezCorrente.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.liquidez_corrente, ano,
                    trimestre, valor))

    def test_get_valor_2030T4(self):
        ano = 2030
        trimestre = 4
        valor = self.liquidez_corrente.get_valor(ano, trimestre)
        self.assertIsNone(valor)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_corrente: {}'.format(self.liquidez_corrente))

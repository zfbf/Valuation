import unittest

from ..test_indice import TestIndice
from .corrente import LiquidezCorrente


class TestLiquidezCorrente(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_corrente = LiquidezCorrente(
                TestLiquidezCorrente.valuation, 2020, 4)

    def test_get_valor(self):
        valor = self.liquidez_corrente.get_valor()
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_corrente: {}'.format(self.liquidez_corrente))

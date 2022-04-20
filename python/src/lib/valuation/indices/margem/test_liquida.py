import unittest

from ..test_indice import TestIndice
from .liquida import MargemLiquida


class TestMargemLiquida(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.margem_liquida = MargemLiquida(TestMargemLiquida.valuation)

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.margem_liquida.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor != 0)

        if TestMargemLiquida.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.margem_liquida.nome, ano,
                    trimestre, valor))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nmargem_liquida: {}'.format(self.margem_liquida))

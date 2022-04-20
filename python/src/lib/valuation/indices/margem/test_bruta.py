import unittest

from ..test_indice import TestIndice
from .bruta import MargemBruta


class TestMargemBruta(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.margem_bruta = MargemBruta(TestMargemBruta.valuation)

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.margem_bruta.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor != 0)

        if TestMargemBruta.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.margem_bruta.nome, ano,
                    trimestre, valor))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nmargem_bruta: {}'.format(self.margem_bruta))

import unittest

from ..test_indice import TestIndice
from .operacional import MargemOperacional


class TestMargemOperacional(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.margem_operacional = MargemOperacional(
                TestMargemOperacional.valuation)

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.margem_operacional.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor != 0)

        if TestMargemOperacional.print_to_stdout:
            print('{} - {}T{}: {}'.format(self.margem_operacional.nome, ano,
                    trimestre, valor))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nmargem_operacional: {}'.format(self.margem_operacional))

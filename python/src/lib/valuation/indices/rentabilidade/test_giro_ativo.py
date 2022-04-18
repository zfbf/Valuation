import unittest

from ..test_indice import TestIndice
from .giro_ativo import GiroAtivo


class TestGiroAtivo(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.giro_ativo = GiroAtivo(TestGiroAtivo.valuation)

    # A receita líquida operacional pode ser negativa
    def test_get_giro(self):
        ano = 2020
        trimestre = 4
        giro = self.giro_ativo.get_giro(ano, trimestre)
        self.assertIsNotNone(giro)
        self.assertTrue(giro != 0)

        if TestGiroAtivo.print_to_stdout:
            print('test_get_giro, ano: {}, trimestre: {}'.format(
                    ano, trimestre))
            print('\tgiro: {}'.format(giro))

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.giro_ativo.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor != 0)

        if TestGiroAtivo.print_to_stdout:
            print('test_get_valor, ano: {}, trimestre: {}'.format(
                    ano, trimestre))
            print('\tvalor: {}'.format(valor))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\ngiro_ativo: {}'.format(self.giro_ativo))

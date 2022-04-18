import unittest

from ..test_indice import TestIndice
from .prazo_medio_estoques import PrazoMedioEstoques


class TestPrazoMedioEstoques(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.prazo_medio_estoques = PrazoMedioEstoques(
                TestPrazoMedioEstoques.valuation)

    # A receita líquida operacional pode ser negativa
    def test_get_giro(self):
        ano = 2020
        trimestre = 4
        giro = self.prazo_medio_estoques.get_giro(ano, trimestre)
        self.assertIsNotNone(giro)
        self.assertTrue(giro != 0)

        if TestPrazoMedioEstoques.print_to_stdout:
            print('test_get_giro, ano: {}, trimestre: {}'.format(
                    ano, trimestre))
            print('\tgiro: {}'.format(giro))

    def test_get_valor(self):
        ano = 2020
        trimestre = 4
        valor = self.prazo_medio_estoques.get_valor(ano, trimestre)
        self.assertIsNotNone(valor)
        self.assertTrue(valor != 0)

        if TestPrazoMedioEstoques.print_to_stdout:
            print('test_get_valor, ano: {}, trimestre: {}'.format(
                    ano, trimestre))
            print('\tvalor: {}'.format(valor))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nprazo_medio_estoques: {}'.format(self.prazo_medio_estoques))

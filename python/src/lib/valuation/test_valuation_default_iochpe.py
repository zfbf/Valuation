import unittest

from .valuation_default import ValuationDefault
from .periodo_contabil import PeriodoContabil
from ..importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from .factories.valuation_factory import ValuationDefaultFactory


class TestValuationDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        iochpe_economatica_dados = IochpeDadosAnuais(2009, 2020)
        valuation_factory = ValuationDefaultFactory()
        self.valuation = valuation_factory.build(iochpe_economatica_dados)
        valuation_factory.load(self.valuation, iochpe_economatica_dados)

    def test_get_empresa(self):
        self.assertIsNotNone(self.valuation.empresa)

    def test_get_periodos(self):
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(len(self.valuation.get_periodos()), 12)

    def test_get_periodo(self):
        identificador = 'Inexistente'
        self.assertIsNone(self.valuation.get_periodo(identificador))
        identificador = '2021'
        self.assertIsNotNone(self.valuation.get_periodo(identificador))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nvaluation: {}'.format(self.valuation))

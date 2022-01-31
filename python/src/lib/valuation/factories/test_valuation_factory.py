import unittest

from .valuation_factory import ValuationDefaultFactory
from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais


class TestValuationDefault(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = IochpeDadosAnuais(2009, 2010)
        self.valuation_factory = ValuationDefaultFactory()

    def test_build(self):
        valuation = self.valuation_factory.build(self.economatica_dados)
        self.assertIsNotNone(valuation)
        self.assertIsNotNone(valuation.get_empresa())
        self.assertIsNotNone(valuation.get_periodos())

    def test_load(self):
        valuation = self.valuation_factory.build(self.economatica_dados)
        self.valuation_factory.load(valuation, self.economatica_dados)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        valuation = self.valuation_factory.build(
                self.economatica_dados)
        self.valuation_factory.load(valuation, self.economatica_dados)
        print('\nvaluation: {}'.format(valuation))

import unittest

from .valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from ...importacao.economatica.iochpe_dados_trimestrais_anualizados import Iochpe2009T12021T4


class TestValuationPeriodoTrimestralFactory(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe2009T12021T4()
        self.economatica_dados.prepare()
        self.valuation_factory = ValuationPeriodoTrimestralFactory()

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

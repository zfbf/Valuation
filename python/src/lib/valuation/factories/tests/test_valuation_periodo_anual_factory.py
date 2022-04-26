import unittest

from ..valuation_periodo_anual_factory import ValuationPeriodoAnualFactory
from ....importacao.economatica.empresas.iochpe.dados_2009_2020 import Iochpe20092020


class TestValuationPeriodoTrimestralFactory(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe20092020()
        self.economatica_dados.prepare()
        self.valuation_factory = ValuationPeriodoAnualFactory()

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

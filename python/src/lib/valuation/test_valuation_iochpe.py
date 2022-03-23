import unittest

from .valuation_default import ValuationDefault
from ..contabilidade.periodo_contabil import PeriodoContabil
from ..importacao.economatica.iochpe_dados_trimestrais_anualizados import Iochpe2009T12021T4
from .factories.valuation_factory import ValuationDefaultFactory


class TestValuationDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        iochpe_economatica_dados = Iochpe2009T12021T4()
        iochpe_economatica_dados.prepare()
        valuation_factory = ValuationDefaultFactory()
        self.valuation = valuation_factory.build(iochpe_economatica_dados)
        valuation_factory.load(self.valuation, iochpe_economatica_dados)

    def test_get_empresa(self):
        self.assertIsNotNone(self.valuation.empresa)

    def test_get_periodos(self):
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(len(self.valuation.get_periodos()), 52)

    def test_get_periodo(self):
        #identificador = 'Inexistente'
        #self.assertIsNone(self.valuation.get_periodo(identificador))
        identificador = '2020T4'
        self.assertIsNotNone(self.valuation.get_periodo(identificador))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nvaluation: {}'.format(self.valuation))

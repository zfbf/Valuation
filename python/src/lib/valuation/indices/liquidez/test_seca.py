import unittest

from .seca import LiquidezSeca
from ....importacao.economatica.oi_dados_trimestrais_anualizados import Oi2009T12021T3
from ...factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory


class TestLiquidezSeca(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.liquidez_seca = LiquidezSeca(
                TestLiquidezSeca.periodo_contabil)

    def test_get_valor(self):
        valor = self.liquidez_seca.get_valor()
        self.assertIsNotNone(valor)
        self.assertTrue(valor > 0)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nliquidez_seca: {}'.format(self.liquidez_seca))

    @classmethod
    def setUpClass(cls):
        cls.periodo_contabil = cls.build_periodo_contabil()

    @classmethod
    def build_periodo_contabil(cls):
        oi_economatica_dados = Oi2009T12021T3()
        oi_economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        valuation = valuation_factory.build(oi_economatica_dados)
        valuation_factory.load(valuation, oi_economatica_dados)
        codigo_periodo = '2020T4'
        periodo_contabil = valuation.get_periodo(codigo_periodo)
        return periodo_contabil

    @classmethod
    def tearDownClass(cls):
        cls.periodo_contabil = None

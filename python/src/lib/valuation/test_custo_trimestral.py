import unittest

from .valuation_default import ValuationDefault
#from ..contabilidade.periodo_contabil_trimestral import PeriodoContabilTrimestral
from ..importacao.economatica.oi_dados_trimestrais_anualizados import Oi2009T12021T3
from .factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from .custo_trimestral import CustoTrimestral


class TestCustoTrimestral(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.custo = CustoTrimestral(TestCustoTrimestral.periodo_contabil)

    def tearDown(self):
        self.custo = None

    def test_get_kd(self):
        kd = self.custo.get_kd()
        self.assertIsNotNone(kd)
        self.assertTrue(kd > 0)

    def test_get_ke(self):
        ke = self.custo.get_ke()
        self.assertIsNotNone(ke)
        self.assertTrue(ke > 0)

    def test_get_wacc(self):
        wacc = self.custo.get_wacc()
        self.assertIsNotNone(wacc)
        self.assertTrue(wacc > 0)

    def test_get_ebit(self):
        ebit = self.custo.get_ebit()
        self.assertIsNotNone(ebit)
        self.assertTrue(ebit.get_saldo() != 0)

    def test_get_ano(self):
        ano = self.custo.get_ano()
        self.assertIsNotNone(ano)
        self.assertEqual(ano, 2021)

    def test_get_trimestre(self):
        trimestre = self.custo.get_trimestre()
        self.assertIsNotNone(trimestre)
        self.assertEqual(trimestre, 3)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\ncusto: {}'.format(self.custo))

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
        codigo_periodo = '2021T3'
        periodo_contabil = valuation.get_periodo(codigo_periodo)
        return periodo_contabil

    @classmethod
    def tearDownClass(cls):
        cls.periodo_contabil = None

import unittest

from .ativo_nao_circulante import AtivoNaoCirculanteIFRS
from ....importacao.economatica.oi_dados_trimestrais_anualizados import Oi2009T12021T3
from ....valuation.factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory


class TestAtivoNaoCirculanteIFRS(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        periodo_contabil = TestAtivoNaoCirculanteIFRS.periodo_contabil
        self.ativo_nao_circulante = periodo_contabil.bp_ifrs.ativo.nao_circulante

    def test_get_conta(self):
        self.assertIsNotNone(self.ativo_nao_circulante.get_conta('realizavel_lp'))
        self.assertIsNone(self.ativo_nao_circulante.get_conta('não existe'))

    def test_get_saldo_realizavel_a_longo_prazo(self):
        saldo = self.ativo_nao_circulante.get_saldo_realizavel_a_longo_prazo()
        self.assertTrue(saldo > 0)
        self.assertEqual(saldo, 12087591000)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('ativo_nao_circulante: {}'.format(self.ativo_nao_circulante))

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

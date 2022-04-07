import unittest

from .prazo_medio_recebimento import PrazoMedioRecebimento
from ....importacao.economatica.oi_dados_trimestrais_anualizados import Oi2009T12021T3
from ...factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory


class TestPrazoMedioRecebimento(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.prazo_medio_recebimento = PrazoMedioRecebimento(
                TestPrazoMedioRecebimento.periodo_contabil)

    # A receita líquida operacional pode ser negativa
    def test_get_giro(self):
        giro = self.prazo_medio_recebimento.get_giro()
        self.assertIsNotNone(giro)
        self.assertTrue(giro != 0)

    def test_get_valor(self):
        valor = self.prazo_medio_recebimento.get_valor()
        self.assertIsNotNone(valor)
        self.assertTrue(valor != 0)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nprazo_medio_recebimento: {}'.format(self.prazo_medio_recebimento))

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

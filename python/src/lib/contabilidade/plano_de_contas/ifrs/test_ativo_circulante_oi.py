import unittest

from .ativo_circulante import AtivoCirculanteIFRS
from ....importacao.economatica.oi_dados_trimestrais_anualizados import Oi2009T12021T3
from ....valuation.factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory


class TestAtivoCirculanteIFRS(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        periodo_contabil = TestAtivoCirculanteIFRS.periodo_contabil
        self.ativo_circulante = periodo_contabil.bp_ifrs.ativo.circulante

    def tearDown(self):
        self.ativo_circulante = None

    def test_get_conta_caixa(self):
        self.assertIsNotNone(self.ativo_circulante.get_conta_caixa())

    def test_get_conta(self):
        contas = ('caixa_e_equivalentes',
                  'aplicacoes_financeiras',
                  'contas_a_receber',
                  'estoques',
                  'ativos_biologicos',
                  'impostos_a_recuperar',
                  'despesas_antecipadas',
                  'outros')

        for conta in contas:
            self.assertIsNotNone(self.ativo_circulante.get_conta(conta))

        self.assertIsNone(self.ativo_circulante.get_conta('não existe'))

    def test_get_contas_disponibilidades(self):
        contas_disponibilidades = self.ativo_circulante.get_contas_disponibilidades()
        self.assertIsNotNone(contas_disponibilidades)
        self.assertEqual(len(contas_disponibilidades), 2)

    def test_get_saldo_disponibilidades(self):
        saldo = self.ativo_circulante.get_saldo_disponibilidades()
        self.assertIsNotNone(saldo)
        self.assertEqual(saldo, 4301656000)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('ativo_circulante: {}'.format(self.ativo_circulante))

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

import unittest

from ..valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from ..dre_loader import DRELoader
from ....importacao.economatica.empresas.iochpe.dados_2009T1_2021T4 import Iochpe2009T12021T4


class TestDRELoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe2009T12021T4()
        self.economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.dre_2010 = periodos[1].dre
        self.dre_loader = DRELoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(52, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.dre_2010)
        self.dre_loader.load(self.dre_2010,
                             '2010T4',
                             self.economatica_dados)
        dre = self.dre_2010
        self.assertTrue(dre.receita_liquida_operacional.get_saldo() != 0)
        self.assertIsNotNone(dre.lucro_bruto.valor_verificacao)
        self.assertIsNotNone(dre.despesas_operacionais.valor_verificacao)
        self.assertIsNotNone(dre.lajir.valor_verificacao)
        self.assertIsNotNone(dre.resultado_financeiro.valor_verificacao)
        self.assertIsNotNone(dre.lair.valor_verificacao)
        self.assertIsNotNone(dre.ircs.valor_verificacao)
        self.assertIsNotNone(dre.lucro_oper_continuadas.valor_verificacao)
        self.assertIsNotNone(dre.lucro_consolidado.valor_verificacao)
        self.assertIsNotNone(dre.lucro_liquido.valor_verificacao)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\ndre_2010: {}'.format(self.dre_2010))

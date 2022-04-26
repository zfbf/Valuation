import unittest

from ..valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from ..dfc_loader import DFCLoader
from ....importacao.economatica.empresas.iochpe.dados_2009T1_2021T4 import Iochpe2009T12021T4


class TestDFCLoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe2009T12021T4()
        self.economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.dfc_2010 = periodos[1].dfc
        self.dfc_loader = DFCLoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(52, len(self.valuation.get_periodos()))
        dfc = self.dfc_2010
        self.assertIsNotNone(dfc)
        self.dfc_loader.load(dfc, '2010T4', self.economatica_dados)
        self.assertIsNotNone(dfc.variacao_liquida_de_caixa.valor_verificacao)
        self.assertIsNotNone(dfc.operacional.valor_verificacao)
        operacao = dfc.operacional.get_conta('operacao')
        self.assertIsNotNone(operacao.valor_verificacao)
        var_atv_pass = dfc.operacional.get_conta('variacao_ativos_passivos')
        self.assertIsNotNone(var_atv_pass.valor_verificacao)
        self.assertIsNotNone(dfc.investimentos.valor_verificacao)
        compra_liquida_ativos_permanentes = dfc.investimentos.get_conta(
                'compra_liquida_ativos_permanentes')
        self.assertIsNotNone(compra_liquida_ativos_permanentes.valor_verificacao)
        self.assertIsNotNone(dfc.financiamentos.valor_verificacao)
        financiamentos_liquido = dfc.financiamentos.get_conta(
                'financiamentos_liquido')
        self.assertIsNotNone(financiamentos_liquido.valor_verificacao)
        aumento_liquido_de_capital = dfc.financiamentos.get_conta(
                'aumento_liquido_de_capital')
        self.assertIsNotNone(aumento_liquido_de_capital.valor_verificacao)


    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\ndfc_2010: {}'.format(self.dfc_2010))

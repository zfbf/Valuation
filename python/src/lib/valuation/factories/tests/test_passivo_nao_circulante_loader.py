import unittest

from ..valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from ..passivo_nao_circulante_loader import PassivoNaoCirculanteIFRSLoader
from ....importacao.economatica.empresas.iochpe.dados_2009T1_2021T4 import Iochpe2009T12021T4


class TestPassivoNaoCirculanteIFRSLoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe2009T12021T4()
        self.economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.passivo_nao_circulante_2010 = periodos[1].bp_ifrs.passivo.nao_circulante
        self.passivo_nao_circulante_loader = PassivoNaoCirculanteIFRSLoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(52, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.passivo_nao_circulante_2010)
        self.passivo_nao_circulante_loader.load(self.passivo_nao_circulante_2010,
                                                '2010T4',
                                                self.economatica_dados)
        passivo_nao_circulante = self.passivo_nao_circulante_2010
        self.assertIsNotNone(passivo_nao_circulante.valor_verificacao)
        emp_e_fin = passivo_nao_circulante.get_conta(
                'emprestimos_e_financiamentos')
        self.assertIsNotNone(emp_e_fin.valor_verificacao)
        self.assertEquals(emp_e_fin.valor_verificacao, 592867000)
        financiamentos = emp_e_fin.get_conta('financiamentos')
        self.assertIsNotNone(financiamentos.valor_verificacao)
        self.assertEquals(financiamentos.valor_verificacao, 592867000)
        outras_obrigacoes = passivo_nao_circulante.get_conta('outras_obrigacoes')
        self.assertIsNotNone(outras_obrigacoes.valor_verificacao)
        self.assertEquals(outras_obrigacoes.valor_verificacao, 11089000)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\npassivo_nao_circulante_2010: {}'.format(
              self.passivo_nao_circulante_2010))

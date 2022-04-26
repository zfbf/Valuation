import unittest

from ..valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from ..passivo_circulante_loader import PassivoCirculanteIFRSLoader
from ....importacao.economatica.empresas.iochpe.dados_2009T1_2021T4 import Iochpe2009T12021T4


class TestPassivoCirculanteIFRSLoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe2009T12021T4()
        self.economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.passivo_circulante_2021T4 = periodos[-1].bp_ifrs.passivo.circulante
        self.passivo_circulante_loader = PassivoCirculanteIFRSLoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(52, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.passivo_circulante_2021T4)
        self.passivo_circulante_loader.load(self.passivo_circulante_2021T4,
                                            '2021T4',
                                            self.economatica_dados)
        passivo_circulante = self.passivo_circulante_2021T4
        self.assertIsNotNone(passivo_circulante.valor_verificacao)
        emp_e_fin = passivo_circulante.get_conta('emprestimos_e_financiamentos')
        self.assertIsNotNone(emp_e_fin.valor_verificacao)
        outras_obrigacoes = passivo_circulante.get_conta('outras_obrigacoes')
        self.assertIsNotNone(outras_obrigacoes.valor_verificacao)
        outros_cp = outras_obrigacoes.get_conta('outros_cp')
        self.assertIsNotNone(outros_cp.valor_verificacao)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\npassivo_circulante_2021T4: {}'.format(
                self.passivo_circulante_2021T4))

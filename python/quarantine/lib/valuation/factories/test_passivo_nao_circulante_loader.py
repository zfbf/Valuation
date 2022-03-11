import unittest

from .valuation_factory import ValuationDefaultFactory
from .passivo_nao_circulante_loader import PassivoNaoCirculanteDefaultLoader
from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais


class TestPassivoNaoCirculanteDefaultLoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = IochpeDadosAnuais(2009, 2010)
        valuation_factory = ValuationDefaultFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.passivo_nao_circulante_2010 = periodos[1]['bp'].passivo.nao_circulante
        self.passivo_nao_circulante_loader = PassivoNaoCirculanteDefaultLoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(2, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.passivo_nao_circulante_2010)
        self.passivo_nao_circulante_loader.load(self.passivo_nao_circulante_2010,
                                                '2010',
                                                self.economatica_dados)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\npassivo_nao_circulante_2010: {}'.format(
              self.passivo_nao_circulante_2010))

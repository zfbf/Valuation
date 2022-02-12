import unittest

from .valuation_factory import ValuationDefaultFactory
from .dre_loader import DRELoader
from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais


class TestDRELoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = IochpeDadosAnuais(2009, 2010)
        valuation_factory = ValuationDefaultFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.dre_2010 = periodos[1]['dre']
        self.dre_loader = DRELoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(2, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.dre_2010)
        self.dre_loader.load(self.dre_2010,
                             '2010',
                             self.economatica_dados)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\ndre_2010: {}'.format(self.dre_2010))

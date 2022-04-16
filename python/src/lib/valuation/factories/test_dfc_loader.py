import unittest

from .valuation_factory import ValuationDefaultFactory
from .dfc_loader import DFCLoader
from ...importacao.economatica.iochpe_dados_trimestrais_anualizados import Iochpe2009T12021T4


class TestDFCLoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe2009T12021T4()
        self.economatica_dados.prepare()
        valuation_factory = ValuationDefaultFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.dfc_2010 = periodos[1].dfc
        self.dfc_loader = DFCLoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(52, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.dfc_2010)
        self.dfc_loader.load(self.dfc_2010,
                             '2010T4',
                             self.economatica_dados)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\ndfc_2010: {}'.format(self.dfc_2010))

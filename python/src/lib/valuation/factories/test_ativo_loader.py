import unittest

from .valuation_factory import ValuationDefaultFactory
from .ativo_loader import AtivoIFRSLoader
from ...importacao.economatica.iochpe_dados_trimestrais_anualizados import Iochpe2009T12021T4


class TestAtivoCirculanteDefaultLoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = Iochpe2009T12021T4()
        self.economatica_dados.prepare()
        valuation_factory = ValuationDefaultFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.ativo_2010 = periodos[1].bp_ifrs.ativo.circulante
        self.ativo_loader = AtivoIFRSLoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(52, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.ativo_2010)
        self.ativo_loader.load(self.ativo_2010,
                               '2010T4',
                               self.economatica_dados)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\nativo_2010: {}'.format(self.ativo_2010))

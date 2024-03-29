import unittest

from .valuation_factory import ValuationDefaultFactory
from .ativo_circulante_loader import AtivoCirculanteDefaultLoader
from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais


class TestAtivoCirculanteDefaultLoader(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.economatica_dados = IochpeDadosAnuais(2009, 2010)
        valuation_factory = ValuationDefaultFactory()
        self.valuation = valuation_factory.build(self.economatica_dados)
        periodos = self.valuation.get_periodos()
        self.ativo_circulante_2010 = periodos[1]['bp'].ativo.circulante
        self.ativo_circulante_loader = AtivoCirculanteDefaultLoader()

    def test_load(self):
        self.assertIsNotNone(self.valuation)
        self.assertIsNotNone(self.valuation.get_empresa())
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(2, len(self.valuation.get_periodos()))
        self.assertIsNotNone(self.ativo_circulante_2010)
        self.ativo_circulante_loader.load(self.ativo_circulante_2010,
                                          '2010',
                                          self.economatica_dados)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        self.test_load()
        print('\nativo_circulante_2010: {}'.format(self.ativo_circulante_2010))

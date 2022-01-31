import unittest

from .valuation_default import ValuationDefault
from .periodo_contabil import PeriodoContabil
from .bperiodo_contabil import PeriodoContabil
from BalancoPatrimonialDefault


class TestValuationDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.valuation = ValuationDefault('Default')
        periodo = PeriodoContabil('2021')





        self.valuation.append_periodo(periodo)

    def test_get_empresa(self):
        self.assertIsNotNone(self.valuation.empresa)

    def test_get_periodos(self):
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(len(self.valuation.get_periodos()), 1)

    def test_get_periodo(self):
        identificador = 'Inexistente'
        self.assertIsNone(self.valuation.get_periodo(identificador))
        identificador = '2021'
        self.assertIsNotNone(self.valuation.get_periodo(identificador))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nvaluation: {}'.format(self.valuation))

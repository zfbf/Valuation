import unittest

from .periodo_contabil import PeriodoContabil


class TestValuationDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.periodo = PeriodoContabil('2021')

    def test_get_identificador(self):
        self.assertIsNotNone(self.periodo.identificador)
        self.assertEqual(self.periodo.identificador, '2021')

    def test_bp_ifrs(self):
        self.assertIsNotNone(self.periodo.bp_ifrs)

    def test_bp_dre(self):
        self.assertIsNotNone(self.periodo.dre)

    def test_bp_dfc(self):
        self.assertIsNotNone(self.periodo.dfc)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nPeriodoContabil: {}'.format(self.periodo))

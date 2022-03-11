import unittest

from .periodo_contabil import PeriodoContabil


class TestPeriodoContabil(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.periodo = PeriodoContabil('2021')

    def test_get_periodos(self):
        self.assertIsNone(self.periodo.bp)
        self.assertIsNone(self.periodo.dre)
        self.assertIsNone(self.periodo.fc)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('periodo: {}'.format(self.periodo))

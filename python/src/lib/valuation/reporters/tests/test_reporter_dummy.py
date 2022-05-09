import unittest

from ..reporter_default import ReporterDefault
from ...valuation_default import ValuationDefault
from ....contabilidade.periodo_contabil import PeriodoContabil


class TestReporter(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.reporter = ReporterDefault()

    def test_execute(self):
        valuation = ValuationDefault('Default', 'ticker')
        periodo = PeriodoContabil('2021')
        valuation.append_periodo(periodo)
        report = self.reporter.execute(valuation)
        self.assertIsNotNone(report)

    def test_ano_tri_frac_index(self):
        ano_inicial = 2009
        trimestre_inicial = 3
        ano_final = 2021
        trimestre_final = 4
        ano_tri_frac_array = self.reporter.get_ano_tri_frac_index(ano_inicial,
                trimestre_inicial, ano_final, trimestre_final)
        self.assertIsNotNone(ano_tri_frac_array)
        print('ano_tri_frac_array: {}'.format(ano_tri_frac_array))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nreporter: {}'.format(self.reporter))

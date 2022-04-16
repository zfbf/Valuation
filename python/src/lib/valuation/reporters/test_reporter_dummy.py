import unittest

from .reporter_default import ReporterDefault
from ..valuation_default import ValuationDefault
from ...contabilidade.periodo_contabil import PeriodoContabil


class TestReporter(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.reporter = ReporterDefault()

    def test_execute(self):
        valuation = ValuationDefault('Default')
        periodo = PeriodoContabil('2021')
        valuation.append_periodo(periodo)
        report = self.reporter.execute(valuation)
        self.assertIsNotNone(report)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nreporter: {}'.format(self.reporter))

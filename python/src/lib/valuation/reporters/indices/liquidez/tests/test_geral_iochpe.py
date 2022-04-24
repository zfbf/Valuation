import unittest

from ..geral import IndiceLiquidezGeralReporter
from .....tests.fixture_test_valuation_iochpe import FixtureValuationIochpe2009T12021T4


class TestIndiceLiquidezGeralReporter(FixtureValuationIochpe2009T12021T4):
    print_to_stdout = False

    def setUp(self):
        self.valuation = TestIndiceLiquidezGeralReporter.valuation

    def tearDown(self):
        self.valuation = None

    def test_execute(self):
        reporter = IndiceLiquidezGeralReporter()
        report = reporter.execute(self.valuation, outros=[None] * 5)
        self.assertIsNotNone(report)

    def test_ensure_args_inicio_fim(self):
        kwargs = {}
        reporter = IndiceLiquidezGeralReporter()
        report = reporter.ensure_args_inicio_fim(self.valuation, kwargs)
        self.assertIsNotNone(kwargs['ano_inicial'])
        self.assertIsNotNone(kwargs['trimestre_inicial'])
        self.assertIsNotNone(kwargs['ano_final'])
        self.assertIsNotNone(kwargs['trimestre_final'])

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nreporter: {}'.format(self.reporter))

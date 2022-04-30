import unittest

from ..reporter_default import ReporterDefault
from ...valuation_default import ValuationDefault
from ....contabilidade.periodo_contabil import PeriodoContabil
from ....importacao.economatica.empresas.iochpe.dados_2009_2020 import Iochpe20092020
from ...    factories.valuation_periodo_anual_factory import ValuationPeriodoAnualFactory


class TestReporter(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.reporter = ReporterDefault()

    def test_execute(self):
        iochpe_economatica_dados = Iochpe20092020()
        valuation_factory = ValuationPeriodoAnualFactory()
        valuation = valuation_factory.build(iochpe_economatica_dados)
        valuation_factory.load(valuation, iochpe_economatica_dados)
        report = self.reporter.execute(valuation)
        self.assertIsNotNone(report)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nreporter: {}'.format(self.reporter))

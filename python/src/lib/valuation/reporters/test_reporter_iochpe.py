import unittest

from .reporter_default import ReporterDefault
from ..valuation_default import ValuationDefault
from ...contabilidade.periodo_contabil import PeriodoContabil
from ...importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ..factories.valuation_factory import ValuationDefaultFactory


class TestReporter(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.reporter = ReporterDefault()

    def test_execute(self):
        iochpe_economatica_dados = IochpeDadosAnuais(2009, 2020)
        valuation_factory = ValuationDefaultFactory()
        valuation = valuation_factory.build(iochpe_economatica_dados)
        valuation_factory.load(valuation, iochpe_economatica_dados)
        self.reporter.execute(valuation)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nreporter: {}'.format(self.reporter))

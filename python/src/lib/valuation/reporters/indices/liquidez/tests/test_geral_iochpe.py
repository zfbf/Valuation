import unittest

from ..geral import IndiceLiquidezGeralReporter
from .....factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from ......importacao.economatica.empresas.iochpe.dados_2009T1_2021T4 import Iochpe2009T12021T4
from ......importacao.economatica.empresas.embraer.dados_2009T1_2021T4 import Embraer2009T12021T4
from ......importacao.economatica.empresas.frasle.dados_2009T1_2021T4 import FrasLe2009T12021T4
from ......importacao.economatica.empresas.mahle_metal_leve.dados_2009T1_2021T4 import MahleMetalLeve2009T12021T4
from ......importacao.economatica.empresas.marcopolo.dados_2009T1_2021T4 import Marcopolo2009T12021T4
from ......importacao.economatica.empresas.randon.dados_2009T1_2021T4 import Randon2009T12021T4


class TestIndiceLiquidezGeralReporter(unittest.TestCase):
    print_to_stdout = True

    @classmethod
    def setUpClass(cls):
        cls.valuation_base = cls.build_valuation_base()
        cls.valuation_outros = cls.build_valuation_outros()

    @classmethod
    def build_valuation_base(cls):
        economatica_dados = Iochpe2009T12021T4()
        economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        valuation = valuation_factory.build(economatica_dados)
        valuation_factory.load(valuation, economatica_dados)
        return valuation

    @classmethod
    def build_valuation_outros(cls):
        dados_array = [Embraer2009T12021T4(),
                       FrasLe2009T12021T4(),
                       MahleMetalLeve2009T12021T4(),
                       Marcopolo2009T12021T4(),
                       Randon2009T12021T4()]
        valuation_factory = ValuationPeriodoTrimestralFactory()
        valuation_array = []

        for dados in dados_array:
            dados.prepare()
            valuation = valuation_factory.build(dados)
            valuation_factory.load(valuation, dados)
            valuation_array.append(valuation)

        return valuation_array

    @classmethod
    def tearDownClass(cls):
        cls.valuation = None

    def setUp(self):
        self.valuation_base = TestIndiceLiquidezGeralReporter.valuation_base
        self.valuation_outros = TestIndiceLiquidezGeralReporter.valuation_outros

    def tearDown(self):
        self.valuation_base = None

    def test_execute(self):
        reporter = IndiceLiquidezGeralReporter(self.valuation_base)
        outros_valuations = self.valuation_outros
        report = reporter.execute(outros=outros_valuations)
        self.assertIsNotNone(report)
        return report

    def test_ensure_args_inicio_fim(self):
        kwargs = {}
        reporter = IndiceLiquidezGeralReporter(self.valuation_base)
        report = reporter.ensure_args_inicio_fim(kwargs)
        self.assertIsNotNone(kwargs['ano_inicial'])
        self.assertIsNotNone(kwargs['trimestre_inicial'])
        self.assertIsNotNone(kwargs['ano_final'])
        self.assertIsNotNone(kwargs['trimestre_final'])

    def test_save_to_latex(self):
        reporter = IndiceLiquidezGeralReporter(self.valuation_base)
        outros_valuations = self.valuation_outros
        report = reporter.execute(outros=outros_valuations, save_to_latex=True)
        self.assertIsNotNone(report)
        return report

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nDentro de test_to_str')
        report = self.test_execute()
        print('\n'.join('{}:\t{}'.format(k, v) for k, v in report.items()))
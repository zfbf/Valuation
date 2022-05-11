import unittest

from ..imediata import IndiceLiquidezImediataReporter
from .....factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory
from ......importacao.economatica.empresas.oi.dados_2009T1_2021T3 import Oi2009T12021T3
from ......importacao.economatica.empresas.tim.dados_2009T1_2021T3 import Tim2009T12021T3
from ......importacao.economatica.empresas.telefonica_brasil.dados_2009T1_2021T4 import TelefonicaBrasil2009T12021T4


class TestIndiceLiquidezImediataReporter(unittest.TestCase):
    print_to_stdout = False

    @classmethod
    def setUpClass(cls):
        cls.valuation_base = cls.build_valuation_base()
        cls.valuation_outros = cls.build_valuation_outros()

    @classmethod
    def build_valuation_base(cls):
        economatica_dados = Oi2009T12021T3()
        economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        valuation = valuation_factory.build(economatica_dados)
        valuation_factory.load(valuation, economatica_dados)
        return valuation

    @classmethod
    def build_valuation_outros(cls):
        dados_array = [Tim2009T12021T3(),
                       TelefonicaBrasil2009T12021T4()]
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
        self.valuation_base = TestIndiceLiquidezImediataReporter.valuation_base
        self.valuation_outros = TestIndiceLiquidezImediataReporter.valuation_outros

    def tearDown(self):
        self.valuation_base = None

    def test_execute(self):
        reporter = IndiceLiquidezImediataReporter(self.valuation_base)
        outros_valuations = self.valuation_outros
        report = reporter.execute(ano_inicial=2011, trimestre_inicial=4,
                outros=outros_valuations)
        self.assertIsNotNone(report)
        return report

    def test_ensure_args_inicio_fim(self):
        kwargs = {}
        reporter = IndiceLiquidezImediataReporter(self.valuation_base)
        report = reporter.ensure_args_inicio_fim(kwargs)
        self.assertIsNotNone(kwargs['ano_inicial'])
        self.assertIsNotNone(kwargs['trimestre_inicial'])
        self.assertIsNotNone(kwargs['ano_final'])
        self.assertIsNotNone(kwargs['trimestre_final'])

    def test_save_to_latex(self):
        reporter = IndiceLiquidezImediataReporter(self.valuation_base)
        outros_valuations = self.valuation_outros
        report = reporter.execute(outros=outros_valuations, ano_inicial=2010,
                trimestre_inicial=4, ano_final=2022, trimestre_final=1,
                save_to_latex=True)
        #report = reporter.execute(outros=outros_valuations, ano_inicial=2011,
        #        trimestre_inicial=4, save_to_latex=True)
        self.assertIsNotNone(report)
        return report

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nDentro de test_to_str')
        report = self.test_execute()
        print('\n'.join('{}:\t{}'.format(k, v) for k, v in report.items()))

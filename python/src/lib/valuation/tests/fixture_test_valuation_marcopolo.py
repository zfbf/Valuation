import unittest

from ...importacao.economatica.empresas.marcopolo.dados_2009T1_2021T4 import Marcopolo2009T12021T4
from ..factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory


class FixtureValuationMarcopolo2009T12021T4(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valuation = cls.build_valuation()

    @classmethod
    def build_valuation(cls):
        economatica_dados = Marcopolo2009T12021T4()
        economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        valuation = valuation_factory.build(economatica_dados)
        valuation_factory.load(valuation, economatica_dados)
        return valuation

    @classmethod
    def tearDownClass(cls):
        cls.valuation = None

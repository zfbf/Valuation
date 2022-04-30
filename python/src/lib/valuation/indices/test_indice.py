import unittest

from ...importacao.economatica.empresas.iochpe.dados_2009T1_2021T4 import Iochpe2009T12021T4
#from ...importacao.economatica.empresas.oi.dados_2009T1_2021T3 import Oi2009T12021T3
from ..factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory


class TestIndice(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.valuation = cls.build_valuation()

    @classmethod
    def build_valuation(cls):
        oi_economatica_dados = Iochpe2009T12021T4()
        #oi_economatica_dados = Oi2009T12021T3()
        oi_economatica_dados.prepare()
        valuation_factory = ValuationPeriodoTrimestralFactory()
        valuation = valuation_factory.build(oi_economatica_dados)
        valuation_factory.load(valuation, oi_economatica_dados)
        return valuation

    @classmethod
    def tearDownClass(cls):
        cls.valuation = None

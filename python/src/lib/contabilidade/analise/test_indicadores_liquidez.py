import unittest

from .indicadores_liquidez import IndicadoresLiquidez
from empresas.dummy.ciclo_contabil_anual_dummy_factory import CicloContabilAnualDummyFactory


class TestPlanoDeContasOtp(unittest.TestCase):

    def setUp(self):
        ciclo_contabil_anual = CicloContabilAnualDummyFactory().execute(ano=2019)
        plano_de_contas = ciclo_contabil_anual.plano_de_contas
        self.indicadores_liquidez = IndicadoresLiquidez(plano_de_contas)

    def test_get_liquidez_imediata(self):
        liquidez_imediata = self.indicadores_liquidez.get_liquidez_imediata()
        self.assertIsNotNone(liquidez_imediata)
        print('\nliquidez_imediata: {:.2f}'.format(liquidez_imediata))

    def test_get_liquidez_seca(self):
        liquidez_seca = self.indicadores_liquidez.get_liquidez_seca()
        self.assertIsNotNone(liquidez_seca)
        print('\nliquidez_seca: {:.2f}'.format(liquidez_seca))

    def test_get_liquidez_corrente(self):
        liquidez_corrente = self.indicadores_liquidez.get_liquidez_corrente()
        self.assertIsNotNone(liquidez_corrente)
        print('\nliquidez_corrente: {:.2f}'.format(liquidez_corrente))

    def test_get_liquidez_geral(self):
        liquidez_geral = self.indicadores_liquidez.get_liquidez_geral()
        self.assertIsNotNone(liquidez_geral)
        print('\nliquidez_geral: {:.2f}'.format(liquidez_geral))

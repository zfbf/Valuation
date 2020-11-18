import unittest

from .indicadores_liquidez import IndicadoresLiquidez
from empresas.otp.ciclo_contabil_anual_otp_factory import CicloContabilAnualOtpFactory


class TestPlanoDeContasOtp(unittest.TestCase):

    def setUp(self):
        self.indicadores_liqquidez = IndicadoresLiquidez()

    def test_get_liquidez_imediata(self):
        indicador_liquidez =

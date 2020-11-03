import unittest

from .plano_de_contas_otp import PlanoDeContasOtp
#from ..lancamento_contabil import LancamentoContabil


class TestPlanoDeContasOtp(unittest.TestCase):

    def setUp(self):
        self.pc = PlanoDeContasOtp()

    def test_attributes(self):
        self.assertIsNotNone(self.pc.ativo)
        self.assertIsNotNone(self.pc.ativo.get_conta('caixa'))

    def test_get_conta(self):
        self.assertIsNotNone(self.pc.get_conta('caixa'))
        self.assertIsNone(self.pc.get_conta('não existe'))
        self.assertIsNotNone(self.pc.get_conta('contas_a_receber'))

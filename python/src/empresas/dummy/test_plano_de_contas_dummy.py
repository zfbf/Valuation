import unittest

from .plano_de_contas_dummy import PlanoDeContasDummy
#from ..lancamento_contabil import LancamentoContabil


class TestPlanoDeContasDummy(unittest.TestCase):

    def setUp(self):
        self.pc = PlanoDeContasDummy()

    def test_attributes(self):
        self.assertIsNotNone(self.pc.ativo)
        self.assertIsNotNone(self.pc.ativo.get_conta('caixa'))

    def test_get_conta(self):
        self.assertIsNotNone(self.pc.get_conta('caixa'))
        self.assertIsNone(self.pc.get_conta('não existe'))

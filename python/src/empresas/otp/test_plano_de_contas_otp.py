import unittest

from .plano_de_contas_otp import PlanoDeContasOtp
#from ..lancamento_contabil import LancamentoContabil


class TestPlanoDeContasOtp(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.pc = PlanoDeContasOtp()

    def test_attributes(self):
        self.assertIsNotNone(self.pc.ativo)
        self.assertIsNotNone(self.pc.ativo.get_conta('caixa'))

    def test_get_conta(self):
        self.assertIsNotNone(self.pc.get_conta('caixa'))
        self.assertIsNone(self.pc.get_conta('não existe'))
        self.assertIsNotNone(self.pc.get_conta('contas_a_receber'))

    def test_get_contas_disponibilidade(self):
        contas_disponibilidade = self.pc.get_contas_disponibilidade()
        self.assertIsNotNone(contas_disponibilidade)
        self.assertEqual(len(contas_disponibilidade), 1)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('plano_de_contas: {}'.format(self.pc))

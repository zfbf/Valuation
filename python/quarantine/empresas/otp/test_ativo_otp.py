import unittest

from .ativo_otp import AtivoOtp


class TestAtivoOtp(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.ativo = AtivoOtp()

    def test_get_conta(self):
        self.assertIsNotNone(self.ativo.get_conta('nao_circulante'))
        self.assertIsNotNone(self.ativo.get_conta('circulante'))
        self.assertIsNotNone(self.ativo.get_conta('caixa'))

    def test_get_contas_disponibilidades(self):
        contas_disponibilidades = self.ativo.get_contas_disponibilidades()
        self.assertIsNotNone(contas_disponibilidades)
        self.assertEqual(len(contas_disponibilidades), 1)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('plano_de_contas: {}'.format(self.ativo))

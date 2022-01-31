import unittest

from .ativo import AtivoDefault


class TestAtivoDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.ativo = AtivoDefault()
        self.ativo.init_contas()

    def test_get_conta(self):
        self.assertIsNotNone(self.ativo.get_conta('nao_circulante'))
        self.assertIsNotNone(self.ativo.get_conta('circulante'))
        self.assertIsNotNone(self.ativo.circulante.get_conta_caixa())

    def test_get_contas_disponibilidades(self):
        contas_disponibilidades = self.ativo.circulante.get_contas_disponibilidades()
        self.assertIsNotNone(contas_disponibilidades)
        self.assertEqual(len(contas_disponibilidades), 1)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('ativo: {}'.format(self.ativo))

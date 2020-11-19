import unittest
#import pdb

from .ativo_dummy import AtivoDummy


class TestAtivoDummy(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.ativo = AtivoDummy()
        self.ativo.init_contas()

    def test_get_conta(self):
        self.assertIsNotNone(self.ativo.get_conta('nao_circulante'))
        self.assertIsNotNone(self.ativo.get_conta('circulante'))
        self.assertIsNotNone(self.ativo.get_conta('caixa'))
        #pdb.set_trace()
        self.assertIsNotNone(self.ativo.get_conta('contas_a_receber'))

    def test_get_contas_disponibilidades(self):
        contas_disponibilidades = self.ativo.get_contas_disponibilidades()
        self.assertIsNotNone(contas_disponibilidades)
        self.assertEqual(len(contas_disponibilidades), 1)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('plano_de_contas: {}'.format(self.ativo))

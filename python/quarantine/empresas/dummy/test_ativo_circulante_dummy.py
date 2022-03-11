import unittest

from .ativo_circulante_dummy import AtivoCirculanteDummy


class TestAtivoCirculanteDummy(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.ativo_circulante = AtivoCirculanteDummy(parent=None)

    def test_get_conta(self):
        self.assertIsNotNone(self.ativo_circulante.get_conta('caixa'))
        self.assertIsNone(self.ativo_circulante.get_conta('não existe'))

    def test_get_contas_disponibilidades(self):
        contas_disponibilidades = self.ativo_circulante.get_contas_disponibilidades()
        self.assertIsNotNone(contas_disponibilidades)
        self.assertEqual(len(contas_disponibilidades), 1)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('plano_de_contas: {}'.format(self.ativo_circulante))

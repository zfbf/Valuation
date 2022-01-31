import unittest

from .ativo_nao_circulante import AtivoNaoCirculanteDefault


class TestAtivoNaoCirculanteDefault(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.ativo_nao_circulante = AtivoNaoCirculanteDefault(parent=None)
        self.ativo_nao_circulante.init_contas()

    def test_get_conta(self):
        self.assertIsNotNone(self.ativo_nao_circulante.get_conta('realizavel_lp'))
        self.assertIsNone(self.ativo_nao_circulante.get_conta('não existe'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('ativo_nao_circulante: {}'.format(self.ativo_nao_circulante))

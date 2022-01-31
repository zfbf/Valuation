import unittest

from .passivo_nao_circulante import PassivoNaoCirculanteDefault


class TestPassivoNaoCirculanteDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.passivo_nao_circulante = PassivoNaoCirculanteDefault(parent=None)

    def test_get_conta(self):
        self.assertIsNotNone(self.passivo_nao_circulante.get_conta('fornecedores'))
        self.assertIsNone(self.passivo_nao_circulante.get_conta('não existe'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('passivo_nao_circulante: {}'.format(self.passivo_nao_circulante))

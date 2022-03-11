import unittest

from .passivo_nao_circulante import PassivoNaoCirculanteDefault


class TestPassivoNaoCirculanteDefault(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.passivo_nao_circulante = PassivoNaoCirculanteDefault(parent=None)
        self.passivo_nao_circulante.init_contas()

    def test_get_conta(self):
        self.assertIsNotNone(self.passivo_nao_circulante.get_conta('impostos_diferidos'))
        self.assertIsNone(self.passivo_nao_circulante.get_conta('não existe'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('passivo_nao_circulante: {}'.format(self.passivo_nao_circulante))

import unittest

from .passivo_circulante import PassivoCirculanteIFRS


class TestPassivoCirculanteIFRS(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.passivo_circulante = PassivoCirculanteIFRS(parent=None)
        self.passivo_circulante.init_contas()

    def test_get_conta(self):
        self.assertIsNotNone(self.passivo_circulante.get_conta('fornecedores'))
        self.assertIsNone(self.passivo_circulante.get_conta('não existe'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('passivo_circulante: {}'.format(self.passivo_circulante))

import unittest

from .passivo import PassivoDefault


class TestPassivoDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.passivo = PassivoDefault()

    def test_get_conta(self):
        self.assertIsNotNone(self.passivo.get_conta('nao_circulante'))
        self.assertIsNotNone(self.passivo.get_conta('circulante'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('passivo: {}'.format(self.passivo))

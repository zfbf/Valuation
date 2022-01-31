import unittest

from .patrimonio_liquido import PatrimonioLiquidoDefault


class TestPatrimonioLiquidoDefault(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.patrimonio_liquido = PatrimonioLiquidoDefault()

    def test_get_conta(self):
        self.assertIsNotNone(self.patrimonio_liquido.get_conta('capital_social'))
        self.assertIsNone(self.patrimonio_liquido.get_conta('não existe'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('patrimonio_liquido: {}'.format(self.patrimonio_liquido))

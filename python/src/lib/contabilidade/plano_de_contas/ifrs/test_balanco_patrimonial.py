import unittest

from .balanco_patrimonial import BalancoPatrimonialIFRS


class TestBalancoPatrimonialIFRS(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.balanco_patrimonial = BalancoPatrimonialIFRS()

    def test_attributes(self):
        self.assertIsNotNone(self.balanco_patrimonial.ativo)
        self.assertIsNotNone(self.balanco_patrimonial.passivo)
        self.assertIsNotNone(self.balanco_patrimonial.patrimonio_liquido)

    def test_get_conta(self):
        self.assertIsNotNone(self.balanco_patrimonial.ativo.circulante.get_conta_caixa())
        self.assertIsNone(self.balanco_patrimonial.get_conta('não existe'))
        self.assertIsNotNone(self.balanco_patrimonial.get_conta('contas_a_receber'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('balanco_patrimonial: {}'.format(self.balanco_patrimonial))

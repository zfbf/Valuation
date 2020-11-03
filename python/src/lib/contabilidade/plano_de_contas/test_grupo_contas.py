import unittest

from .grupo_contas import GrupoContas
from .conta_devedora import ContaDevedora
from .lancamento_contabil import LancamentoContabil


class DummyGrupoContas(GrupoContas):

    def __init__(self, codigo, nome):
        super().__init__(codigo, nome)

    def get_saldo(self):
        pass

    def set_saldo(self, saldo):
        pass

    def increase_saldo(self, lancamento):
        pass

    def decrease_saldo(self, lancamento):
        pass


class TestGrupoContas(unittest.TestCase):
    #print_to_stdout = True

    def setUp(self):
        self.gc1 = DummyGrupoContas('grupo_1', 'Grupo 1')
        conta_1 = ContaDevedora('conta_1', 'Conta 1')
        conta_1.set_saldo(10.3)
        self.gc1.add_conta(conta_1)
        conta_2 = ContaDevedora('conta_2', 'Conta 2')
        conta_2.set_saldo(5)
        self.gc1.add_conta(conta_2)

    def test_get_conta(self):
        self.assertIsNotNone(self.gc1.get_conta('conta_1'))
        self.assertIsNone(self.gc1.get_conta('conta_a'))

    def test_get_saldo(self):
        #self.assertAlmostEqual(self.gc1.get_saldo(), 15.3)
        #self.assertAlmostEqual(self.gc2.get_saldo(), 45.3)

    #@unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        self.assertTrue(True)
        print('test_to_str')

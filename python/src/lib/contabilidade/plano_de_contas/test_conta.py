import unittest

from .conta import Conta
from .lancamento_contabil import LancamentoContabil


class DummyConta(Conta):
    def __init__(self, codigo, nome, saldo=0):
        super().__init__(codigo, nome)
        self.saldo = saldo

    def get_saldo(self):
        return self.saldo

    def set_saldo(self, saldo):
        self.saldo = saldo

    def increase_saldo(self, lancamento):
        pass

    def decrease_saldo(self, lancamento):
        pass


class TestConta(unittest.TestCase):

    def setUp(self):
        self.dummy = DummyConta('dummy', 'dummy')
        self.dummy.add_debito(LancamentoContabil(10))
        self.dummy.add_debito(LancamentoContabil(10))
        self.dummy.add_credito(LancamentoContabil(10))

    def tearDown(self):
        pass

    def test_codigo(self):
        self.assertEqual(self.dummy.codigo, 'dummy')

    def test_get_conta(self):
        self.assertIsNotNone(self.dummy.get_conta('dummy'))

    def test_get_total_debitos(self):
        self.assertAlmostEqual(self.dummy.get_total_debitos(), 20)

    def test_get_total_creditos(self):
        self.assertAlmostEqual(self.dummy.get_total_creditos(), 10)

    def test_is_saldo_equals(self):
        self.assertTrue(self.dummy.is_saldo_equals(0))
        self.dummy.set_saldo(10)
        self.assertTrue(self.dummy.is_saldo_equals(10))
        self.assertFalse(self.dummy.is_saldo_equals(10.0001))
        self.assertTrue(self.dummy.is_saldo_equals(10.000001))

    def test_is_saldo_credor(self):
        self.assertFalse(self.dummy.is_saldo_credor())

    def test_is_saldo_devedor(self):
        self.assertTrue(self.dummy.is_saldo_devedor())

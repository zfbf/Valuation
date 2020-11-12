import unittest
#import pdb

from .conta import Conta
from .grupo_contas import GrupoContas
from .conta_devedora import ContaDevedora
from ..lancamento_contabil import LancamentoContabil
from ..natureza import Natureza


class DummyConta(Conta):
    def __init__(self, codigo, nome, parent, saldo=0):
        super().__init__(codigo, nome, parent)
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
        self.grupo_a = GrupoContas('grupo_a', 'Grupo A', None)
        grupo_a1 = GrupoContas('grupo_a1', 'Grupo A1', Natureza.DEVEDORA)
        self.grupo_a.add_conta(grupo_a1)
        self.dummy = ContaDevedora('dummy', 'Dummy')
        self.dummy.add_debito(LancamentoContabil(10))
        self.dummy.add_debito(LancamentoContabil(10))
        self.dummy.add_credito(LancamentoContabil(10))
        grupo_a1.add_conta(self.dummy)

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
        self.assertFalse(self.dummy.is_saldo_equals(0))
        self.dummy.set_saldo(10)
        self.assertTrue(self.dummy.is_saldo_equals(10))
        self.assertFalse(self.dummy.is_saldo_equals(10.0001))
        self.assertTrue(self.dummy.is_saldo_equals(10.000001))

    def test_is_saldo_credor(self):
        self.assertFalse(self.dummy.is_saldo_credor())

    def test_is_saldo_devedor(self):
        self.assertTrue(self.dummy.is_saldo_devedor())

    def test_get_codigos_ascendentes(self):
        #pdb.set_trace()
        codigos_ascendentes = self.dummy.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 2)
        self.assertEqual(codigos_ascendentes[0], 'grupo_a1')
        self.assertEqual(codigos_ascendentes[1], 'grupo_a')

    def test_get_grupos_ascendentes(self):
        grupos_ascendentes = self.dummy.get_grupos_ascendentes()
        self.assertEqual(len(grupos_ascendentes), 2)

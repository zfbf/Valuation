import unittest

from .conta_credora import ContaCredora
from ..lancamento_contabil import LancamentoContabil


class TestContaCredora(unittest.TestCase):

    def setUp(self):
        self.fornecedores = ContaCredora('fornecedores', 'Fornecedores')
        self.fornecedores.add_debito(LancamentoContabil(10))
        self.fornecedores.add_credito(LancamentoContabil(10))
        self.fornecedores.add_credito(LancamentoContabil(10))

    def tearDown(self):
        pass

    def test_codigo(self):
        self.assertEqual(self.fornecedores.codigo, 'fornecedores')

    def test_get_conta(self):
        self.assertIsNotNone(self.fornecedores.get_conta('Fornecedores'))

    def test_get_saldo(self):
        self.assertAlmostEqual(self.fornecedores.get_saldo(), 10)

    def test_get_total_debitos(self):
        self.assertAlmostEqual(self.fornecedores.get_total_debitos(), 10)

    def test_get_total_creditos(self):
        self.assertAlmostEqual(self.fornecedores.get_total_creditos(), 20)

    def test_increase_saldo(self):
        self.fornecedores.increase_saldo(LancamentoContabil(10))
        self.assertAlmostEqual(self.fornecedores.get_total_debitos(), 10)
        self.assertAlmostEqual(self.fornecedores.get_total_creditos(), 30)
        self.assertAlmostEqual(self.fornecedores.get_saldo(), 20)

    def test_decrease_saldo(self):
        self.fornecedores.decrease_saldo(LancamentoContabil(3))
        self.assertAlmostEqual(self.fornecedores.get_total_debitos(), 13)
        self.assertAlmostEqual(self.fornecedores.get_total_creditos(), 20)
        self.assertAlmostEqual(self.fornecedores.get_saldo(), 7)

    # Saldo informado positivo e menor que atual
    def test_set_saldo_1(self):
        self.fornecedores.set_saldo(5)
        self.assertAlmostEqual(self.fornecedores.get_total_debitos(), 15)
        self.assertAlmostEqual(self.fornecedores.get_total_creditos(), 20)
        self.assertAlmostEqual(self.fornecedores.get_saldo(), 5)

    # Saldo informado negativo
    def test_set_saldo_2(self):
        self.fornecedores.set_saldo(-5)
        self.assertAlmostEqual(self.fornecedores.get_total_debitos(), 25)
        self.assertAlmostEqual(self.fornecedores.get_total_creditos(), 20)
        self.assertAlmostEqual(self.fornecedores.get_saldo(), -5)

    # Aumento do número de lançamentos e retorno ao saldo inicial
    def test_set_saldo_3(self):
        self.fornecedores.add_debito(LancamentoContabil(20))
        self.assertAlmostEqual(self.fornecedores.get_total_debitos(), 30)
        self.assertAlmostEqual(self.fornecedores.get_total_creditos(), 20)
        self.assertAlmostEqual(self.fornecedores.get_saldo(), -10)
        self.fornecedores.set_saldo(10)
        self.assertAlmostEqual(self.fornecedores.get_total_debitos(), 30)
        self.assertAlmostEqual(self.fornecedores.get_total_creditos(), 40)
        self.assertAlmostEqual(self.fornecedores.get_saldo(), 10)

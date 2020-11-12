import unittest

from .conta_devedora import ContaDevedora
from ..lancamento_contabil import LancamentoContabil


class TestContaDevedora(unittest.TestCase):

    def setUp(self):
        self.caixa = ContaDevedora('caixa', 'caixa')
        self.caixa.add_debito(LancamentoContabil(10))
        self.caixa.add_debito(LancamentoContabil(10))
        self.caixa.add_credito(LancamentoContabil(10))

    def tearDown(self):
        pass

    def test_codigo(self):
        self.assertEqual(self.caixa.codigo, 'caixa')

    def test_get_conta(self):
        self.assertIsNotNone(self.caixa.get_conta('Caixa'))

    def test_get_saldo(self):
        self.assertAlmostEqual(self.caixa.get_saldo(), 10)

    def test_get_total_debitos(self):
        self.assertAlmostEqual(self.caixa.get_total_debitos(), 20)

    def test_get_total_creditos(self):
        self.assertAlmostEqual(self.caixa.get_total_creditos(), 10)

    def test_increase_saldo(self):
        self.caixa.increase_saldo(LancamentoContabil(10))
        self.assertAlmostEqual(self.caixa.get_total_debitos(), 30)
        self.assertAlmostEqual(self.caixa.get_total_creditos(), 10)
        self.assertAlmostEqual(self.caixa.get_saldo(), 20)

    def test_decrease_saldo(self):
        self.caixa.decrease_saldo(LancamentoContabil(3))
        self.assertAlmostEqual(self.caixa.get_total_debitos(), 20)
        self.assertAlmostEqual(self.caixa.get_total_creditos(), 13)
        self.assertAlmostEqual(self.caixa.get_saldo(), 7)

    # Saldo informado positivo e menor que atual
    def test_set_saldo_1(self):
        self.caixa.set_saldo(5)
        self.assertAlmostEqual(self.caixa.get_total_debitos(), 20)
        self.assertAlmostEqual(self.caixa.get_total_creditos(), 15)
        self.assertAlmostEqual(self.caixa.get_saldo(), 5)

    # Saldo informado negativo
    def test_set_saldo_2(self):
        self.caixa.set_saldo(-5)
        self.assertAlmostEqual(self.caixa.get_total_debitos(), 20)
        self.assertAlmostEqual(self.caixa.get_total_creditos(), 25)
        self.assertAlmostEqual(self.caixa.get_saldo(), -5)

    # Aumento do número de lançamentos e retorno ao saldo inicial
    def test_set_saldo_3(self):
        self.caixa.add_credito(LancamentoContabil(20))
        self.assertAlmostEqual(self.caixa.get_total_debitos(), 20)
        self.assertAlmostEqual(self.caixa.get_total_creditos(), 30)
        self.assertAlmostEqual(self.caixa.get_saldo(), -10)
        self.caixa.set_saldo(10)
        self.assertAlmostEqual(self.caixa.get_total_debitos(), 40)
        self.assertAlmostEqual(self.caixa.get_total_creditos(), 30)
        self.assertAlmostEqual(self.caixa.get_saldo(), 10)

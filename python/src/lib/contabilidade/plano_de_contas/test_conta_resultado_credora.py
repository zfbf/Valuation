import unittest

from .conta_credora import ContaCredora
from .conta_devedora import ContaDevedora
from .conta_resultado_credora import ContaResultadoCredora
from ..lancamento_contabil import LancamentoContabil


class TestContaResultadoCredora(unittest.TestCase):

    def setUp(self):
        self.lucro_bruto = ContaResultadoCredora('lucro_bruto', 'Lucro Bruto')

        receita_liquida_operacional = ContaCredora(
                'receita_liquida_operacional',
                'Receita Líquida Operacional')
        receita_liquida_operacional.add_credito(LancamentoContabil(1500))

        self.lucro_bruto.add_conta(receita_liquida_operacional)

    def tearDown(self):
        pass

    def test_codigo(self):
        self.assertEqual(self.lucro_bruto.codigo, 'lucro_bruto')

    def test_get_conta(self):
        self.assertIsNotNone(self.lucro_bruto.get_conta(
                'receita_liquida_operacional'))

    def test_get_saldo_1(self):
        self.assertAlmostEqual(self.lucro_bruto.get_saldo(), 1500)

    def test_get_saldo_2(self):
        custo_produtos_vendidos = ContaDevedora(
                'custo_produtos_vendidos',
                'Custo Produtos Vendidos')
        custo_produtos_vendidos.add_debito(LancamentoContabil(500))
        self.lucro_bruto.add_conta(custo_produtos_vendidos)
        self.assertAlmostEqual(self.lucro_bruto.get_saldo(), 1000)

    def test_get_total_debitos(self):
        self.assertAlmostEqual(self.lucro_bruto.get_total_debitos(), 0)

    def test_get_total_creditos(self):
        rlo = self.lucro_bruto.get_conta('receita_liquida_operacional')
        self.assertAlmostEqual(rlo.get_total_creditos(), 1500)

    def test_increase_saldo(self):
        rlo = self.lucro_bruto.get_conta('receita_liquida_operacional')
        rlo.increase_saldo(LancamentoContabil(10))
        self.assertAlmostEqual(rlo.get_total_debitos(), 0)
        self.assertAlmostEqual(rlo.get_total_creditos(), 1510)
        self.assertAlmostEqual(rlo.get_saldo(), 1510)

    def test_decrease_saldo(self):
        rlo = self.lucro_bruto.get_conta('receita_liquida_operacional')
        rlo.decrease_saldo(LancamentoContabil(10))
        self.assertAlmostEqual(rlo.get_total_debitos(), 10)
        self.assertAlmostEqual(rlo.get_total_creditos(), 1500)
        self.assertAlmostEqual(rlo.get_saldo(), 1490)

    # Saldo informado positivo e menor que atual
    def test_set_saldo_1(self):
        rlo = self.lucro_bruto.get_conta('receita_liquida_operacional')
        rlo.set_saldo(1000)
        self.assertAlmostEqual(rlo.get_total_debitos(), 500)
        self.assertAlmostEqual(rlo.get_total_creditos(), 1500)
        self.assertAlmostEqual(rlo.get_saldo(), 1000)

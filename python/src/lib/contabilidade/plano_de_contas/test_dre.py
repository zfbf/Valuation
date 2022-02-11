import unittest

from .grupo_contas import GrupoContas
from .conta_devedora import ContaDevedora
from .conta_credora import ContaCredora
from ..lancamento_contabil import LancamentoContabil
from ..natureza import Natureza
from .dre import DRE


class TestDRE(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.dre = DRE()
        self.dre.init_contas()

    def test_lucro_bruto(self):
        self.dre.receita_liquida_operacional.add_credito(
                LancamentoContabil(1500))
        self.dre.custo_produtos_vendidos.add_debito(
                LancamentoContabil(500))
        self.dre.lucro_bruto.valor_verificacao = 1000
        saldo_lucro_bruto = self.dre.lucro_bruto.get_saldo()
        self.assertAlmostEqual(saldo_lucro_bruto, 1000)
        self.assertTrue(self.dre.lucro_bruto.verificar_saldo())

    def test_despesas_operacionais(self):
        self.dre.receita_liquida_operacional.add_credito(
                LancamentoContabil(1500))
        self.dre.custo_produtos_vendidos.add_debito(
                LancamentoContabil(500))
        despesas_com_vendas = self.dre.despesas_operacionais.get_conta('despesas_com_vendas')
        despesas_com_vendas.add_debito(LancamentoContabil(50))
        self.dre.despesas_operacionais.valor_verificacao = 50
        self.assertTrue(self.dre.despesas_operacionais.verificar_saldo())

    def test_lair(self):
        self.dre.receita_liquida_operacional.add_credito(
                LancamentoContabil(1500))
        self.dre.custo_produtos_vendidos.add_debito(
                LancamentoContabil(500))
        despesas_com_vendas = self.dre.despesas_operacionais.get_conta('despesas_com_vendas')
        despesas_com_vendas.add_debito(LancamentoContabil(50))
        self.dre.despesas_operacionais.valor_verificacao = 50
        self.assertTrue(self.dre.despesas_operacionais.verificar_saldo())
        self.dre.lair.valor_verificacao = 950
        #self.assertTrue(self.dre.lair.verificar_saldo())

    @unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        self.test_lair()
        print(self.dre)

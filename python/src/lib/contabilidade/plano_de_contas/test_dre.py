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

    def test_lajir(self):
        self.dre.receita_liquida_operacional.add_credito(
                LancamentoContabil(1500))
        self.dre.custo_produtos_vendidos.add_debito(
                LancamentoContabil(500))
        despesas_com_vendas = self.dre.despesas_operacionais.get_conta('despesas_com_vendas')
        despesas_com_vendas.add_debito(LancamentoContabil(50))
        self.dre.despesas_operacionais.valor_verificacao = 50
        self.assertTrue(self.dre.despesas_operacionais.verificar_saldo())
        self.dre.lajir.valor_verificacao = 950
        self.assertTrue(self.dre.lajir.verificar_saldo())

    def test_resultado_financeiro(self):
        self.dre.resultado_financeiro.valor_verificacao = -50
        receitas_financeiras = self.dre.resultado_financeiro.get_conta(
                'receitas_financeiras')
        receitas_financeiras.add_credito(LancamentoContabil(100))
        despesas_financeiras = self.dre.resultado_financeiro.get_conta(
                'despesas_financeiras')
        despesas_financeiras.add_debito(LancamentoContabil(150))
        self.assertTrue(self.dre.resultado_financeiro.verificar_saldo())

    def test_lair(self):
        self.dre.receita_liquida_operacional.add_credito(
                LancamentoContabil(1500))
        self.dre.custo_produtos_vendidos.add_debito(
                LancamentoContabil(500))
        self.dre.despesas_operacionais.valor_verificacao = 50
        despesas_com_vendas = self.dre.despesas_operacionais.get_conta('despesas_com_vendas')
        despesas_com_vendas.add_debito(LancamentoContabil(50))
        self.dre.resultado_financeiro.valor_verificacao = -50
        receitas_financeiras = self.dre.resultado_financeiro.get_conta(
                'receitas_financeiras')
        receitas_financeiras.add_credito(LancamentoContabil(100))
        despesas_financeiras = self.dre.resultado_financeiro.get_conta(
                'despesas_financeiras')
        despesas_financeiras.add_debito(LancamentoContabil(150))
        self.dre.lair.valor_verificacao = 900
        self.assertTrue(self.dre.lair.verificar_saldo())

    @unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        self.test_lair()
        print(self.dre)

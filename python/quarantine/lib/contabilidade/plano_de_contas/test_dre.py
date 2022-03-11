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

    def set_values(self):
        self.dre.receita_liquida_operacional.add_credito(
                LancamentoContabil(1500))
        self.dre.custo_produtos_vendidos.add_debito(
                LancamentoContabil(500))
        self.dre.lucro_bruto.valor_verificacao = 1000
        self.dre.despesas_operacionais.valor_verificacao = 50
        despesas_com_vendas = self.dre.despesas_operacionais.get_conta('despesas_com_vendas')
        despesas_com_vendas.add_debito(LancamentoContabil(50))
        self.dre.lajir.valor_verificacao = 950
        self.dre.resultado_financeiro.valor_verificacao = -50
        receitas_financeiras = self.dre.resultado_financeiro.get_conta(
                'receitas_financeiras')
        receitas_financeiras.add_credito(LancamentoContabil(100))
        despesas_financeiras = self.dre.resultado_financeiro.get_conta(
                'despesas_financeiras')
        despesas_financeiras.add_debito(LancamentoContabil(150))
        self.dre.lair.valor_verificacao = 900
        self.dre.ircs.valor_verificacao = 200
        provisao_ir = self.dre.ircs.get_conta('provisao_ir')
        provisao_ir.add_debito(LancamentoContabil(120))
        ir_diferido = self.dre.ircs.get_conta('ir_diferido')
        ir_diferido.add_debito(LancamentoContabil(80))
        self.dre.lucro_oper_continuadas.valor_verificacao = 700
        self.dre.operacoes_descontinuadas.add_credito(LancamentoContabil(10))
        self.dre.lucro_consolidado.valor_verificacao = 710
        self.dre.participacao_minoritaria.add_debito(LancamentoContabil(60))
        self.dre.lucro_liquido.valor_verificacao = 650

    def test_lucro_bruto(self):
        self.set_values()
        saldo_lucro_bruto = self.dre.lucro_bruto.get_saldo()
        self.assertAlmostEqual(saldo_lucro_bruto, 1000)
        self.assertTrue(self.dre.lucro_bruto.verificar_saldo())

    def test_despesas_operacionais(self):
        self.set_values()
        self.assertTrue(self.dre.despesas_operacionais.verificar_saldo())

    def test_lajir(self):
        self.set_values()
        self.assertTrue(self.dre.lajir.verificar_saldo())

    def test_resultado_financeiro(self):
        self.set_values()
        self.assertTrue(self.dre.resultado_financeiro.verificar_saldo())

    def test_lair(self):
        self.set_values()
        self.assertTrue(self.dre.lair.verificar_saldo())

    def test_ircs(self):
        self.set_values()
        self.assertTrue(self.dre.ircs.verificar_saldo())

    def test_lucro_oper_continuadas(self):
        self.set_values()
        self.assertTrue(self.dre.lucro_oper_continuadas.verificar_saldo())

    def test_lucro_consolidado(self):
        self.set_values()
        self.assertTrue(self.dre.lucro_consolidado.verificar_saldo())

    def test_participacao_minoritaria(self):
        self.set_values()
        self.assertAlmostEqual(self.dre.participacao_minoritaria.get_saldo(), 60)

    def test_lucro_liquido(self):
        self.set_values()
        self.assertTrue(self.dre.lucro_liquido.verificar_saldo())

    @unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        self.set_values()
        print(self.dre)

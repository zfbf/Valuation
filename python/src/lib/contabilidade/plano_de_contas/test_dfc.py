import unittest

from .grupo_contas import GrupoContas
from .conta_devedora import ContaDevedora
from .conta_credora import ContaCredora
from ..lancamento_contabil import LancamentoContabil
from ..natureza import Natureza
from .dfc import DFC


class TestDFC(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.dfc = DFC()

    def set_values(self):
        self.dfc.operacional.valor_verificacao = 1000

        operacao = self.dfc.operacional.get_conta('operacao')
        operacao.valor_verificacao = 600

        lucro_liquido = operacao.get_conta('lucro_liquido')
        lucro_liquido.add_credito(LancamentoContabil(600))

        variacao_ativos_passivos = self.dfc.operacional.get_conta(
                'variacao_ativos_passivos')
        variacao_ativos_passivos.valor_verificacao = 300

        variacao_duplicatas_a_receber = variacao_ativos_passivos.get_conta(
                'variacao_duplicatas_a_receber')
        variacao_duplicatas_a_receber.add_credito(LancamentoContabil(200))

        variacao_estoques = variacao_ativos_passivos.get_conta(
                'variacao_estoques')
        variacao_estoques.add_credito(LancamentoContabil(100))

        outros_operacional = self.dfc.operacional.get_conta('outros')
        outros_operacional.add_credito(LancamentoContabil(100))

        investimentos = self.dfc.investimentos
        investimentos.valor_verificacao = 200

        compra_liquida_ativ_perm = investimentos.get_conta(
                'compra_liquida_ativos_permanentes')
        compra_liquida_ativ_perm.valor_verificacao = 200

        compra_investimentos_permanentes = compra_liquida_ativ_perm.get_conta(
                'compra_investimentos_permanentes')
        compra_investimentos_permanentes.add_credito(LancamentoContabil(180))

        compra_ativos_fixos = compra_liquida_ativ_perm.get_conta(
                'compra_ativos_fixos')
        compra_ativos_fixos.add_credito(LancamentoContabil(60))

        venda_ativos_permanentes = compra_liquida_ativ_perm.get_conta(
                'venda_ativos_permanentes')
        venda_ativos_permanentes.add_debito(LancamentoContabil(40))

        financiamentos = self.dfc.financiamentos
        financiamentos.valor_verificacao = 300

        financiamentos_liquido = financiamentos.get_conta(
                'financiamentos_liquido')
        financiamentos_liquido.valor_verificacao = 300

        financiamentos_obtidos = financiamentos_liquido.get_conta(
                'financiamentos_obtidos')
        financiamentos_obtidos.add_credito(LancamentoContabil(1000))

        financiamentos_pagos = financiamentos_liquido.get_conta(
                'financiamentos_pagos')
        financiamentos_pagos.add_debito(LancamentoContabil(700))

    def test_operacao(self):
        self.set_values()
        operacao = self.dfc.operacional.get_conta('operacao')
        self.assertTrue(operacao.verificar_saldo())

    def test_variacao_ativos_passivos(self):
        self.set_values()
        variacao_ativos_passivos = self.dfc.operacional.get_conta(
                'variacao_ativos_passivos')
        self.assertTrue(variacao_ativos_passivos.verificar_saldo())

    def test_operacional(self):
        self.set_values()
        self.assertTrue(self.dfc.operacional.verificar_saldo())

    def test_investimentos(self):
        self.set_values()
        self.assertTrue(self.dfc.investimentos.verificar_saldo())

    def test_financiamentos(self):
        self.set_values()
        self.assertTrue(self.dfc.financiamentos.verificar_saldo())

    @unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        self.set_values()
        print(self.dfc)

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
        print('receita_liquida_operacional: {}'.format(
              self.dre.receita_liquida_operacional))

        self.dre.custo_produtos_vendidos.add_debito(
                LancamentoContabil(500))
        print('custo_produtos_vendidos: {}'.format(
              self.dre.custo_produtos_vendidos))
              
        self.dre.lucro_bruto.valor_verificacao = 1000
        print('lucro_bruto: {}'.format(
              self.dre.lucro_bruto))
        saldo_lucro_bruto = self.dre.lucro_bruto.get_saldo()
        print('saldo_lucro_bruto: {}'.format(saldo_lucro_bruto))
        self.assertAlmostEqual(saldo_lucro_bruto, 1000)
        self.assertTrue(self.dre.lucro_bruto.verificar_saldo())

    def test_get_saldo_1(self):
        self.assertAlmostEqual(self.gc1.get_saldo(), 15.3)
        self.assertAlmostEqual(self.gc2.get_saldo(), 45.3)

    def test_get_saldo_2(self):
        gc24 = GrupoContas('grupo_2.4', 'Grupo 2.4', Natureza.DEVEDORA)
        conta_241 = ContaDevedora('conta_1', 'Conta 1')
        conta_241.set_saldo(4.7)
        gc24.add_conta(conta_241)
        self.gc2.add_conta(gc24)
        gc24.valor_verificacao = 4.7
        self.assertTrue(gc24.verificar_saldo())
        self.gc2.valor_verificacao = 50
        self.assertTrue(self.gc2.verificar_saldo())

        gc242 = GrupoContas('grupo_2.4.2', 'Grupo 2.4.2', Natureza.DEVEDORA)
        conta_2421 = ContaDevedora('conta_1', 'Conta 1')
        conta_2421.set_saldo(10)
        gc242.add_conta(conta_2421)
        gc242.valor_verificacao = 10
        self.assertTrue(gc242.verificar_saldo())

        conta_2422 = ContaCredora('conta_2', 'Conta 2')
        conta_2422.set_saldo(5)
        gc242.add_conta(conta_2422)
        gc242.valor_verificacao = 5
        self.assertTrue(gc242.verificar_saldo())

        gc24.add_conta(gc242)
        self.gc2.valor_verificacao = 55
        self.assertTrue(self.gc2.verificar_saldo())

    def test_verificar_saldo(self):
        self.assertFalse(self.gc1.verificar_saldo())
        self.assertTrue(self.gc2.verificar_saldo())

    def test_get_codigos_ascendentes(self):
        codigos_ascendentes = self.gc1.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 0)

        codigos_ascendentes = self.gc2.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 0)

        conta_23 = self.gc2.get_conta('conta_3')
        codigos_ascendentes = conta_23.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 1)
        self.assertEqual(codigos_ascendentes[0], 'grupo_2')

        conta_11 = self.gc1.get_conta('conta_1')
        codigos_ascendentes = conta_11.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 1)
        self.assertEqual(codigos_ascendentes[0], 'grupo_1')

    def test_get_grupos_ascendentes(self):
        grupos_ascendentes = self.gc1.get_grupos_ascendentes()
        self.assertEqual(len(grupos_ascendentes), 0)

    @unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        print(self.gc1)
        print(self.gc2)

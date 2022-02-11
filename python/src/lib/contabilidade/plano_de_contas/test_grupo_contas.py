import unittest

from .grupo_contas import GrupoContas
from .conta_devedora import ContaDevedora
from .conta_credora import ContaCredora
from ..lancamento_contabil import LancamentoContabil
from ..natureza import Natureza


class TestGrupoContas(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.gc1 = GrupoContas('grupo_1', 'Grupo 1', Natureza.DEVEDORA)
        self.gc1.valor_verificacao = 15.3
        conta_11 = ContaDevedora('conta_1', 'Conta 1')
        conta_11.set_saldo(10.3)
        self.gc1.add_conta(conta_11)
        conta_12 = ContaDevedora('conta_2', 'Conta 2')
        conta_12.set_saldo(5)
        self.gc1.add_conta(conta_12)

        self.gc2 = GrupoContas('grupo_2', 'Grupo 2', Natureza.DEVEDORA)
        conta_21 = ContaDevedora('conta_1', 'Conta 1')
        conta_21.set_saldo(10.3)
        self.gc2.add_conta(conta_21)
        conta_22 = ContaDevedora('conta_2', 'Conta 2')
        conta_22.set_saldo(5)
        self.gc2.add_conta(conta_22)
        conta_23 = ContaDevedora('conta_3', 'Conta 3')
        conta_23.set_saldo(30)
        self.gc2.add_conta(conta_23)
        self.gc2.valor_verificacao = 45.3

    def test_get_conta(self):
        self.assertIsNotNone(self.gc1.get_conta('conta_1'))
        self.assertIsNone(self.gc1.get_conta('conta_a'))

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
        self.assertTrue(self.gc1.verificar_saldo())
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

    def test_get_linha_ascendente(self):
        linha_ascendente = self.gc1.get_linha_ascendente()
        self.assertEqual(len(linha_ascendente), 0)

    def test_get_total_creditos(self):
        total_creditos = self.gc1.get_total_creditos()
        print('total_creditos: {}'.format(total_creditos))
        print('self.gc1: {}'.format(self.gc1))
        print('self.gc1 - conta_1: {}'.format(self.gc1.get_conta('conta_1')))
        print('self.gc1 - conta_2: {}'.format(self.gc1.get_conta('conta_2')))
        self.assertEqual(total_creditos, 0)

    def test_get_total_debitos(self):
        print('\nDentro de test_get_total_debitos')
        total_debitos = self.gc1.get_total_debitos()
        print('total_debitos: {}'.format(total_debitos))
        print('self.gc1: {}'.format(self.gc1))
        print('self.gc1 - conta_1: {}'.format(self.gc1.get_conta('conta_1')))
        print('self.gc1 - conta_2: {}'.format(self.gc1.get_conta('conta_2')))
        self.assertEqual(total_debitos, 15.3)

    @unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        print(self.gc1)
        print(self.gc2)

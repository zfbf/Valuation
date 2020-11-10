import unittest

from .grupo_contas import GrupoContas
from .conta_devedora import ContaDevedora
from ..lancamento_contabil import LancamentoContabil


class TestGrupoContas(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.gc1 = GrupoContas('grupo_1', 'Grupo 1')
        conta_g11 = ContaDevedora('conta_1', 'Conta 1')
        conta_g11.set_saldo(10.3)
        self.gc1.add_conta(conta_g11)
        conta_g12 = ContaDevedora('conta_2', 'Conta 2')
        conta_g12.set_saldo(5)
        self.gc1.add_conta(conta_g12)

        self.gc2 = GrupoContas('grupo_2', 'Grupo 2')
        conta_g21 = ContaDevedora('conta_1', 'Conta 1')
        conta_g21.set_saldo(10.3)
        self.gc2.add_conta(conta_g21)
        conta_g22 = ContaDevedora('conta_2', 'Conta 2')
        conta_g22.set_saldo(5)
        self.gc2.add_conta(conta_g22)
        conta_g23 = ContaDevedora('conta_3', 'Conta 3')
        conta_g23.set_saldo(30)
        self.gc2.add_conta(conta_g23)
        self.gc2.valor_verificacao = 45.3

    def test_get_conta(self):
        self.assertIsNotNone(self.gc1.get_conta('conta_1'))
        self.assertIsNone(self.gc1.get_conta('conta_a'))

    def test_get_saldo(self):
        self.assertAlmostEqual(self.gc1.get_saldo(), 15.3)
        self.assertAlmostEqual(self.gc2.get_saldo(), 45.3)

    def test_verificar_saldo(self):
        self.assertFalse(self.gc1.verificar_saldo())
        self.assertTrue(self.gc2.verificar_saldo())

    def test_get_codigos_ascendentes(self):
        codigos_ascendentes = self.gc1.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 0)

        codigos_ascendentes = self.gc2.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 0)

        conta_g23 = self.gc2.get_conta('conta_3')
        codigos_ascendentes = conta_g23.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 1)
        self.assertEqual(codigos_ascendentes[0], 'grupo_2')

        conta_g11 = self.gc1.get_conta('conta_1')
        codigos_ascendentes = conta_g11.get_codigos_ascendentes()
        self.assertEqual(len(codigos_ascendentes), 1)
        self.assertEqual(codigos_ascendentes[0], 'grupo_1')

    def test_get_grupos_ascendentes(self):
        grupos_ascendentes = self.gc1.get_grupos_ascendentes()
        self.assertEqual(len(grupos_ascendentes), 0)

    @unittest.skipUnless(print_to_stdout, 'making_clear_tests')
    def test_to_str(self):
        print(self.gc1)
        print(self.gc2)

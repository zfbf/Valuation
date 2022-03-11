import unittest

from .ativo_circulante import AtivoCirculanteDefault


class TestAtivoCirculanteDefault(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.ativo_circulante = AtivoCirculanteDefault(parent=None)
        self.ativo_circulante.init_conta_caixa()
        self.ativo_circulante.init_contas()

    def test_get_conta_caixa(self):
        self.assertIsNotNone(self.ativo_circulante.get_conta_caixa())

    def test_get_conta(self):
        contas = ('caixa_e_equivalentes',
                  'aplicacoes_financeiras',
                  'contas_a_receber',
                  'estoques',
                  'ativos_biologicos',
                  'impostos_a_recuperar',
                  'despesas_antecipadas',
                  'outros')

        for conta in contas:
            self.assertIsNotNone(self.ativo_circulante.get_conta(conta))

        self.assertIsNone(self.ativo_circulante.get_conta('não existe'))

    def test_get_contas_disponibilidades(self):
        contas_disponibilidades = self.ativo_circulante.get_contas_disponibilidades()
        self.assertIsNotNone(contas_disponibilidades)
        self.assertEqual(len(contas_disponibilidades), 1)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('ativo_circulante: {}'.format(self.ativo_circulante))

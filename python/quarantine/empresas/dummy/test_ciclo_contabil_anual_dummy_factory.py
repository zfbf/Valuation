import unittest
#import pdb

from .ciclo_contabil_anual_dummy_factory import CicloContabilAnualDummyFactory


class TestCicloContabilAnualDummyFactory(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.otp_factory = CicloContabilAnualDummyFactory()

    def test_execute(self):
        #pdb.set_trace()
        ciclo_contabil_anual = self.otp_factory.execute(ano=2019)
        plano_de_contas = ciclo_contabil_anual.plano_de_contas
        self.assertIsNotNone(plano_de_contas)
        self.assertEqual(ciclo_contabil_anual.ano, 2019)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        ciclo_contabil_anual = self.otp_factory.execute(ano=2019)
        print('ciclo_contabil_anual: {}'.format(ciclo_contabil_anual))

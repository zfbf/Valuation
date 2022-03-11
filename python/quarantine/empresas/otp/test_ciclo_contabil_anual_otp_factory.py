import unittest
#import pdb

from .ciclo_contabil_anual_otp_factory import CicloContabilAnualOtpFactory


class TestCicloContabilAnualOtpFactory(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.otp_factory = CicloContabilAnualOtpFactory()

    def test_execute(self):
        #pdb.set_trace()
        ciclo_contabil_anual = self.otp_factory.execute(ano=2017)
        plano_de_contas = ciclo_contabil_anual.plano_de_contas
        self.assertIsNotNone(plano_de_contas)
        self.assertEqual(ciclo_contabil_anual.ano, 2017)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        ciclo_contabil_anual = self.otp_factory.execute(ano=2017)
        print('ciclo_contabil_anual: {}'.format(ciclo_contabil_anual))

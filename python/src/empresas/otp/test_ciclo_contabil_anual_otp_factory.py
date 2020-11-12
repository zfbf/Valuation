import unittest
#import pdb

from .ciclo_contabil_anual_otp_factory import CicloContabilAnualOtpFactory


class TestCicloContabilAnualOtpFactory(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.otp_factory = CicloContabilAnualOtpFactory()

    def test_execute(self):
        #pdb.set_trace()
        plano_de_contas = self.otp_factory.execute()
        self.assertIsNotNone(plano_de_contas)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        plano_de_contas = self.otp_factory.execute()
        print('plano_de_contas: {}'.format(plano_de_contas))

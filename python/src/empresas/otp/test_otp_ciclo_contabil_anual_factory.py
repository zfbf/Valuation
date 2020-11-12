import unittest

from .otp_ciclo_contabil_anual_factory import OtpCicloContabilAnualFactory


class TestOtpCicloContabilAnualFactory(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        self.otp_factory = OtpCicloContabilAnualFactory()

    def test_execute(self):
        plano_de_contas = self.otp_factory.execute()
        self.assertIsNotNone(plano_de_contas)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        plano_de_contas = self.otp_factory.execute()
        print('plano_de_contas: {}'.format(plano_de_contas))

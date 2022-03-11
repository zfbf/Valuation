import unittest

from .otp import Otp


class TestOtp(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.otp = Otp()
        self.otp.init_ciclos_contabeis_anuais(2016, 2019)

    def test_get_ciclos_contabeis_anuais(self):
        ciclos_contabeis_anuais = self.otp.get_ciclos_contabeis_anuais()
        self.assertIsNotNone(ciclos_contabeis_anuais)
        self.assertEqual(len(ciclos_contabeis_anuais), 4)
        self.assertIsNotNone(ciclos_contabeis_anuais.get('2017'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print(self.otp)

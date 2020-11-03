import unittest

from .otp_factory import OtpFactory


class TestOtpFactory(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.otp_factory = OtpFactory()

    def test_execute(self):
        self.otp_factory.execute()

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print(self.otp_factory)

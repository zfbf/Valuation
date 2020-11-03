import unittest

from .dummy import Dummy


class TestDummy(unittest.TestCase):
    print_to_stdout = False

    def setUp(self):
        self.dummy = Dummy()
        self.dummy.init_ciclos_contabeis_anuais(2017, 2019)

    def test_get_ciclos_contabeis_anuais(self):
        ciclos_contabeis_anuais = self.dummy.get_ciclos_contabeis_anuais()
        self.assertIsNotNone(ciclos_contabeis_anuais)
        self.assertEqual(len(ciclos_contabeis_anuais), 3)
        self.assertIsNotNone(ciclos_contabeis_anuais.get('2017'))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print(self.dummy)

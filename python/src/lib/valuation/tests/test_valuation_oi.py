import unittest

from .fixture_test_valuation_oi import FixtureValuationOi2009T12021T3


class TestValuationOi(FixtureValuationOi2009T12021T3):
    print_to_stdout = True

    def setUp(self):
        self.valuation = TestValuationOi.valuation

    def tearDown(self):
        self.valuation = None

    def test_get_empresa(self):
        self.assertIsNotNone(self.valuation.empresa)

    def test_get_periodos(self):
        self.assertIsNotNone(self.valuation.get_periodos())
        self.assertEqual(len(self.valuation.get_periodos()), 51)

    def test_get_periodo(self):
        identificador = '2020T4'
        self.assertIsNotNone(self.valuation.get_periodo(identificador))

    def test_get_indices_liquidez(self):
        ano_inicial = 2010
        trimestre_inicial = 1
        ano_final = 2021
        trimestre_final = 3
        indices_liquidez = self.valuation.get_indices_liquidez(ano_inicial,
                trimestre_inicial, ano_final, trimestre_final)
        self.assertIsNotNone(indices_liquidez)

        if TestValuationOi.print_to_stdout:
            print('test_get_indices_liquidez')
            print('indices_liquidez:\n{}'.format(indices_liquidez))

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nvaluation: {}'.format(self.valuation))

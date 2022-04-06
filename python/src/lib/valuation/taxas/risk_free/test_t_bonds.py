import unittest

from .t_bonds import TBonds


class TestTBonds(unittest.TestCase):
    print_to_stdout = True

    def setUp(self):
        serie_historica = None
        self.tbonds = TBonds(serie_historica)

    def test_get_taxa(self):
        taxa = self.tbonds.get_taxa()
        self.assertIsNotNone(taxa)
        self.assertTrue(taxa > 0)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\ntbonds: {}'.format(self.tbonds))

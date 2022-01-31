import unittest

from .razonete import Razonete
from ..contabilidade.lancamento_contabil import LancamentoContabil


class TestRazonete(unittest.TestCase):

    def setUp(self):
        self.razonete = Razonete()
        self.razonete.add_debito(LancamentoContabil(10))
        self.razonete.add_debito(LancamentoContabil(10))
        self.razonete.add_credito(LancamentoContabil(20))

    def test_get_total_debitos(self):
        self.assertAlmostEqual(self.razonete.get_total_debitos(), 20)
        self.razonete.add_debito(LancamentoContabil(15))
        self.assertAlmostEqual(self.razonete.get_total_debitos(), 35)
        razonete2 = Razonete()
        self.assertAlmostEqual(razonete2.get_total_debitos(), 0)

    def test_get_total_creditos(self):
        self.assertAlmostEqual(self.razonete.get_total_creditos(), 20)
        self.razonete.add_credito(LancamentoContabil(10))
        self.assertAlmostEqual(self.razonete.get_total_creditos(), 30)
        self.razonete.add_credito(LancamentoContabil(10))
        self.assertAlmostEqual(self.razonete.get_total_creditos(), 40)

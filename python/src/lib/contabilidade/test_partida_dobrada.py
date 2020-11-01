import unittest

from .partida_dobrada import PartidaDobrada
from ..contabilidade.lancamento_contabil import LancamentoContabil


class TestPartidaDobrada(unittest.TestCase):

    def setUp(self):
        ld1 = LancamentoContabil(10)
        ld2 = LancamentoContabil(10)
        lc1 = LancamentoContabil(20)
        self.pd1 = PartidaDobrada(ano=2020, mes=10, dia=18)
        self.pd1.add_debito(ld1)
        self.pd1.add_debito(ld2)
        self.pd1.add_credito(lc1)

    def tearDown(self):
        pass

    def test_get_data(self):
        self.assertIsNotNone(self.pd1.get_data())
        self.pd1.mes = None
        self.assertIsNone(self.pd1.get_data())

    def test_is_valid(self):
        self.assertTrue(self.pd1.is_valid())

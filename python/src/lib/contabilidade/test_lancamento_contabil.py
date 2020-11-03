import unittest

from .lancamento_contabil import LancamentoContabil


class TestRazonete(unittest.TestCase):

    def test_get_data(self):
        lancamento_contabil = LancamentoContabil(10)
        self.assertIsNone(lancamento_contabil.get_data())
        lancamento_contabil.ano = 2020
        self.assertIsNone(lancamento_contabil.get_data())
        lancamento_contabil.mes = 5
        self.assertIsNone(lancamento_contabil.get_data())
        lancamento_contabil.dia = 5
        self.assertIsNotNone(lancamento_contabil.get_data())

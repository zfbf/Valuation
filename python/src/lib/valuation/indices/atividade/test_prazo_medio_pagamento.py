import unittest

from ..test_indice import TestIndice
from .prazo_medio_pagamento import PrazoMedioPagamento
from ....importacao.economatica.oi_dados_trimestrais_anualizados import Oi2009T12021T3
from ...factories.valuation_periodo_trimestral_factory import ValuationPeriodoTrimestralFactory


class TestPrazoMedioPagamento(TestIndice):
    print_to_stdout = True

    def setUp(self):
        self.prazo_medio_pagamento = PrazoMedioPagamento(
                TestPrazoMedioPagamento.valuation, 2020, 4)

    # A receita líquida operacional pode ser negativa
    def test_get_giro(self):
        giro = self.prazo_medio_pagamento.get_giro()
        self.assertIsNotNone(giro)
        self.assertTrue(giro != 0)

    def test_get_valor(self):
        valor = self.prazo_medio_pagamento.get_valor()
        self.assertIsNotNone(valor)
        self.assertTrue(valor != 0)

    @unittest.skipUnless(print_to_stdout, 'making clean tests')
    def test_to_str(self):
        print('\nprazo_medio_pagamento: {}'.format(self.prazo_medio_pagamento))

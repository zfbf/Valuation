import numbers

from abc import ABC, abstractmethod

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.dre import DRE
from ...contabilidade.lancamento_contabil import LancamentoContabil


class EconomaticaDadosLoader(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def load(self, objeto, periodo, economatica_dados):
        pass

    def load_conta_credora(self,
                           conta_credora,
                           index,
                           periodo,
                           economatica_dados):
        saldo = economatica_dados.get_valor(index, periodo)

        if isinstance(saldo, numbers.Number):
            if saldo < 0:
                conta_credora.add_debito(LancamentoContabil(-saldo))
            else:
                conta_credora.add_credito(LancamentoContabil(saldo))

    def load_conta_devedora(self,
                            conta_devedora,
                            index,
                            periodo,
                            economatica_dados):
        saldo = economatica_dados.get_valor(index, periodo)

        if isinstance(saldo, numbers.Number):
            if saldo < 0:
                conta_devedora.add_credito(LancamentoContabil(-saldo))
            else:
                conta_devedora.add_debito(LancamentoContabil(saldo))

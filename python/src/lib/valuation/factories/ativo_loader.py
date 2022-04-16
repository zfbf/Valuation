import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ...contabilidade.periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.ifrs.balanco_patrimonial import BalancoPatrimonialIFRS
from ...contabilidade.lancamento_contabil import LancamentoContabil


class AtivoIFRSLoader():
    def __init__(self):
        super().__init__()

    def load(self, ativo, codigo_periodo, economatica_dados):
        # Usar economatica_dados para buscar os dados das contas
        # abaixo para o periodo passado
        ativo_index = ('bp', 'ativo')
        saldo = economatica_dados.get_valor(ativo_index, codigo_periodo)
        
        if isinstance(saldo, numbers.Number):
            ativo.valor_verificacao = saldo

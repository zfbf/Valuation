import numbers

from ...contabilidade.periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.ifrs.balanco_patrimonial import BalancoPatrimonialIFRS
from ...contabilidade.lancamento_contabil import LancamentoContabil


class PatrimonioLiquidoIFRSLoader():
    def __init__(self):
        super().__init__()

    def load(self, patrimonio_liquido, periodo, economatica_dados):
        patrimonio_liquido_index = 'bp.patrimonio_liquido'
        saldo = economatica_dados.get_valor(patrimonio_liquido_index, periodo)

        if isinstance(saldo, numbers.Number):
            patrimonio_liquido.valor_verificacao = saldo

        contas = ('capital_social',
                  'reservas_de_capital',
                  'reservas_de_reavaliacao',
                  'reservas_de_lucros',
                  'lucros_acumulados',
                  'ajustes_avaliacao_patrimonial',
                  'ajustes_acumulados_conversao',
                  'outros_resultados_abrangentes')

        for conta in contas:
            conta_index = patrimonio_liquido_index + '.' + conta
            #print('conta_index: {}'.format(conta_index))
            saldo = economatica_dados.get_valor(conta_index, periodo)
            #print('saldo: {}'.format(saldo))

            if isinstance(saldo, numbers.Number):
                conta = patrimonio_liquido.get_conta(conta)
                #print('conta: {}'.format(conta))
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                pass
                #print('Not a number: conta_index: {}, saldo: {}'.format(
                #        conta_index, saldo))

import numbers

from ...contabilidade.periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.ifrs.balanco_patrimonial import BalancoPatrimonialIFRS
from ...contabilidade.lancamento_contabil import LancamentoContabil


class AtivoNaoCirculanteIFRSLoader():
    def __init__(self):
        super().__init__()

    def load(self, ativo_nao_circulante, periodo, economatica_dados):
        ativo_nao_circulante_index = ('bp', 'ativo', 'nao_circulante')
        saldo = economatica_dados.get_valor(ativo_nao_circulante_index, periodo)

        if isinstance(saldo, numbers.Number):
            ativo_nao_circulante.valor_verificacao = saldo

        realizavel_lp_index = ('bp', 'ativo', 'nao_circulante',
                               'realizavel_lp')
        saldo = economatica_dados.get_valor(realizavel_lp_index, periodo)
        realizavel_lp = ativo_nao_circulante.get_conta('realizavel_lp')

        if isinstance(saldo, numbers.Number):
            realizavel_lp.valor_verificacao = saldo

        contas = ('aplicacao_financeira_valor_justo',
                  'aplicacao_financeira_custo_amortizado',
                  'contas_a_receber',
                  'estoques',
                  'ativos_biologicos',
                  'impostos_diferidos',
                  'despesas_antecipadas',
                  'partes_relacionadas',
                  'outros')

        for conta in contas:
            conta_index = realizavel_lp_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = realizavel_lp.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                pass
                #print('Not a number: conta_index: {}, saldo: {}'.format(
                #        conta_index, saldo))

        contas = ('investimentos',
                  'imobilizado')

        for conta in contas:
            conta_index = ativo_nao_circulante_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = ativo_nao_circulante.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                pass
                #print('Not a number: conta_index: {}, saldo: {}'.format(
                #        conta_index, saldo))

        intangiveis_liquido_index = ('bp', 'ativo', 'nao_circulante',
                                     'intangiveis_liquido')
        saldo = economatica_dados.get_valor(intangiveis_liquido_index, periodo)
        intangiveis = ativo_nao_circulante.get_conta('intangiveis_liquido')

        if isinstance(saldo, numbers.Number):
            intangiveis.valor_verificacao = saldo

        contas = ('intangiveis',
                  'goodwill')

        for conta in contas:
            conta_index = intangiveis_liquido_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = intangiveis.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                pass
                #print('Not a number: conta_index: {}, saldo: {}'.format(
                #        conta_index, saldo))

        #TODO: Realizável a longo prazo náo está no ativo não circulante do IFRS.

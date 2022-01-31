import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.default.balanco_patrimonial import BalancoPatrimonialDefault
from ...contabilidade.lancamento_contabil import LancamentoContabil


class AtivoNaoCirculanteDefaultLoader():
    def __init__(self):
        super().__init__()

    def load(self, ativo_nao_circulante, periodo, economatica_dados):
        ativo_nao_circulante_index = ('bp', 'ativo', 'nao_circulante')
        saldo = economatica_dados.get_valor(ativo_nao_circulante_index, periodo)

        if isinstance(saldo, numbers.Number):
            ativo_nao_circulante.valor_verificacao = saldo
        
        contas = ('realizavel_lp',
                  'aplicacao_financeira_custo_amortizado',
                  'contas_a_receber',
                  'estoques',
                  'ativos_biologicos',
                  'impostos_diferidos',
                  'despesas_antecipadas',
                  'partes_relacionadas',
                  'outros',
                  'investimentos',
                  'imobilizado')

        for conta in contas:
            conta_index = ativo_nao_circulante_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = ativo_nao_circulante.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

        intangiveis_liquido_index = ('bp', 'ativo', 'nao_circulante',
                'intangiveis_liquido')
        saldo = economatica_dados.get_valor(intangiveis_liquido_index, periodo)
        conta = ativo_nao_circulante.get_conta('intangiveis_liquido')

        if isinstance(saldo, numbers.Number):
            conta = ativo_nao_circulante.get_conta('intangiveis_liquido')
            conta.valor_verificacao = saldo

        contas = ('intangiveis',
                  'goodwill')

        for conta in contas:
            conta_index = intangiveis_liquido_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = ativo_nao_circulante.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

        #TODO: Realizável a longo prazo náo está no ativo não circulante do IFRS.

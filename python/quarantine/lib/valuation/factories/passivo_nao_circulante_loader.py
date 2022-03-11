import numbers

from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.default.balanco_patrimonial import BalancoPatrimonialDefault
from ...contabilidade.lancamento_contabil import LancamentoContabil


class PassivoNaoCirculanteDefaultLoader():
    def __init__(self):
        super().__init__()

    def load(self, passivo_nao_circulante, periodo, economatica_dados):
        passivo_nao_circulante_index = ('bp', 'passivo', 'nao_circulante')
        saldo = economatica_dados.get_valor(passivo_nao_circulante_index, periodo)

        if isinstance(saldo, numbers.Number):
            passivo_nao_circulante.valor_verificacao = saldo

        contas = ('impostos_diferidos',
                  'provisoes',
                  'lucros_e_receitas_a_apropriar')

        for conta in contas:
            conta_index = passivo_nao_circulante_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = passivo_nao_circulante.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

        conta = passivo_nao_circulante.get_conta('emprestimos_e_financiamentos')
        self.load_emprestimo_e_financiamentos(conta, periodo, economatica_dados)

        conta = passivo_nao_circulante.get_conta('outras_obrigacoes')
        self.load_outras_obrigacoes(conta, periodo, economatica_dados)

    def load_emprestimo_e_financiamentos(self,
                                         emprestimos_e_financiamentos,
                                         periodo,
                                         economatica_dados):

        emp_e_fin_index = ('bp', 'passivo', 'nao_circulante',
                           'emprestimos_e_financiamentos')
        saldo = economatica_dados.get_valor(emp_e_fin_index, periodo)

        if isinstance(saldo, numbers.Number):
            emprestimos_e_financiamentos.valor_verificacao = saldo

        contas = ('debentures',
                  'arrendamento_financeiro')

        for conta in contas:
            conta_index = emp_e_fin_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = emprestimos_e_financiamentos.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

        financiamentos_index = emp_e_fin_index + ('financiamentos', )
        financiamentos = emprestimos_e_financiamentos.get_conta('financiamentos')

        saldo = economatica_dados.get_valor(financiamentos_index, periodo)

        if isinstance(saldo, numbers.Number):
            financiamentos.valor_verificacao = saldo

        contas = ('nacional',
                  'estrangeiro')

        for conta in contas:
            conta_index = financiamentos_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = financiamentos.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

    def load_outras_obrigacoes(self,
                               outras_obrigacoes,
                               periodo,
                               economatica_dados):
        outras_obrigacoes_index = ('bp', 'passivo', 'nao_circulante',
                                   'outras_obrigacoes')
        saldo = economatica_dados.get_valor(outras_obrigacoes_index, periodo)

        if isinstance(saldo, numbers.Number):
            outras_obrigacoes.valor_verificacao = saldo

        contas = ('partes_relacionadas',
                  'outros_lp')

        for conta in contas:
            conta_index = outras_obrigacoes_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = outras_obrigacoes.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

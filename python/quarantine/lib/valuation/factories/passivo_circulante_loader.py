import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.default.balanco_patrimonial import BalancoPatrimonialDefault
from ...contabilidade.lancamento_contabil import LancamentoContabil


class PassivoCirculanteDefaultLoader():
    def __init__(self):
        super().__init__()

    def load(self, passivo_circulante, periodo, economatica_dados):
        passivo_circulante_index = ('bp', 'passivo', 'circulante')
        saldo = economatica_dados.get_valor(passivo_circulante_index, periodo)

        if isinstance(saldo, numbers.Number):
            passivo_circulante.valor_verificacao = saldo

        contas = ('obrigacoes_sociais',
                  'fornecedores',
                  'impostos_a_pagar',
                  'provisoes')

        for conta in contas:
            conta_index = passivo_circulante_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = passivo_circulante.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

        conta = passivo_circulante.get_conta('emprestimos_e_financiamentos')
        self.load_emprestimo_e_financiamentos(conta, periodo, economatica_dados)

        conta = passivo_circulante.get_conta('outras_obrigacoes')
        self.load_outras_obrigacoes(conta, periodo, economatica_dados)

    def load_emprestimo_e_financiamentos(self,
                                         emprestimos_e_financiamentos,
                                         periodo,
                                         economatica_dados):

        emp_e_fin_index = ('bp', 'passivo', 'circulante',
                           'emprestimos_e_financiamentos')
        saldo = economatica_dados.get_valor(emp_e_fin_index, periodo)

        if isinstance(saldo, numbers.Number):
            emprestimos_e_financiamentos.valor_verificacao = saldo

        contas = ('financiamentos',
                  'debentures',
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

    def load_outras_obrigacoes(self,
                               outras_obrigacoes,
                               periodo,
                               economatica_dados):
        outras_obrigacoes_index = ('bp', 'passivo', 'circulante',
                                   'outras_obrigacoes')
        saldo = economatica_dados.get_valor(outras_obrigacoes_index, periodo)

        print('type(outras_obrigacoes: {})'.format(type(outras_obrigacoes)))

        if isinstance(saldo, numbers.Number):
            outras_obrigacoes.valor_verificacao = saldo

        outros_oo = outras_obrigacoes.get_conta('outros_cp')
        outros_oo_index = ('bp', 'passivo', 'circulante',
                           'outras_obrigacoes', 'outros_cp')
        saldo = economatica_dados.get_valor(outros_oo_index, periodo)

        if isinstance(saldo, numbers.Number):
            outros_oo.valor_verificacao = saldo

        contas = ('dividendos',
                  'outros')

        for conta in contas:
            conta_index = outros_oo_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                conta = outros_oo.get_conta(conta)
                print('conta_index: {})'.format(conta_index))
                print('saldo: {})'.format(saldo))
                print('type(conta: {})'.format(type(conta)))
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ...contabilidade.periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.ifrs.balanco_patrimonial import BalancoPatrimonialIFRS
from ...contabilidade.lancamento_contabil import LancamentoContabil


class PassivoCirculanteIFRSLoader():
    def __init__(self):
        super().__init__()

    def load(self, passivo_circulante, codigo_periodo, economatica_dados):
        passivo_circulante_index = 'bp.passivo.circulante'
        saldo = economatica_dados.get_valor(passivo_circulante_index, codigo_periodo)

        if isinstance(saldo, numbers.Number):
            passivo_circulante.valor_verificacao = saldo

        contas = ('obrigacoes_sociais',
                  'fornecedores',
                  'impostos_a_pagar',
                  'provisoes')

        for conta in contas:
            conta_index = passivo_circulante_index + '.' + conta
            saldo = economatica_dados.get_valor(conta_index, codigo_periodo)

            if isinstance(saldo, numbers.Number):
                conta = passivo_circulante.get_conta(conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                pass
                #print('Not a number: conta_index: {}, saldo: {}'.format(
                #        conta_index, saldo))

        conta = passivo_circulante.get_conta('emprestimos_e_financiamentos')
        self.load_emprestimo_e_financiamentos(conta, codigo_periodo, economatica_dados)

        conta = passivo_circulante.get_conta('outras_obrigacoes')
        self.load_outras_obrigacoes(conta, codigo_periodo, economatica_dados)

    def load_emprestimo_e_financiamentos(self,
                                         emprestimos_e_financiamentos,
                                         codigo_periodo,
                                         economatica_dados):

        emp_e_fin_index = 'bp.passivo.circulante.emprestimos_e_financiamentos'
        saldo = economatica_dados.get_valor(emp_e_fin_index, codigo_periodo)

        if isinstance(saldo, numbers.Number):
            emprestimos_e_financiamentos.valor_verificacao = saldo

        codigos_contas = ('financiamentos',
                          'debentures',
                          'arrendamento_financeiro')

        for codigo_conta in codigos_contas:
            conta_index = emp_e_fin_index + '.' + codigo_conta
            saldo = economatica_dados.get_valor(conta_index, codigo_periodo)

            if isinstance(saldo, numbers.Number):
                conta = emprestimos_e_financiamentos.get_conta(codigo_conta)
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                pass
                #print('Not a number: conta_index: {}, saldo: {}'.format(
                #        conta_index, saldo))

    def load_outras_obrigacoes(self,
                               outras_obrigacoes,
                               codigo_periodo,
                               economatica_dados):
        outras_obrigacoes_index = 'bp.passivo.circulante.outras_obrigacoes'
        saldo = economatica_dados.get_valor(outras_obrigacoes_index,
                codigo_periodo)

        if isinstance(saldo, numbers.Number):
            outras_obrigacoes.valor_verificacao = saldo

        outros_cp = outras_obrigacoes.get_conta('outros_cp')
        outros_cp_index = 'bp.passivo.circulante.outras_obrigacoes.outros_cp'
        saldo = economatica_dados.get_valor(outros_cp_index, codigo_periodo)

        if isinstance(saldo, numbers.Number):
            outros_cp.valor_verificacao = saldo

        codigos_contas = ('dividendos',
                          'outros')

        for codigo_conta in codigos_contas:
            conta_index = outros_cp_index + '.' + codigo_conta
            #print('\n##########################################')
            #print('codigo_periodo: {}'.format(codigo_periodo))
            #print('codigo_conta: {}'.format(codigo_conta))
            #print('conta_index: {}'.format(conta_index))

            saldo = economatica_dados.get_valor(conta_index, codigo_periodo)

            #print('saldo: {}'.format(saldo))

            if isinstance(saldo, numbers.Number):
                conta = outros_cp.get_conta(codigo_conta)
                #print('conta: {}'.format(conta))
                #print('conta_index: {})'.format(conta_index))
                #print('saldo: {})'.format(saldo))
                #print('type(conta: {})'.format(type(conta)))
                conta.increase_saldo(LancamentoContabil(saldo))
            else:
                #msg = 'Not a number: codigo_periodo: {}'.format(codigo_periodo)
                #msg += ',\tconta_index: {}'.format(conta_index)
                #msg += ',\tsaldo: {}'.format(saldo)
                #print(msg)
                pass

            #print('saldo: {}'.format(saldo))
            #print('##########################################\n')

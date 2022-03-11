import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.default.balanco_patrimonial import BalancoPatrimonialDefault
from ...contabilidade.lancamento_contabil import LancamentoContabil


class AtivoCirculanteDefaultLoader():
    def __init__(self):
        super().__init__()

    def load(self, ativo_circulante, periodo, economatica_dados):
        # Usar economatica_dados para buscar os dados das contas
        # abaixo para o periodo passado
        ativo_circulante_index = ('bp', 'ativo', 'circulante')
        saldo = economatica_dados.get_valor(ativo_circulante_index, periodo)

        if isinstance(saldo, numbers.Number):
            ativo_circulante.valor_verificacao = saldo

        contas = ('caixa_e_equivalentes',
                  'aplicacoes_financeiras',
                  'contas_a_receber',
                  'estoques',
                  'ativos_biologicos',
                  'impostos_a_recuperar',
                  'despesas_antecipadas',
                  'outros')

        ano = int(periodo)

        for conta in contas:
            conta_index = ativo_circulante_index + (conta, )
            saldo = economatica_dados.get_valor(conta_index, periodo)

            if isinstance(saldo, numbers.Number):
                print('conta_index: {}, saldo: {}'.format(conta_index, saldo))
                conta = ativo_circulante.get_conta(conta)
                print('type(conta): {}'.format(type(conta)))
                print('#1 - conta: {}'.format(conta))
                conta.increase_saldo(LancamentoContabil(saldo, ano=ano))
                print('conta.get_saldo(): {}'.format(conta.get_saldo()))
                print('#2 - conta: {}'.format(conta))
            else:
                print('Not a number: conta_index: {}, saldo: {}'.format(
                        conta_index, saldo))

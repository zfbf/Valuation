import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from .economatica_dados_loader import EconomaticaDadosLoader
from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.dfc import DFC
from ...contabilidade.lancamento_contabil import LancamentoContabil


class DFCLoader(EconomaticaDadosLoader):
    def __init__(self):
        super().__init__()

    def load(self, dfc, periodo, economatica_dados):
        self.load_operacional(dfc.operacional,
                              periodo,
                              economatica_dados)

    def load_operacional(self,
                         operacional,
                         periodo,
                         economatica_dados):
        base_index = ('dfc', 'operacional')
        saldo = economatica_dados.get_valor(base_index, periodo)

        if isinstance(saldo, numbers.Number):
            operacional.valor_verificacao = saldo

        operacao = operacional.get_conta('operacao')
        operacao_index = base_index + ('operacao', )
        saldo = economatica_dados.get_valor(operacao_index, periodo)

        if isinstance(saldo, numbers.Number):
            operacao.valor_verificacao = saldo

        contas_credoras_codes = (
                'lucro_liquido',
                'depreciacao_amortizacao_exaustao',
                'variacao_cambial',
                'venda_ativos_permanentes',
                'valor_contabil',
                'equivalencia_patrimonial',
                'impostos_diferidos',
                'variacao_minoritarios',
                'outros_extra_caixa')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    operacao.get_conta(code),
                    operacao_index + (code, ),
                    periodo,
                    economatica_dados
            )

        var_atv_pass = operacional.get_conta('variacao_ativos_passivos')
        var_atv_pass_index = base_index + ('variacao_ativos_passivos', )
        saldo = economatica_dados.get_valor(var_atv_pass_index, periodo)

        if isinstance(saldo, numbers.Number):
            var_atv_pass.valor_verificacao = saldo

        contas_credoras_codes = (
                'variacao_duplicatas_a_receber',
                'variacao_estoques',
                'variacao_outros_ativos',
                'variacao_fornecedores',
                'variacao_importacao',
                'variacao_outros_passivos')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    var_atv_pass.get_conta(code),
                    var_atv_pass_index + (code, ),
                    periodo,
                    economatica_dados
            )

        outros = operacional.get_conta('outros')
        outros_index = base_index + ('outros', )
        saldo = economatica_dados.get_valor(outros_index, periodo)

        if isinstance(saldo, numbers.Number):
            outros.add_credito(LancamentoContabil(saldo))

import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from .economatica_dados_loader import EconomaticaDadosLoader
from ...contabilidade.periodo_contabil import PeriodoContabil
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

        self.load_investimentos(dfc.investimentos,
                                periodo,
                                economatica_dados)

        self.load_financiamentos(dfc.financiamentos,
                                 periodo,
                                 economatica_dados)

        self.load_conta_credora(
                dfc.efeito_cambial,
                'dfc.efeito_cambial',
                periodo,
                economatica_dados
        )

        self.load_conta_credora(
                dfc.outras_variacoes,
                'dfc.outras_variacoes',
                periodo,
                economatica_dados
        )

        var_liq_caixa_index = 'dfc.var_liquida_de_caixa'
        saldo = economatica_dados.get_valor(var_liq_caixa_index, periodo)

        if isinstance(saldo, numbers.Number):
            dfc.variacao_liquida_de_caixa.valor_verificacao = saldo

    def load_operacional(self,
                         operacional,
                         periodo,
                         economatica_dados):
        base_index = 'dfc.operacional'
        saldo = economatica_dados.get_valor(base_index, periodo)

        if isinstance(saldo, numbers.Number):
            operacional.valor_verificacao = saldo

        operacao = operacional.get_conta('operacao')
        operacao_index = base_index + '.operacao'
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
                    operacao_index + '.' + code,
                    periodo,
                    economatica_dados
            )

        var_atv_pass = operacional.get_conta('variacao_ativos_passivos')
        var_atv_pass_index = base_index + '.variacao_ativos_passivos'
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
                    var_atv_pass_index + '.' + code,
                    periodo,
                    economatica_dados
            )

        self.load_conta_credora(
                operacional.get_conta('outros'),
                base_index + '.outros',
                periodo,
                economatica_dados
        )

    def load_investimentos(self,
                           investimentos,
                           periodo,
                           economatica_dados):
        base_index = 'dfc.investimentos'
        saldo = economatica_dados.get_valor(base_index, periodo)

        if isinstance(saldo, numbers.Number):
            investimentos.valor_verificacao = saldo

        compra_liq_atv_permnt = investimentos.get_conta(
                'compra_liquida_ativos_permanentes')
        compra_liq_atv_permnt_index = (base_index +
                '.compra_liquida_ativos_permanentes')
        saldo = economatica_dados.get_valor(compra_liq_atv_permnt_index, periodo)

        if isinstance(saldo, numbers.Number):
            compra_liq_atv_permnt.valor_verificacao = saldo

        contas_credoras_codes = (
                'compra_investimentos_permanentes',
                'compra_ativos_fixos',
                'venda_ativos_permanentes')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    compra_liq_atv_permnt.get_conta(code),
                    compra_liq_atv_permnt_index + '.' + code,
                    periodo,
                    economatica_dados
            )

        contas_credoras_codes = (
                'dividendos_recebidos',
                'resgate_aplicacao_financeira_liquida',
                'outros')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    investimentos.get_conta(code),
                    base_index + '.' + code,
                    periodo,
                    economatica_dados
            )

    def load_financiamentos(self,
                            financiamentos,
                            periodo,
                            economatica_dados):
        base_index = 'dfc.financiamentos'
        saldo = economatica_dados.get_valor(base_index, periodo)

        if isinstance(saldo, numbers.Number):
            financiamentos.valor_verificacao = saldo

        financiamentos_liq = financiamentos.get_conta('financiamentos_liquido')
        financiamentos_liq_index = base_index + '.financiamentos_liquido'
        saldo = economatica_dados.get_valor(financiamentos_liq_index, periodo)

        if isinstance(saldo, numbers.Number):
            financiamentos_liq.valor_verificacao = saldo

        contas_credoras_codes = (
                'financiamentos_obtidos',
                'financiamentos_pagos')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    financiamentos_liq.get_conta(code),
                    financiamentos_liq_index + '.' + code,
                    periodo,
                    economatica_dados
            )

        aumnt_liq_capital = financiamentos.get_conta('aumento_liquido_de_capital')
        aumnt_liq_capital_index = base_index + '.aumento_liquido_de_capital'
        saldo = economatica_dados.get_valor(aumnt_liq_capital_index, periodo)

        if isinstance(saldo, numbers.Number):
            aumnt_liq_capital.valor_verificacao = saldo

        contas_credoras_codes = (
                'aumento_de_capital',
                'reducao_de_capital')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    aumnt_liq_capital.get_conta(code),
                    aumnt_liq_capital_index + '.' + code,
                    periodo,
                    economatica_dados
            )

        contas_credoras_codes = (
                'dividendos_pagos',
                'outros')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    financiamentos.get_conta(code),
                    base_index + '.' + code,
                    periodo,
                    economatica_dados
            )

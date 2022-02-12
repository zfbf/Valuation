import numbers

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.dre import DRE
from ...contabilidade.lancamento_contabil import LancamentoContabil


class DRELoader():
    def __init__(self):
        super().__init__()

    def load(self, dre, periodo, economatica_dados):
        receita_liquida_index = ('dre', 'receita_liquida_operacional')
        saldo = economatica_dados.get_valor(receita_liquida_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.receita_liquida_operacional.add_credito(LancamentoContabil(saldo))

        cpv_index = ('dre', 'custo_produtos_vendidos')
        saldo = economatica_dados.get_valor(cpv_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.custo_produtos_vendidos.add_debito(LancamentoContabil(saldo))

        lucro_bruto_index = ('dre', 'lucro_bruto')
        saldo = economatica_dados.get_valor(lucro_bruto_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.lucro_bruto.valor_verificacao = saldo

        self.load_despesas_operacionais(dre.despesas_operacionais,
                                        periodo,
                                        economatica_dados)

        lajir_index = ('dre', 'lajir')
        saldo = economatica_dados.get_valor(lajir_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.lajir.valor_verificacao = saldo

        self.load_resultado_financeiro(dre.resultado_financeiro,
                                       periodo,
                                       economatica_dados)

        lair_index = ('dre', 'lair')
        saldo = economatica_dados.get_valor(lair_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.lair.valor_verificacao = saldo

        self.load_ircs(dre.ircs,
                       periodo,
                       economatica_dados)

        lucro_oper_continuadas_index = ('dre', 'lucro_oper_continuadas')
        saldo = economatica_dados.get_valor(lucro_oper_continuadas_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.lucro_oper_continuadas.valor_verificacao = saldo

        operacoes_descontinuadas_index = ('dre', 'operacoes_descontinuadas')
        saldo = economatica_dados.get_valor(operacoes_descontinuadas_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.operacoes_descontinuadas.add_credito(LancamentoContabil(saldo))

        lucro_consolidado_index = ('dre', 'lucro_consolidado')
        saldo = economatica_dados.get_valor(lucro_consolidado_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.lucro_consolidado.valor_verificacao = saldo

        participacao_minoritaria_index = ('dre', 'participacao_minoritaria')
        saldo = economatica_dados.get_valor(participacao_minoritaria_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.participacao_minoritaria.add_debito(LancamentoContabil(saldo))

        lucro_liquido_index = ('dre', 'lucro_liquido')
        saldo = economatica_dados.get_valor(lucro_liquido_index, periodo)

        if isinstance(saldo, numbers.Number):
            dre.lucro_liquido.valor_verificacao = saldo

    def load_despesas_operacionais(self,
                                   despesas_operacionais,
                                   periodo,
                                   economatica_dados):
        base_index = ('dre', 'despesas_operacionais')
        saldo = economatica_dados.get_valor(base_index, periodo)

        if isinstance(saldo, numbers.Number):
            despesas_operacionais.valor_verificacao = saldo

        contas_devedoras_codes = (
                'despesas_com_vendas',
                'despesas_administrativas',
                'perdas_recuperacao_de_ativos',
                'outras_despesas_operacionais')

        for code in contas_devedoras_codes:
            self.load_conta_devedora(
                    despesas_operacionais.get_conta(code),
                    base_index + (code, ),
                    periodo,
                    economatica_dados
            )

        contas_credoras_codes = (
                'outras_receitas_operacionais',
                'equivalencia_patrimonial')

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    despesas_operacionais.get_conta(code),
                    base_index + (code, ),
                    periodo,
                    economatica_dados
            )

    def load_resultado_financeiro(self,
                                  resultado_financeiro,
                                  periodo,
                                  economatica_dados):
        base_index = ('dre', 'resultado_financeiro')
        saldo = economatica_dados.get_valor(base_index, periodo)

        if isinstance(saldo, numbers.Number):
            resultado_financeiro.valor_verificacao = saldo

        contas_credoras_codes = ('receitas_financeiras', )

        for code in contas_credoras_codes:
            self.load_conta_credora(
                    resultado_financeiro.get_conta(code),
                    base_index + (code, ),
                    periodo,
                    economatica_dados
            )

        contas_devedoras_codes = ('despesas_financeiras', )

        for code in contas_devedoras_codes:
            self.load_conta_devedora(
                    resultado_financeiro.get_conta(code),
                    base_index + (code, ),
                    periodo,
                    economatica_dados
            )

    def load_ircs(self, ircs, periodo, economatica_dados):
        base_index = ('dre', 'ircs')
        saldo = economatica_dados.get_valor(base_index, periodo)

        if isinstance(saldo, numbers.Number):
            ircs.valor_verificacao = saldo

        contas_devedoras_codes = ('provisao_ir', 'ir_diferido')

        for code in contas_devedoras_codes:
            self.load_conta_devedora(
                    ircs.get_conta(code),
                    base_index + (code, ),
                    periodo,
                    economatica_dados
            )

    def load_conta_credora(self,
                           conta_credora,
                           index,
                           periodo,
                           economatica_dados):
        saldo = economatica_dados.get_valor(index, periodo)

        if isinstance(saldo, numbers.Number):
            if saldo < 0:
                conta_credora.add_debito(LancamentoContabil(-saldo))
            else:
                conta_credora.add_credito(LancamentoContabil(saldo))

    def load_conta_devedora(self,
                            conta_devedora,
                            index,
                            periodo,
                            economatica_dados):
        saldo = economatica_dados.get_valor(index, periodo)

        if isinstance(saldo, numbers.Number):
            if saldo < 0:
                conta_devedora.add_credito(LancamentoContabil(-saldo))
            else:
                conta_devedora.add_debito(LancamentoContabil(saldo))

from .conta_devedora import ContaDevedora
from .conta_credora import ContaCredora
from .grupo_contas import GrupoContas
from .conta_resultado_credora import ContaResultadoCredora
from ..natureza import Natureza


class DFC:
    def __init__(self):
        super().__init__()
        self.init_contas()

    def init_contas(self):
        self.init_operacional()
        self.init_investimentos()
        self.init_financiamentos()

    def init_operacional(self):
        self.operacional = GrupoContas(
                'operacional',
                'Operacional',
                Natureza.CREDORA,
                self)

        operacao = GrupoContas(
                'operacao',
                'Operação',
                Natureza.CREDORA,
                self)

        self.operacional.add_conta(operacao)

        contas = (('lucro_liquido', 'Lucro Líquido'),
                  ('depreciacao_amortizacao_exaustao', 'Depreciação, Amortização e Exaustão'),
                  ('variacao_cambial', 'Variação Cambial'),
                  ('venda_ativos_permanentes', 'Venda Ativos Permanentes'),
                  ('valor_contabil', 'Valor Contábil'),
                  ('equivalencia_patrimonial', 'Equivalência Patrimonial'),
                  ('impostos_diferidos', 'Impostos Diferidos'),
                  ('variacao_minoritarios', 'Variação Participação Minoritários'),
                  ('outros_extra_caixa', 'Outros'))

        for conta in contas:
            operacao.add_conta(ContaCredora(conta[0], conta[1]))

        variacao_ativos_passivos = GrupoContas(
                'variacao_ativos_passivos',
                'Variação Ativos Passivos',
                Natureza.CREDORA,
                self)

        self.operacional.add_conta(variacao_ativos_passivos)

        contas = (('variacao_duplicatas_a_receber', 'Variação Duplicatas a Receber'),
                  ('variacao_estoques', 'Variação Estoques'),
                  ('variacao_outros_ativos', 'Variação Outros Ativos'),
                  ('variacao_fornecedores', 'Variação Fornecedores'),
                  ('variacao_importacao', 'Variação Importação'),
                  ('variacao_outros_passivos', 'Variação Outros Passivos'))

        for conta in contas:
            variacao_ativos_passivos.add_conta(ContaCredora(conta[0], conta[1]))

        self.operacional.add_conta(ContaCredora('outros', 'Outros'))

    def init_investimentos(self):
        self.investimentos = GrupoContas(
                'investimentos',
                'Investimentos',
                Natureza.CREDORA,
                self)

        compra_liquida_ativos_permanentes = GrupoContas(
                'compra_liquida_ativos_permanentes',
                'Compra Líquida Ativos Permanentes',
                Natureza.CREDORA,
                self)

        self.investimentos.add_conta(compra_liquida_ativos_permanentes)

        contas = (('compra_investimentos_permanentes', 'Compra Investimentos Permanentes'),
                  ('compra_ativos_fixos', 'Compra Ativos Fixos'),
                  ('venda_ativos_permanentes', 'Venda Ativos Permanentes'))

        for conta in contas:
            compra_liquida_ativos_permanentes.add_conta(ContaCredora(conta[0], conta[1]))

        contas = (('dividendos_recebidos', 'Dividendos Recebidos'),
                  ('resgate_aplicacao_financeira_liquida',
                            'Resgate Aplicação Financeira Líquida'),
                  ('outros', 'Outros Investimentos'))

        for conta in contas:
            self.investimentos.add_conta(ContaCredora(conta[0], conta[1]))

    def init_financiamentos(self):
        self.financiamentos = GrupoContas(
                'financiamentos',
                'Financiamentos',
                Natureza.CREDORA,
                self)

        financiamentos_liquido = GrupoContas(
                'financiamentos_liquido',
                'Financiamentos Líquido',
                Natureza.CREDORA,
                self)

        self.financiamentos.add_conta(financiamentos_liquido)

        contas = (('financiamentos_obtidos', 'Financiamentos Obtidos'),
                  ('financiamentos_pagos', 'Financiamentos Pagos'))

        for conta in contas:
            financiamentos_liquido.add_conta(ContaCredora(conta[0], conta[1]))

        aumento_liquido_de_capital = GrupoContas(
                'aumento_liquido_de_capital',
                'Aumento Líquido de Capital',
                Natureza.CREDORA,
                self)

        self.financiamentos.add_conta(aumento_liquido_de_capital)

        contas = (('aumento_de_capital', 'Aumento de Capital'),
                  ('reducao_de_capital', 'Redução de Capital'))

        for conta in contas:
            aumento_liquido_de_capital.add_conta(ContaCredora(conta[0], conta[1]))

        self.financiamentos.add_conta(ContaCredora('dividendos_pagos',
                'Dividendos Pagos'))

        self.financiamentos.add_conta(ContaCredora('outros',
                'Outros'))

    def get_conta(self, codigo):
        conta = None
        grupos = [self.ativo, self.passivo, self.patrimonio_liquido]

        for grupo in grupos:
            conta = grupo.get_conta(codigo)

            if conta is not None:
                break

        return conta

    def rename_conta_caixa(self, nome):
        self.ativo.circulante.rename_conta_caixa(nome)

    def __str__(self):
        repr = 'Plano de Contas:\n- DFC:\n'
        repr += str(self.operacional)
        repr += str(self.investimentos)
        repr += str(self.financiamentos)
        return repr

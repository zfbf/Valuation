from .conta_devedora import ContaDevedora
from .conta_credora import ContaCredora
from .grupo_contas import GrupoContas
from .conta_resultado_credora import ContaResultadoCredora
from ..natureza import Natureza


class DRE:
    def __init__(self):
        super().__init__()

    def init_contas(self):
        self.receita_liquida_operacional = ContaCredora(
                'receita_liquida_operacional',
                'Receita Líquida Operacional')

        self.custo_produtos_vendidos = ContaDevedora(
                'custo_produtos_vendidos',
                'Custo Produtos Vendidos')

        self.lucro_bruto = ContaResultadoCredora(
                'lucro_bruto', 'Lucro Bruto')
        self.lucro_bruto.add_conta(self.receita_liquida_operacional)
        self.lucro_bruto.add_conta(self.custo_produtos_vendidos)

        self.despesas_operacionais = GrupoContas(
                'despesas_operacionais',
                'Despesas Operacionais',
                Natureza.DEVEDORA,
                self)

        contas = (('despesas_com_vendas', 'Despesas com Vendas'),
                  ('despesas_administrativas', 'Despesas Administrativas'),
                  ('perdas_recuperacao_de_ativos', 'Perdas Recuperação de Ativos'),
                  ('outras_receitas_operacionais', 'Outras Receitas Operacionais'),
                  ('outras_despesas_operacionais', 'Outras Despesas Operacionais'),
                  ('equivalencia_patrimonial', 'Equivalência Patrimonial'))

        for conta in contas:
            self.despesas_operacionais.add_conta(ContaDevedora(conta[0], conta[1]))

        self.lajir = ContaResultadoCredora('lajir', 'LAJIR')
        self.lajir.add_conta(self.lucro_bruto)
        self.lajir.add_conta(self.despesas_operacionais)

        self.resultado_financeiro = GrupoContas(
                'resultado_financeiro',
                'Resultado Financeiro',
                Natureza.CREDORA,
                self)

        contas = (ContaCredora('receitas_financeiras', 'Receitas Financeiras'),
                  ContaDevedora('despesas_financeiras', 'Despesas Financeiras'))

        for conta in contas:
            self.resultado_financeiro.add_conta(conta)

        self.lair = ContaResultadoCredora('lair', 'LAIR')
        self.lair.add_conta(self.lajir)
        self.lair.add_conta(self.resultado_financeiro)

        self.ircs = GrupoContas(
                'icrs',
                'Imposto de Renda e Contribuição Social',
                Natureza.DEVEDORA,
                self)

        contas = (ContaDevedora('provisao_ir', 'Provisão de Imposto de Renda'),
                  ContaDevedora('ir_diferido', 'Imposto de Renda Diferido'))

        for conta in contas:
            self.ircs.add_conta(conta)

        self.lucro_oper_continuadas = ContaResultadoCredora(
                'lucro_oper_continuadas',
                'Lucro Operações Continuadas')
        self.lucro_oper_continuadas.add_conta(self.lair)
        self.lucro_oper_continuadas.add_conta(self.ircs)

        self.operacoes_descontinuadas = ContaCredora(
                'operacoes_descontinuadas',
                'Operações Descontinuadas')

        self.lucro_consolidado = ContaResultadoCredora(
                'lucro_consolidado',
                'Lucro Consolidado')
        self.lucro_consolidado.add_conta(self.lucro_oper_continuadas)
        self.lucro_consolidado.add_conta(self.operacoes_descontinuadas)

        self.participacao_minoritaria = ContaDevedora(
                'participacao_minoritaria',
                'Participação Minoritária')

        self.lucro_liquido = ContaResultadoCredora(
                'lucro_liquido',
                'Lucro Líquido')
        self.lucro_liquido.add_conta(self.lucro_consolidado)
        self.lucro_liquido.add_conta(self.participacao_minoritaria)

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
        repr = 'Plano de Contas:\n- DRE:\n'
        repr += str(self.receita_liquida_operacional)
        repr += '\n'
        repr += str(self.custo_produtos_vendidos)
        repr += str(self.lucro_bruto)
        repr += str(self.despesas_operacionais)
        repr += str(self.lajir)
        repr += str(self.resultado_financeiro)
        repr += str(self.lair)
        repr += str(self.ircs)
        repr += str(self.lucro_oper_continuadas)
        repr += str(self.operacoes_descontinuadas)
        repr += str(self.lucro_consolidado)
        repr += '\n'
        repr += str(self.participacao_minoritaria)
        repr += str(self.lucro_liquido)
        return repr

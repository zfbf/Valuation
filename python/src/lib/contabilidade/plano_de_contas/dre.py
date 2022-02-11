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

        self.lair = ContaResultadoCredora('lair', 'LAIR')
        self.lair.add_conta(self.receita_liquida_operacional)
        self.lair.add_conta(self.custo_produtos_vendidos)
        self.lair.add_conta(self.despesas_operacionais)

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
        repr += str(self.lair)
        return repr

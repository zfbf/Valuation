from abc import ABC, abstractmethod

from lib.contabilidade.plano_de_contas.ativo import Ativo
from lib.contabilidade.plano_de_contas.conta_devedora import ContaDevedora
from lib.contabilidade.plano_de_contas.conta_credora import ContaCredora
from lib.contabilidade.plano_de_contas.grupo_contas import GrupoContas
from lib.contabilidade.plano_de_contas.plano_de_contas import PlanoDeContas
from lib.contabilidade.natureza import Natureza


class PlanoDeContasOtp(PlanoDeContas):
    def init_contas_ativo_circulante(self):
        aux = (('aplicacoes_financeiras', 'Aplicações financeiras'),
               ('contas_a_receber', 'Contas a receber'),
               ('partes_relacionadas', 'Partes relacionadas'),
               ('tributos_a_recuperar', 'Tributos a recuperar'),
               ('despesas_antecipadas', 'Despesas antecipadas'),
               ('outros', 'Outros ativos'))

        for pars in aux:
            self.add_conta_ativo_circulante(ContaDevedora(pars[0], pars[1]))

        self.ativo.circulante.rename_conta_caixa('Caixa e equivalentes de caixa')

    def init_contas_ativo_nao_circulante(self):
        realizavel_a_longo_prazo = GrupoContas('realizavel_a_longo_prazo',
                'Realizável a longo prazo', Natureza.DEVEDORA,
                 self.ativo.nao_circulante)

        aux = (('mantidos_para_negociacao',
                    'Ativos não circulantes mantidos para negociação'),
               ('aplicacoes_financeiras', 'Aplicações financeiras'),
               ('contas_a_receber', 'Contas a receber'),
               ('partes_relacionadas', 'Partes relacionadas'),
               ('depositos_judiciais', 'Depósitos judiciais'),
               ('ir_e_cs_diferidos',
                    'Imposto de renda e contribuição social diferidos'),
               ('outros', 'Outros ativos'))

        for pars in aux:
            realizavel_a_longo_prazo.add_conta(ContaDevedora(
                    pars[0], pars[1], self.ativo.nao_circulante))

        self.ativo.nao_circulante.add_conta(realizavel_a_longo_prazo)
        aux = (('investimentos', 'Investimentos'),
               ('imobilizado', 'Imobilizado'),
               ('intangivel', 'Intangível'))

        for pars in aux:
            self.add_conta_ativo_nao_circulante(ContaDevedora(pars[0], pars[1]))

    def init_contas_passivo_circulante(self):
        aux = (('emp_financ_debentures',
                    'Empréstimos, financiamentos e debêntures'),
               ('arrendamento_mercantil', 'Arrendamento mercantil'),
               ('fornecedores', 'Fornecedores'),
               ('obrigacoes_sociais_e_trabalhistas',
                    'Obrigações sociais e trabalhistas'),
               ('impostos_taxas_e_contribuições_sociais',
                    'Impostos, taxas e contribuições sociais'),
               ('outros', 'Outros passivos'))

        for pars in aux:
            self.add_conta_passivo_circulante(ContaCredora(pars[0], pars[1]))

    def init_contas_passivo_nao_circulante(self):
        aux = (('emp_financ_debentures',
                    'Empréstimos, financiamentos e debêntures'),
               ('arrendamento_mercantil', 'Arrendamento mercantil'),
               ('fornecedores', 'Fornecedores'),
               ('partes_relacionadas', 'Partes relacionadas'),
               ('prov_civeis_trabalhistas_e_previdenciarias',
                    'Provisões cíveis, trabalhistas e previdenciárias'),
               ('prov_conserva_especial', 'Provisão para conserva especial'),
               ('outros', 'Outros passivos'))

        for pars in aux:
            self.add_conta_passivo_nao_circulante(ContaCredora(pars[0], pars[1]))

    def init_contas_patrimonio_liquido(self):
        aux = (('capital_social', 'Capital social'),
               ('reservas_de_capital', 'Reservas de capital'),
               ('ajustes_de_avaliacao_patrimonial',
                    'Ajustes de avaliação patrimonial'),
               ('prejuizos_acumulados', 'Prejuízos acumulados'))

        for pars in aux:
            self.add_conta_patrimonio_liquido(ContaCredora(pars[0], pars[1]))

from abc import ABC, abstractmethod

from lib.contabilidade.plano_de_contas.ativo import Ativo
from lib.contabilidade.plano_de_contas.conta_devedora import ContaDevedora
from lib.contabilidade.plano_de_contas.plano_de_contas import PlanoDeContas


class PlanoDeContasDummy(PlanoDeContas):
    def init_contas_ativo_circulante(self):
        aux = (('duplicatas_a_receber', 'Duplicatas a Receber'),
               ('estoques', 'Estoques'),
               ('despesas_antecipadas', 'Despesas Antecipadas'),
               ('outros_ativos_circulantes', 'Outros Ativos'))

        for pars in aux:
            self.ativo.circulante.add_conta(ContaDevedora(pars[0], pars[1]))

    def init_contas_ativo_nao_circulante(self):
        aux = (('depositos_judiciais', 'Depósitos judiciais'),
               ('tributos_a_recuperar', 'Tributos a recuperar'),
               ('outros_ativos_nao_circulates', 'Outros ativos'))

        for pars in aux:
            self.ativo.nao_circulante.add_conta(ContaDevedora(pars[0], pars[1]))

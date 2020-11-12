from abc import ABC, abstractmethod

from .ativo import Ativo
from .passivo import Passivo
from .patrimonio_liquido import PatrimonioLiquido
from .conta_devedora import ContaDevedora


#
# O PlanoDeContas foi concebido para:
# - Aglutinar todas as contas de um determinado período;
# - Promover a independência de contas entre períodos de análises diferentes;
# - Promover a consistência das contas de forma a evitar lançamentos em
#   contas com nomes parecidos ou nomenclaturas diferentes, ou seja,
#   garantir que lançamentos destinados a uma determinada conta não sejam
#   lançados em objetos diferentes.
#
# Utilização:
# - O ideal é que o objeto que contenha o :PlanoDeContas tenha métodos
#   específicos para retornar o plano de contas de um determinado período
#   de forma a garantir a independência de contas entre períodos diferentes,
#   ou seja, o :PlanoDeContas do primeiro trimestre de um determinado ano terá
#   o mesmo conjunto de contas do período anual.
#
class PlanoDeContas(ABC):
    def __init__(self):
        super().__init__()
        self.ativo = Ativo()
        self.init_contas_ativo_circulante()
        self.init_contas_ativo_nao_circulante()
        self.passivo = Passivo()
        self.init_contas_passivo_circulante()
        self.init_contas_passivo_nao_circulante()
        self.patrimonio_liquido = PatrimonioLiquido()
        self.init_contas_patrimonio_liquido()

    @abstractmethod
    def init_contas_ativo_circulante(self):
        pass

    @abstractmethod
    def init_contas_ativo_nao_circulante(self):
        pass

    @abstractmethod
    def init_contas_passivo_circulante(self):
        pass

    @abstractmethod
    def init_contas_passivo_nao_circulante(self):
        pass

    @abstractmethod
    def init_contas_patrimonio_liquido(self):
        pass

    def get_conta(self, codigo):
        conta = self.ativo.get_conta(codigo)
        return conta

    def add_conta_ativo_circulante(self, conta):
        self.ativo.circulante.add_conta(conta)

    def add_conta_ativo_nao_circulante(self, conta):
        self.ativo.nao_circulante.add_conta(conta)

    def add_conta_passivo_circulante(self, conta):
        self.passivo.circulante.add_conta(conta)

    def add_conta_passivo_nao_circulante(self, conta):
        self.passivo.nao_circulante.add_conta(conta)

    def add_conta_patrimonio_liquido(self, conta):
        self.patrimonio_liquido.add_conta(conta)

    def rename_conta_caixa(self, nome):
        self.ativo.circulante.rename_conta_caixa(nome)

    def __str__(self):
        repr = 'Plano de Contas:\n- Balanço Patrimonial:\n'
        repr += str(self.ativo)
        repr += str(self.passivo)
        repr += str(self.patrimonio_liquido)
        repr += '\n\tTotal Ativo: {:.2f}'.format(self.ativo.get_saldo())
        repr += '\n\tTotal Passivo + Patrimônio Líquido: {:.2f}'.format(
                self.passivo.get_saldo() + self.patrimonio_liquido.get_saldo())
        return repr


class DummyPlanoDeContas(PlanoDeContas):
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

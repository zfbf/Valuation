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
        self.build_ativo()
        self.build_passivo()
        self.build_patrimonio_liquido()
        self.init_contas()

    @abstractmethod
    def build_ativo(self):
        pass

    @abstractmethod
    def build_passivo(self):
        pass

    @abstractmethod
    def build_patrimonio_liquido(self):
        pass

    def init_contas(self):
        self.ativo.init_contas()
        self.passivo.init_contas()
        self.patrimonio_liquido.init_contas()

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
        repr = 'Plano de Contas:\n- Balanço Patrimonial:\n'
        repr += str(self.ativo)
        repr += str(self.passivo)
        repr += str(self.patrimonio_liquido)
        repr += '\n\tTotal Ativo: {:.2f}'.format(self.ativo.get_saldo())
        repr += '\n\tTotal Passivo + Patrimônio Líquido: {:.2f}'.format(
                self.passivo.get_saldo() + self.patrimonio_liquido.get_saldo())
        return repr

from abc import ABC, abstractmethod

from .conta_devedora import ContaDevedora
from .grupo_contas import GrupoContas
from ..natureza import Natureza


class AtivoCirculante(GrupoContas, ABC):
    def __init__(self, parent):
        super().__init__('circulante', 'Circulante', Natureza.DEVEDORA, parent)
        self.init_conta_caixa()

    def init_conta_caixa(self):
        self.add_conta(ContaDevedora('caixa', 'caixa', self))

    def rename_conta_caixa(self, nome):
        self.get_conta('caixa').rename_conta(nome)

    #
    # Assume-se que todas as contas que compoe o grupo de
    # contas de disponibilidades sejam de natureza devedora,
    # ou seja, espera-se que as contas retificadoras nao
    # sejam trazidas neste conjunto.
    #
    @abstractmethod
    def get_contas_disponibilidades(self):
        pass

    def get_saldo_disponibilidades(self):
        return self.get_saldo_contas(self.get_contas_disponibilidades())

    @abstractmethod
    def get_contas_estoques(self):
        pass

    def get_saldo_estoques(self):
        return self.get_saldo_contas(self.get_contas_estoques())

    @abstractmethod
    def init_contas(self):
        pass

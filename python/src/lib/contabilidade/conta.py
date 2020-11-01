from abc import ABC, abstractmethod

from .razonete import Razonete
#
# Incorporar listas de débitos e créditos
# criar atributo para natureza
# criar metodos para adicionar e subtrair o saldo, de acordo com a natureza
#

class Conta(ABC, Razonete):
    def __init__(self, codigo, nome):
        super().__init__()
        self.codigo = codigo
        self.nome = nome

    def get_conta(self, codigo):
        if codigo.lower() == self.codigo.lower():
            return self
        else:
            return None

    def rename_conta(self, nome):
        self.nome = nome

    def is_saldo_equals(self, valor):
        return abs(self.get_saldo() - valor) < 0.00001

    @abstractmethod
    def get_saldo(self):
        pass

    @abstractmethod
    def set_saldo(self, saldo):
        pass

    @abstractmethod
    def increase_saldo(self, lancamento):
        pass

    @abstractmethod
    def decrease_saldo(self, lancamento):
        pass

    def __str__(self):
        repr = '{:s}: {:.2f}'.format(self.nome, self.get_saldo())
        repr += super().__str__()
        return repr

    def __repr__(self):
        repr = "{:s} - {:s}: {:.2f}".format(self.codigo, self.nome, self.get_saldo())
        return repr

    def str_indent(self, level=1):
        str = "\n{:s}{:s}: {:.2f}".format('\t' * level, self.nome, self.get_saldo())
        return str

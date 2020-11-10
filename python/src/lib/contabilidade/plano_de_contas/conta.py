from abc import ABC, abstractmethod

from ..razonete import Razonete


#
# Incorporar listas de débitos e créditos
# criar atributo para natureza
# criar metodos para adicionar e subtrair o saldo, de acordo com a natureza
#
class Conta(ABC, Razonete):
    def __init__(self, codigo, nome, parent=None):
        super().__init__()
        self.codigo = codigo
        self.nome = nome
        self.parent = parent

    def get_conta(self, codigo):
        if codigo.lower() == self.codigo.lower():
            return self
        else:
            return None

    def rename_conta(self, nome):
        self.nome = nome

    def is_saldo_equals(self, valor):
        return abs(self.get_saldo() - valor) < 0.00001

    def get_codigos_ascendentes(self):
        codigos_ascendentes = [grupo_ascendente.codigo for grupo_ascendente in
                self.get_grupos_ascendentes()]
        return codigos_ascendentes

    def get_grupos_ascendentes(self):
        grupos_ascendentes = []
        grupo_ascendente = self.parent

        while grupo_ascendente is not None:
            grupos_ascendentes.append(grupo_ascendente)
            grupo_ascendente = grupo_ascendente.parent

        return grupos_ascendentes

    @abstractmethod
    def get_saldo(self):
        pass

    #
    # * Se a conta apresenta um saldo s1 e se deseja aumentar o saldo
    #   para s2, ou seja, se s1 < s2, então deve-se aumentar o saldo no
    #   valor da subtração de s2 por s1.
    #   OBS: A implementação de como o saldo será aumentado depende
    #        da natureza da conta.
    #
    # * Se a conta apresentar um saldo s1 e se deseja diminuir o saldo,
    #   ou seja, se s1 > s2, então deve-se reduzir o saldo no valor
    #   da subtração de s1 por s2.
    #   OBS: A implementação de como o saldo será reduzido depende
    #        da natureza da conta.
    #
    def set_saldo(self, saldo):
        if not super().is_saldo_equals(saldo):
            comentario = 'Ajuste de saldo para {:.2f}'.format(saldo)
            saldo_atual = self.get_saldo()

            if saldo_atual < saldo:
                valor_ajuste = saldo - saldo_atual
                lancamento = LancamentoContabil(valor=valor_ajuste,
                                                comentario=comentario)
                self.increase_saldo(lancamento)
            else:
                valor_ajuste = saldo_atual - saldo
                lancamento = LancamentoContabil(valor=valor_ajuste,
                                                comentario=comentario)
                self.decrease_saldo(lancamento)

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

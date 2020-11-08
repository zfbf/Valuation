from .conta import Conta


class GrupoContas(Conta):
    def __init__(self, codigo, nome, parent):
        super().__init__(codigo, nome, parent)
        self.contas = []

    def add_conta(self, conta):
        self.contas.append(conta)

    def add_nomes_valores(self, codigos, nomes, valores):
        tuplas = list(zip(codigos, nomes, valores))

        for tupla in tuplas:
            self.add_conta(Conta(tupla[0], tupla[1], tupla[2]))

    def get_conta(self, codigo):
        founded = None

        if codigo.lower() == self.codigo.lower():
            founded = self
        else:
            for conta in self.contas:
                if conta.get_conta(codigo):
                    founded = conta.get_conta(codigo)

        return founded

    def get_saldo(self):
        saldo = 0

        for conta in self.contas:
            saldo += conta.get_saldo()

        return saldo

    #
    # Por default, a utilização deste método é desabilitada
    # para promover a verificação de erros de digitação de
    # balanços fechados de empresas, porém em cenários de
    # simulação, pode-se redefinir este método para criar alguma
    # conta como Outros e fazer com que o valor do passivo se
    # ajuste a um determinado valor sem necessariamente modificar
    # os valores das outras contas componentes do grupo.
    #
    def set_saldo(self, saldo):
        raise TypeError()

    def increase_saldo(self, lancamento):
        raise TypeError()

    def decrease_saldo(self, lancamento):
        raise TypeError()

    def __str__(self):
        return self.str_indent()

    def str_indent(self, level=1):
        str = "\n{:s}{:s}: {:.2f}".format('\t' * level, self.nome, self.get_saldo())

        for conta in self.contas:
            str += '{}'.format(conta.str_indent(level + 1))

        return str

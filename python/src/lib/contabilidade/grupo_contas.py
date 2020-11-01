from src.lib.contabilidade.conta import Conta


class GrupoContas(Conta):
    def __init__(self, codigo, nome, valor=None):
        super().__init__(codigo, nome, valor)
        self.contas = []

    def set_total(self, total):
        self.valor = total

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
                    founded = conta
                    break

        return founded

    @property
    def validate(self):
        is_valid = self.valor == self.get_total()
        return is_valid

    def get_total(self):
        total = 0

        for conta in self.contas:
            total += conta.get_total()

        return total

    def __str__(self):
        return self.str_indent()

    def str_indent(self, level=1):
        str = "\n{:s}{:s}: {:.2f}".format('\t' * level, self.nome, self.valor or 0)

        for conta in self.contas:
            str += '{}'.format(conta.str_indent(level + 1))

        return str




if __name__ == '__main__':
    from src.lib.contabilidade.conta import Conta

    gc1 = GrupoContas('grupo_1', 'Grupo 1', 15.3)
    gc1.add_conta(Conta('conta_1', 'Conta 1', 10.3))
    gc1.add_conta(Conta('conta_2', 'Conta 2', 5))
    print('Validação de contas: {}'.format(gc1.validate))
    print('Total gc1: {}'.format(gc1.get_total()))

    gc2 = GrupoContas('grupo_2', 'Grupo 2', 45.3)
    codigos = ['conta_1', 'conta_2', 'conta_3', 'conta_4']
    nomes = ['Conta 1', 'Conta 2', 'Conta 3', 'Conta 4']
    valores = [10, 10, 10.1, 15.2]
    gc2.add_nomes_valores(codigos, nomes, valores)
    print('Validação de contas: {}'.format(gc2.validate))
    print('Total gc2: {}'.format(gc2.get_total()))
    print(gc2)

    investimentos_2019 = GrupoContas('anc_investimentos', 'Investimentos')

    codigos_grupo_investimentos = [
        'participacao_em_controladas',
        'outros'
    ]

    nomes_grupo_investimentos = [
        'Participação em controladas',
        'Outros'
    ]

    valores_grupo_investimentos_2019 = [
        160970,
        9687
    ]

    investimentos_2019.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2019)

    print('Validação de contas: {}'.format(investimentos_2019.validate))
    print('Total investimentos_2019: {}'.format(investimentos_2019.get_total()))
    print(investimentos_2019)

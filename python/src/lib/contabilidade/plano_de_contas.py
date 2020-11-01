from abc import ABC, abstractmethod
from src.lib.contabilidade.ativo import Ativo


class PlanoDeContas(ABC):
    def __init__(self):
        super().__init__()
        self.ativo = Ativo()
        self.init_contas_ativo_circulante()
        self.init_contas_ativo_nao_circulante()

    @abstractmethod
    def init_contas_ativo_circulante(self):
        pass

    @abstractmethod
    def init_contas_ativo_nao_circulante(self):
        pass

    def add_conta_ativo_circulante(self, conta):
        self.ativo.circulante.add_conta(conta)

    def add_conta_ativo_nao_circulante(self, conta):
        self.ativo.nao_circulante.add_conta(conta)

    def rename_conta_caixa(self, nome):
        self.ativo.circulante.rename_conta_caixa(nome)

    def __str__(self):
        repr = 'Plano de Contas:\n'
        repr += str(self.ativo)
        return repr




if __name__ == '__main__':
    plano_de_contas = PlanoDeContas()
    ativo = Ativo()

    nomes_contas = [
        'Caixa e equivalentes de caixa',
        'Títulos e valores mobiliários',
        'Contas a receber de clientes',
        'Perdas estimadas com créditos de liquidação duvidosa',
        'Estoques',
        'Tributos a recuperar',
        'Despesas antecipadas - partes relacionadas',
        'Despesas antecipadas - terceiros',
        'Outros ativos'
    ]

    for nome_conta in nomes_contas:
        ativo.circulante.add_conta(nome_conta)

    nomes_contas = [
        'Depósitos judiciais',
        'Tributos a recuperar',
        'Outros ativos'
    ]

    for nome_conta in nomes_contas:
        ativo.nao_circulante.add_conta(nome_conta)

    print(plano_de_contas)

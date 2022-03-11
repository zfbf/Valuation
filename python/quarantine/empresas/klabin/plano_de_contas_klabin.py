from src.lib.contabilidade.conta import Conta
from src.lib.contabilidade.plano_de_contas import PlanoDeContas


class PlanoDeContasKlabin(PlanoDeContas):
    def __init__(self):
        super().__init__()

    def init_contas_ativo_circulante(self):
        print("PlanoDeContasKlabin.init_contas_ativo_circulante")
        self.rename_conta_caixa('Caixa e equivalentes de caixa')

        nomes_contas = [
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
            self.add_conta_ativo_circulante(Conta(nome_conta, nome_conta))

    def init_contas_ativo_nao_circulante(self):
        print("PlanoDeContasKlabin.init_contas_ativo_nao_circulante")

        nomes_contas = [
            'Depósitos judiciais',
            'Tributos a recuperar',
            'Outros ativos'
        ]

        for nome_conta in nomes_contas:
            self.add_conta_ativo_nao_circulante(Conta(nome_conta, nome_conta))

    def __str__(self):
        repr = 'Plano de Contas:\n'
        repr += str(self.ativo)
        return repr




if __name__ == '__main__':
    plano_de_contas_klabin = PlanoDeContasKlabin()
    print(plano_de_contas_klabin)

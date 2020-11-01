from src.lib.contabilidade.conta import Conta
from src.lib.contabilidade.plano_de_contas import PlanoDeContas


class PlanoDeContasRef1(PlanoDeContas):
    def __init__(self):
        super().__init__()

    def init_contas_ativo_circulante(self):
        print("PlanoDeContasKlabin.init_contas_ativo_circulante")
        self.rename_conta_caixa('Caixa e equivalentes de caixa')

        parametros_contas = [
            ('titulos_e_valores_mobiliarios', 'Títulos e valores mobiliários'),
            ('contas_a_receber_de_clientes', 'Contas a receber de clientes'),
            ('perdas_estimadas_com_creditos_de_liquidacao_duvidosa', 'Perdas estimadas com créditos de liquidação duvidosa'),
            ('estoques', 'Estoques'),
            ('tributos_a_recuperar', 'Tributos a recuperar'),
            ('despesas_antecipadas_partes_relacionadas', 'Despesas antecipadas - partes relacionadas'),
            ('despesas_antecipadas_terceiros', 'Despesas antecipadas - terceiros'),
            ('outros_ativos', 'Outros ativos')
        ]

        for parametros_conta in parametros_contas:
            self.add_conta_ativo_circulante(Conta(parametros_conta[0], parametros_conta[1]))

    def init_contas_ativo_nao_circulante(self):
        print("PlanoDeContasKlabin.init_contas_ativo_nao_circulante")

        parametros_contas = [
            ('depositos_judiciais', 'Depósitos judiciais'),
            ('tributos_a_recuperar', 'Tributos a recuperar'),
            ('outros_ativos', 'Outros ativos')
        ]

        for parametros_conta in parametros_contas:
            self.add_conta_ativo_nao_circulante(Conta(parametros_conta[0], parametros_conta[1]))

    def __str__(self):
        repr = 'Plano de Contas:\n'
        repr += str(self.ativo)
        return repr




if __name__ == '__main__':
    plano_de_contas = PlanoDeContasRef1()
    print(plano_de_contas)

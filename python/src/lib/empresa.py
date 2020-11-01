import src.lib.utils as utils
from src.lib.contabilidade.ciclo_contabil.ciclo_contabil_anual import CicloContabilAnual

#
# Para facilitar o processo de analise, se faz importante que um objeto :Empresa
# tenha um único plano de contas.   Caso seja desejável analisar as contas sobre
# um outro plano de contas, então um outro objeto seria criado com este outro
# plano de contas.
#


class Empresa:

    def __init__(self, nome):
        super().__init__()
        self.nome = nome
        self.ciclos_contabeis_anuais = []
        self.plano_de_contas = None

    def init_ciclos_contabeis_anuais(self, ano_inicio, ano_fim):
        self.ciclos_contabeis_anuais = [CicloContabilAnual(ano, self.plano_de_contas)
                                        for ano in range(ano_inicio, ano_fim + 1)]

    def get_ciclos_contabeis_anuais(self):
        return self.ciclos_contabeis_anuais

    def get_ciclo_contabil_anual(self, ano):
        ciclo_contabil_anual = None

        for ciclo_contabil_anual in self.ciclos_contabeis_anuais:
            if ciclo_contabil_anual.ano == ano:
                break

        return ciclo_contabil_anual

    # Fazer um refactoring para permitir vários layouts
    def set_layout_contas_ativo_circulante(self, layout_contas_ativo_circulante):
        self.layout_contas_ativo_circulante = layout_contas_ativo_circulante

    def set_layout_contas_ativo_nao_circulante(self, layout_contas_ativo_nao_circulante):
        self.layout_contas_ativo_nao_circulante = layout_contas_ativo_nao_circulante

    def add_balanco_patrimonial(self, balanco_patrimonial):
        self.ciclos_contabeis_anuais.append(balanco_patrimonial)

    def get_valor_conta_ativo_circulante(self, ano:int, codigo_da_conta:str):
        bp = self.get_ciclo_contabil_anual(ano)
        valor = None

        for conta in bp.ativo.circulante.contas:
            if conta.codigo.lower() == codigo_da_conta.lower():
                valor = conta.valor

        return valor

    def get_valor_conta_ativo_nao_circulante(self, ano:int, codigo_da_conta:str):
        bp = self.get_ciclo_contabil_anual(ano)
        valor = None

        for conta in bp.ativo.nao_circulante.contas:
            founded = conta.get_conta(codigo_da_conta)

            if founded:
                valor = founded.valor

        return valor

    def get_valores_conta_ativo_circulante(self, anos, nome_da_conta:str):
        valores = []

        for ano in anos:
            valores.append(self.get_valor_conta_ativo_circulante(ano, nome_da_conta))

        return valores

    def get_valores_conta_ativo_nao_circulante(self, anos, nome_da_conta:str):
        valores = []

        for ano in anos:
            valores.append(self.get_valor_conta_ativo_nao_circulante(ano, nome_da_conta))

        return valores

    def ativo_circulante_to_analise_horizontal(self, ano_final: int, qtd_anos: int):
        linhas_ativo_circulante = dict.fromkeys(self.layout_contas_ativo_circulante, [None] * qtd_anos)

        for nome_da_conta in linhas_ativo_circulante:
            valores = self.get_valores_conta_ativo_circulante(range(ano_final, ano_final - qtd_anos, -1),
                                                              nome_da_conta)
            linhas_ativo_circulante[nome_da_conta] = valores

        return linhas_ativo_circulante

    def ativo_nao_circulante_to_analise_horizontal(self, ano_final: int, qtd_anos: int):
        linhas_ativo_nao_circulante = dict.fromkeys(self.layout_contas_ativo_nao_circulante, [None] * qtd_anos)

        for nome_da_conta in linhas_ativo_nao_circulante:
            valores = self.get_valores_conta_ativo_nao_circulante(
                    range(ano_final, ano_final - qtd_anos, -1),
                    nome_da_conta)
            linhas_ativo_nao_circulante[nome_da_conta] = valores

        return linhas_ativo_nao_circulante




if __name__ == '__main__':
    import sys

    from src.lib.contabilidade.relatorios_contabeis.balanco_patrimonial import BalancoPatrimonial
    from src.lib.contabilidade.grupo_contas import GrupoContas

    sys.path.append(r'/home/zenon/PycharmProjects/Teste')
    sys.path.append(r'/home/zenon/PycharmProjects/Teste/front')
    sys.path.append(r'/home/zenon/PycharmProjects/Teste/front/library')

    klabin = Empresa('Klabin')
    bp_2019 = BalancoPatrimonial(2019)
    klabin.add_balanco_patrimonial(bp_2019)

    investimentos_2019 = GrupoContas('anc_investimentos', 'Investimentos')
    codigos_grupo_investimentos = ['participacao_em_controladas', 'outros']
    nomes_grupo_investimentos = ['Participação em controladas', 'Outros']
    valores_grupo_investimentos_2019 = [160970, 9687]
    investimentos_2019.add_nomes_valores(codigos_grupo_investimentos,
                                         nomes_grupo_investimentos,
                                         valores_grupo_investimentos_2019)

    print('Validação de contas: {}'.format(investimentos_2019.validate))
    print('Total investimentos_2019: {}'.format(investimentos_2019.get_total()))
    print(investimentos_2019)

    bp_2019.ativo.nao_circulante.add_conta(investimentos_2019)
    valor = klabin.get_valor_conta_ativo_nao_circulante(2019, 'participacao_em_controladas')
    print('valor: {:.2f}'.format(valor))




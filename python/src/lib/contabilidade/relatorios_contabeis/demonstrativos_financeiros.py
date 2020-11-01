#
# É importante garantir que cada grupo de demonstrativos
# financeiros siga um único plano de contas e que a
# a especificação do lapso temporal entre os exercícios
# seja especificada para possibilitar o cálculo de
# ajustes a valor presente e possibilitar a
# junção de períodos, como por exemplo a junção dos
# quatro últimos trimestres para representar o YTD.
#

from src.lib.contabilidade.relatorios_contabeis.demonstrativo_financeiro import DemonstrativoFinanceiro


class DemonstrativosFinanceiros:
    def __init__(self, plano_de_contas, ):
        super().__init__()
        self.plano_de_contas = plano_de_contas
        self.demonstrativos_financeiros = []

    def initialize_demonstrativos_anuais(self, ano_inicial, ano_final):
        self.demonstrativos_financeiros.append([
            DemonstrativoFinanceiro(ano) for ano in range(ano_inicial, ano_final + 1)
        ])

    #
    # Deverá ser adicionado um método para adicionar um demonstrativo do tipo YTD
    #


if __name__ == '__main__':
    demonstrativos_financeiros = DemonstrativosFinanceiros(None)
    demonstrativos_financeiros.initialize_demonstrativos_anuais(2014, 2019)
    print('Demonstrativos financeiros: {}'.format(demonstrativos_financeiros))

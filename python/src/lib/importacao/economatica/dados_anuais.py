import os.path
from datetime import datetime

from .dados import EconomaticaDados


#
# Um :CicloContabilAnual representa as movimentações anuais das várias
# contas de um determinado plano de contas em um período de um ano.
# Para haver independência de contas entre ciclos diferentes, é importante
# que o objeto :PlanoDeContas seja único em cada :CicloContabilAnual.
#
class EconomaticaDadosAnuais(EconomaticaDados):
    def __init__(self, nome_empresa, ano_inicial, ano_final):
        super().__init__(nome_empresa)
        self.ano_inicial = ano_inicial
        self.ano_final = ano_final

    def get_dados_dir(self):
        return os.path.abspath('/home/zenon/dev/projects/Valuation/dados')

    def get_identificador(self):
        return '{}_{}_{}'.format(self.nome_empresa,
                                 self.ano_inicial,
                                 self.ano_final)

    def get_data_inicio(self):
        data = datetime(self.ano_inicial, 1, 1)
        return data

    def get_data_fim(self):
        data = datetime(self.ano_final, 12, 31)
        return data

    def get_periodos(self):
        return [str(periodo) for periodo in range(self.ano_inicial, self.ano_final + 1)]

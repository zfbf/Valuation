import os
from datetime import datetime

from .dados import EconomaticaDados


#
# Um :CicloContabilAnual representa as movimentações anuais das várias
# contas de um determinado plano de contas em um período de um ano.
# Para haver independência de contas entre ciclos diferentes, é importante
# que o objeto :PlanoDeContas seja único em cada :CicloContabilAnual.
#
class EconomaticaDadosTrimestraisAnualizados(EconomaticaDados):
    def __init__(self, nome_empresa, ano_inicial, trimestre_inicial, ano_final, trimestre_final):
        super().__init__(nome_empresa)
        self.ano_inicial = ano_inicial
        self.trimestre_inicial = trimestre_inicial
        self.ano_final = ano_final
        self.trimestre_final = trimestre_final

    def get_dados_dir(self):
        dados_dir = os.environ['VALUATION_DADOS_DIR']
        return dados_dir
        #return os.environ.abspath('/home/zenon/dev/projects/Valuation/dados')

    def get_identificador(self):
        return '{}_{}T{}_{}T{}'.format(self.nome_empresa,
                                 self.ano_inicial,
                                 self.trimestre_inicial,
                                 self.ano_final,
                                 self.trimestre_final)

    def get_codigos_periodos(self):
        codigos_trimestres = []
        trimestre = self.trimestre_inicial

        for ano in range(self.ano_inicial, self.ano_final):
            while trimestre <= 4:
                codigos_trimestres.append('{}T{}'.format(ano, trimestre))
                trimestre += 1

            trimestre = 1

        ano = self.ano_final

        for trimestre in range(1, self.trimestre_final + 1):
            codigos_trimestres.append('{}T{}'.format(ano, trimestre))

        return codigos_trimestres

    def __str__(self):
        repr = "\nExercício Social - {:s}".format(self.get_identificador())
        repr += "\n\tInício: {}T{}".format(self.ano_inicial, self.trimestre_inicial)
        repr += "\n\tFinal: {}".format(self.ano_final, self.trimestre_final)
        return repr

    #def get_periodos(self):
        #return [str(periodo) for periodo in range(self.ano_inicial, self.ano_final + 1)]

import os.path
from datetime import datetime

from .dados_anuais import EconomaticaDadosAnuais


class IochpeDadosAnuais(EconomaticaDadosAnuais):
    def __init__(self, ano_inicial, ano_final):
        super().__init__('Iochpe', ano_inicial, ano_final)

    def get_dados_empresa_file_path(self):
        relative_path = '../dados/iochpe/economatica/'
        return os.path.join(super().get_dados_dir(), relative_path)

    def get_dados_empresa_file_name(self):
        return 'economatica_Iochpe_anual_2009-2020.xls'

    def get_sheet_name(self):
        return 'MYPK3'

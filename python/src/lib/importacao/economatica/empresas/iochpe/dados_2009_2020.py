import os.path
from datetime import datetime

from ...dados_anuais import EconomaticaDadosAnuais


class Iochpe20092020(EconomaticaDadosAnuais):
    def __init__(self):
        super().__init__('Iochpe', 'MYPK3', 2009, 2020)

    def get_dados_empresa_file_path(self):
        relative_path = 'economatica/iochpe'
        return os.path.join(super().get_dados_dir(), relative_path)

    def get_dados_empresa_file_name(self):
        return 'economatica_Iochpe_2009-2020.xls'

    def get_sheet_name(self):
        return 'MYPK3'

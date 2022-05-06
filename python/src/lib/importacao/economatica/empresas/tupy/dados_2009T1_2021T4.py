import os.path
from datetime import datetime

from ...dados_trimestrais_anualizados import EconomaticaDadosTrimestraisAnualizados


class Tupy2009T12021T4(EconomaticaDadosTrimestraisAnualizados):
    def __init__(self):
        super().__init__('Tupy', 'TUPY4', 2009, 1, 2021, 4)

    def get_dados_empresa_file_path(self):
        relative_path = 'economatica/tupy/'
        return os.path.join(super().get_dados_dir(), relative_path)

    def get_dados_empresa_file_name(self):
        return 'economatica_Tupy_2009T1-2021T4.xls'

    def get_sheet_name(self):
        return 'TUPY4'

import os.path
from datetime import datetime

from ...dados_trimestrais_anualizados import EconomaticaDadosTrimestraisAnualizados


class Schulz2009T42022T1(EconomaticaDadosTrimestraisAnualizados):
    def __init__(self):
        super().__init__('Schulz', 'SHUL3', 2009, 4, 2022, 1)

    def get_dados_empresa_file_path(self):
        relative_path = 'economatica/schulz/'
        return os.path.join(super().get_dados_dir(), relative_path)

    def get_dados_empresa_file_name(self):
        return 'economatica_Schulz_2009T4-2022T1.xls'

    def get_sheet_name(self):
        return 'SHUL3'

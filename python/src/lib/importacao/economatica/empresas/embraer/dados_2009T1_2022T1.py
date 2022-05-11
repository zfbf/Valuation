import os.path
from datetime import datetime

from ...dados_trimestrais_anualizados import EconomaticaDadosTrimestraisAnualizados


class Embraer2009T12022T1(EconomaticaDadosTrimestraisAnualizados):
    def __init__(self):
        super().__init__('Embraer', 'EMBR4', 2009, 1, 2022, 1)

    def get_dados_empresa_file_path(self):
        relative_path = 'economatica/embraer/'
        return os.path.join(super().get_dados_dir(), relative_path)

    def get_dados_empresa_file_name(self):
        return 'economatica_Embraer_2009T1-2022T1.xls'

    def get_sheet_name(self):
        return 'EMBR4'

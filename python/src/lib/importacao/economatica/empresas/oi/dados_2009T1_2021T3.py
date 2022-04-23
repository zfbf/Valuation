import os.path
from datetime import datetime

from ...dados_trimestrais_anualizados import EconomaticaDadosTrimestraisAnualizados


class Oi2009T12021T3(EconomaticaDadosTrimestraisAnualizados):
    def __init__(self):
        super().__init__('Oi', 'OIBR3', 2009, 1, 2021, 3)

    def get_dados_empresa_file_path(self):
        relative_path = 'economatica/oi/'
        return os.path.join(super().get_dados_dir(), relative_path)

    def get_dados_empresa_file_name(self):
        return 'economatica_Oi_2009T1-2021T3.xls'

    def get_sheet_name(self):
        return 'OIBR3'

from lib.contabilidade.ciclo_contabil.ciclo_contabil_anual_excel_factory import CicloContabilAnualExcelFactory
from .plano_de_contas_dummy import PlanoDeContasDummy


class CicloContabilAnualDummyFactory(CicloContabilAnualExcelFactory):
    def __init__(self):
        super().__init__()

    def get_empty_plano_de_contas(self):
        return PlanoDeContasDummy()

    def get_excel_file_dir(self):
        return '../../dados/dummy/demonstracoes_financeiras/'

    def get_excel_file_name(self):
        return 'Dummy_demonstracoes_financeiras.xlsx'

    def get_excel_columns(self, ano):
        column_mapping = {
            '2019': 'J',
            '2018': 'K',
            '2017': 'L',
            '2016': 'M'
        }

        excel_columns = 'A:G, {}'.format(column_mapping[str(ano)])
        return excel_columns

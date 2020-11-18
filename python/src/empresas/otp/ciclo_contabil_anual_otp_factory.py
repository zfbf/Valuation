from lib.contabilidade.ciclo_contabil.ciclo_contabil_anual_excel_factory import CicloContabilAnualExcelFactory
from .plano_de_contas_otp import PlanoDeContasOtp


class CicloContabilAnualOtpFactory(CicloContabilAnualExcelFactory):
    def __init__(self):
        super().__init__()

    def get_empty_plano_de_contas(self):
        return PlanoDeContasOtp()

    def get_excel_file_dir(self):
        return '../../dados/demonstracoes_financeiras/'

    def get_excel_file_name(self):
        return 'OTP_demonstracoes_financeiras.xlsx'

    def get_excel_columns(self, ano):
        column_mapping = {
            '2019': 'I',
            '2018': 'J',
            '2017': 'K',
            '2016': 'L'
        }

        excel_columns = 'A:G, {}'.format(column_mapping[str(ano)])
        return excel_columns

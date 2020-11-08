import pandas as pd

from .plano_de_contas_otp import PlanoDeContasOtp
from lib.contabilidade.ciclo_contabil.ciclo_contabil_anual import CicloContabilAnual


class OtpCicloContabilAnualFactory:
    def __init__(self):
        super().__init__()
        self.config()

    def config(self):
        self.df_dir = '../../dados/demonstracoes_financeiras/'
        self.df_file = ''
        self.excel_config = {
            'df_dir': '../../dados/demonstracoes_financeiras/',
            'df_file': 'OTP_demonstracoes_financeiras.xlsx',
            'column_mapping': {
                '2019': 'I',
                '2018': 'J',
                '2017': 'K',
                '2016': 'L'
            }
        }

    def read_from_excel(self):
        path = self.excel_config['df_dir'] + self.excel_config['df_file']

        with open(path, 'rb') as excel_file:
            df = pd.read_excel(excel_file,
                               sheet_name='anuais',
                               header=None,
                               index_col=None,
                               usecols='A:F, I',
                               names=['g1', 'g2', 'g3', 'g4',
                                      'codigo', 'nome', 'valor'])

        print(df[10:17])
        print(df.columns)

        conta_df = df[(df['g1'] == 'ativo') &
                      (df['g2'] == 'circulante') &
                      (df['codigo'] == 'caixa')]
        print(conta_df)
        print('conta_df.any(): {}'.format(conta_df.any()))
        return df

    def execute(self):
        print('execute')
        plano_de_contas = PlanoDeContasOtp()
        ciclo_contabil_anual = CicloContabilAnual(2017, plano_de_contas)
        df = self.read_from_excel()

        for conta in plano_de_contas.ativo.contas:
            self.feed_conta(conta, df)



    def feed_conta(self, conta, df):

        print(conta.nome)

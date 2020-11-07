import pandas as pd


class OtpFactory:
    def __init__(self):
        super().__init__()

    def read_from_excel(self):
        path = '../../dados/demonstracoes_financeiras/OTP_demonstracoes_financeiras.xlsx'
        df = pd.read_excel(open(path, 'rb'),
                           sheet_name='anuais',
                           header=None,
                           index_col=None,
                           usecols='A:L')
        print(df)

    def execute(self):
        print('execute')
        self.read_from_excel()

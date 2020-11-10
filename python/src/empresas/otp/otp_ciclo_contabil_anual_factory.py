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

        print(df)
        print(df.columns)
        print('df.any(): {}'.format(df.any()))
        return df

    def execute(self):
        print('execute')
        plano_de_contas = PlanoDeContasOtp()
        ciclo_contabil_anual = CicloContabilAnual(2017, plano_de_contas)
        df = self.read_from_excel()

        ativo = plano_de_contas.ativo
        self.feed_conta(ativo, df)

        #for conta in plano_de_contas.ativo.contas:
        #    self.feed_conta(conta, df)

    def feed_conta(self, conta, df):
        print('feed_conta')
        print(conta)
        codigos_ascendentes = conta.get_codigos_ascendentes()
        print('codigos ascendentes: {}'.format(codigos_ascendentes))

        query = 'codigo == "{}"'.format(conta.codigo)
        for i, codigo_ascendente in enumerate(reversed(codigos_ascendentes), start=1):
            query += ' & g{} == "{}"'.format(i, codigo_ascendente)

        #conta_df = df[(df['g1'] == get_codigos_ascendentes[0]) &
        #              (df['g2'] == 'circulante') &
        #              (df['codigo'] == 'caixa')]

        print('query: {}'.format(query))
        conta_df = df.query(query)
        print(conta_df)
        print('type(conta_df): {}'.format(type(conta_df)))
        print('conta_df.shape: {}'.format(conta_df.shape))
        print('conta_df.shape[0]: {}'.format(conta_df.shape[0]))
        print('type(conta_df.shape[0]): {}'.format(type(conta_df.shape[0])))

        if conta_df.shape[0] > 0:
            print('type(conta_df.iloc[0]["valor"]): {}'.format(type(conta_df.iloc[0]["valor"])))
            valor = conta_df.iloc[0]["valor"]

            try:
                conta.set_saldo(valor)
            except TypeError:
                conta.valor_verificacao = valor

        print(conta)

        for child in conta.contas:
            self.feed_conta(child, df)

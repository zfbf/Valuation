import pandas as pd

from .plano_de_contas_otp import PlanoDeContasOtp
from lib.contabilidade.ciclo_contabil.ciclo_contabil_anual import CicloContabilAnual


class CicloContabilAnualOtpFactory:
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
                               usecols='A:G, J',
                               names=['df', 'g1', 'g2', 'g3', 'g4',
                                      'codigo', 'nome', 'valor'])

        print(df)
        print(df.columns)
        print('df.any(): {}'.format(df.any()))
        return df

    def execute(self):
        plano_de_contas = PlanoDeContasOtp()
        ciclo_contabil_anual = CicloContabilAnual(2017, plano_de_contas)
        df = self.read_from_excel()
        self.feed_conta_postorder(plano_de_contas.ativo, df)
        self.feed_conta_postorder(plano_de_contas.passivo, df)
        self.feed_conta_postorder(plano_de_contas.patrimonio_liquido, df)
        return plano_de_contas

    def feed_conta_postorder(self, conta, df):
        try:
            for child in conta.contas:
                self.feed_conta_postorder(child, df)
        except Exception:
            pass

        self.feed_conta(conta, df)

    def feed_conta(self, conta, df):
        codigos_ascendentes = conta.get_codigos_ascendentes()
        query = 'df == "balanco_patrimonial"'
        query += ' & codigo == "{}"'.format(conta.codigo)

        for i, codigo_ascendente in enumerate(reversed(codigos_ascendentes), start=1):
            query += ' & g{} == "{}"'.format(i, codigo_ascendente)

        conta_df = df.query(query)

        if conta_df.shape[0] > 0:
            valor = conta_df.iloc[0]["valor"]

            if pd.isnull(valor):
                print('#feed_conta, conta.codigo: {}'.format(conta.codigo))
                print('\n\tquery: {}'.format(query))
                print('\n\tconta_df: {}'.format(conta_df))
                print('\n\tconta_df.shape: {}'.format(conta_df.shape))
                print('\n\tvalor: {}'.format(valor))
            else:
                try:
                    conta.set_saldo(valor)
                except TypeError:
                    conta.valor_verificacao = valor
                    print(conta)

        if conta.codigo == 'passivos_rel_ativos_nao_circulantes_mantidos_para_negociacao':
            print('#feed_conta, conta.codigo: {}'.format(conta.codigo))
            print('\n\tquery: {}'.format(query))
            print('\n\tconta_df: {}'.format(conta_df))
            print('\n\tconta_df.shape: {}'.format(conta_df.shape))
            print('\n\tconta.valor_verificacao: {}'.format(conta.valor_verificacao))

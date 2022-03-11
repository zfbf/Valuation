from abc import abstractmethod
from os import path
import pandas as pd

from .ciclo_contabil_anual_factory import CicloContabilAnualFactory


class CicloContabilAnualExcelFactory(CicloContabilAnualFactory):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def get_excel_file_dir(self):
        pass

    @abstractmethod
    def get_excel_file_name(self):
        pass

    @abstractmethod
    def get_excel_columns(self, ano):
        pass

    def feed_plano_de_contas(self, plano_de_contas, ano):
        df = self.read_from_excel(ano)
        self.feed_conta_postorder(plano_de_contas.ativo, df)
        self.feed_conta_postorder(plano_de_contas.passivo, df)
        self.feed_conta_postorder(plano_de_contas.patrimonio_liquido, df)

    def read_from_excel(self, ano):
        file_path = path.join(self.get_excel_file_dir(),
                self.get_excel_file_name())
        
        with open(file_path, 'rb') as excel_file:
            df = pd.read_excel(excel_file,
                               sheet_name='anuais',
                               header=None,
                               index_col=None,
                               usecols=self.get_excel_columns(ano),
                               names=['df', 'g1', 'g2', 'g3', 'g4',
                                      'codigo', 'nome', 'valor'])

        #print(df)
        #print(df.columns)
        #print('df.any(): {}'.format(df.any()))
        return df

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
                #print('#feed_conta, conta.codigo: {}'.format(conta.codigo))
                #print('\n\tquery: {}'.format(query))
                #print('\n\tconta_df: {}'.format(conta_df))
                #print('\n\tconta_df.shape: {}'.format(conta_df.shape))
                #print('\n\tvalor: {}'.format(valor))
                pass
            else:
                try:
                    conta.set_saldo(valor)
                except TypeError:
                    conta.valor_verificacao = valor
                    #print(conta)

        #if conta.codigo == 'passivos_rel_ativos_nao_circulantes_mantidos_para_negociacao':
        #    print('#feed_conta, conta.codigo: {}'.format(conta.codigo))
        #    print('\n\tquery: {}'.format(query))
        #    print('\n\tconta_df: {}'.format(conta_df))
        #    print('\n\tconta_df.shape: {}'.format(conta_df.shape))
        #    print('\n\tconta.valor_verificacao: {}'.format(conta.valor_verificacao))

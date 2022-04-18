import os.path

import pandas as pd
import numpy as np

from abc import ABC, abstractmethod


class EconomaticaDados(ABC):
    def __init__(self, nome_empresa):
        super().__init__()
        self.nome_empresa = nome_empresa

    @abstractmethod
    def get_identificador(self):
        pass

    @abstractmethod
    def get_codigos_periodos(self):
        pass

    def import_from_excel(self):
        dados_empresa_file_name = os.path.join(self.get_dados_empresa_file_path(),
                                               self.get_dados_empresa_file_name())
        rows_to_skip = {}
        codigos = ['codigo_{}'.format(i) for i in range(8)]
        column_names = codigos + ['conta'] + self.get_codigos_periodos()

        with open(dados_empresa_file_name, 'rb') as dados_empresa_file:
            df = pd.read_excel(dados_empresa_file,
                               sheet_name=self.get_sheet_name(),
                               names=column_names,
                               #usecols='A:BI',
                               skiprows=range(1, 8))

        return df

    def prepare(self):
        multi_index = ['codigo_0', 'codigo_1', 'codigo_2', 'codigo_3',
                       'codigo_4', 'codigo_5', 'codigo_6', 'codigo_7']
        aux_df = self.import_from_excel().set_index(multi_index).sort_index()
        aux_index = aux_df.index.dropna(how='all')
        self.df = aux_df.loc[aux_index]
        self.df.sort_index(inplace=True)

    def query(self, codigos):
        result = self.df.loc[codigos, :]
        return result

    def get_valor(self, index, codigo_periodo):
        #print('Dentro de EconomaticaDados.get_valor()')
        #print('index: {}, codigo_periodo: <{}>'.format(index, codigo_periodo))
        valor = None

        try:
            valor = self.df.loc[index, codigo_periodo].values[-1]
        except:
            pass
        finally:
            return valor

    def read_row():
        fs = '{} \t& {} \t& {} \t& {} \t& {} \t& {} \t& {} \\\\'

        for i in range(len(df)):
            s = fs.format(df.at[i, 'Ano'],
                          table_latex_number_formatter(df.at[i, 'REM_EUA']),
                          table_latex_number_formatter(df.at[i, 'DES_EUA']),
                          table_latex_number_formatter(df.at[i, 'REM_CAN']),
                          table_latex_number_formatter(df.at[i, 'DES_CAN']),
                          table_latex_number_formatter(df.at[i, 'REM_RU']),
                          table_latex_number_formatter(df.at[i, 'DES_RU']))
            print(s)

    def get_project_path(self):
        return os.path.abspath(os.path.dirname(''))

    @abstractmethod
    def get_dados_empresa_file_path(self):
        pass

    @abstractmethod
    def get_dados_empresa_file_name(self):
        pass

    @abstractmethod
    def get_sheet_name(self):
        pass

    def __str__(self):
        repr = "\nExercício Social - {:s}".format(self.get_identificador())
        repr += "\n\tInício: {}".format(self.get_data_inicio().strftime('%d/%m/%Y'))
        repr += "\n\tInício: {}".format(self.get_data_fim().strftime('%d/%m/%Y'))
        return repr

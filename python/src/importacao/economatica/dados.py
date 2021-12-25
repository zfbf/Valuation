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
    def get_data_inicio(self):
        pass

    @abstractmethod
    def get_data_fim(self):
        pass

    def import_from_excel(self):
        dados_empresa_file = os.path.join(self.get_dados_empresa_file_path(),
                                          self.get_dados_empresa_file_name())
        rows_to_skip = {}
        df = pd.read_excel(open(dados_empresa_file, 'rb'),
                                sheet_name=self.get_sheet_name(),
                                names=['Conta'] + [str(ano) for ano in range(2009, 2021)],
                                usecols='A, B, C, D, E, F, G, H, I, J, K, L, M',
                                skiprows=range(1, 8))
                                #dtype={'ret_Cemig': float, 'ret_Bovespa': int, 'ret_Dow_Jones': int},
                                #skiprows=[0],
                                #nrows=36)
        return df

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
        repr += "\n\tPlano de Contas: {}".format(self.plano_de_contas)
        return repr

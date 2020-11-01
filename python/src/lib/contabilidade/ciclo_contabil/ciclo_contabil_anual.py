from datetime import datetime

from lib.contabilidade.ciclo_contabil.ciclo_contabil import CicloContabil


class CicloContabilAnual(CicloContabil):
    def __init__(self, ano, plano_de_contas, identificador):
        super().__init__(plano_de_contas)
        self.ano = ano
        self.identificador = identificador

    def get_identificador(self):
        return self.identificador if self.identificador else str(self.ano)

    def get_data_inicio(self):
        data = datetime(self.ano, 1, 1)
        return data

    def get_data_fim(self):
        data = datetime(self.ano, 12, 31)
        return data




if __name__ == '__main__':
    es = CicloContabilAnual(2020, None, None)
    print(es)

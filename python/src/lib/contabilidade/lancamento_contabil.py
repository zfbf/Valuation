from datetime import datetime


#
# A ideia do :LancamentoContabil consiste em poder usar nos lançamentos
# de débito e crédito das contas individuais e poder ordenar por ordem
# cronológica os vários lançamentos e poder calcular os saldos em qualquer
# ponto da linha do tempo.
#
class LancamentoContabil:
    def __init__(self, valor, ano=None, mes=None, dia=None, comentario=None):
        super().__init__()
        self.valor = valor
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.comentario = comentario

    def get_data(self):
        data = None

        if self.ano and self.mes and self.dia:
            data = datetime(self.ano, self.mes, self.dia)

        return data

    def __str__(self):
        repr = "{:.2f}".format(self.valor)

        if self.get_data():
            repr += " ({})".format(self.get_data().strftime('%d/%m/%Y'))

        return repr

from datetime import datetime
from functools import reduce

from ..contabilidade.lancamento_contabil import LancamentoContabil


class PartidaDobrada:
    def __init__(self, ano=None, mes=None, dia=None, comentario=None):
        super().__init__()
        self.ano = ano
        self.mes = mes
        self.dia = dia
        self.comentario = comentario
        self.debitos = []
        self.creditos = []

    def get_data(self):
        data = None

        if self.ano and self.mes and self.dia:
            data = datetime(self.ano, self.mes, self.dia)

        return data

    def add_debito(self, debito):
        self.debitos.append(debito)

    def add_debitos(self, debitos):
        for debito in debitos:
            self.debitos.append(debito)

    def add_credito(self, credito):
        self.creditos.append(credito)

    def add_creditos(self, creditos):
        for credito in creditos:
            self.creditos.append(credito)

    def get_total_debitos(self):
        total_debitos = 0

        if len(self.debitos) == 1:
            total_debitos = self.debitos[0].valor
        elif len(self.debitos) > 1:
            total_debitos = reduce((lambda x, y: x.valor + y.valor), self.debitos)

        return total_debitos

    def get_total_creditos(self):
        total_creditos = 0

        if len(self.creditos) == 1:
            total_creditos = self.creditos[0].valor
        elif len(self.creditos) > 1:
            total_creditos = reduce((lambda x, y: x.valor + y.valor), self.creditos)

        return total_creditos

    def execute(self):
        pass

    def is_valid(self):
        diferenca = self.get_total_creditos() - self.get_total_creditos()
        return abs(diferenca) < .00001

    def __str__(self):
        repr = 'Partida Dobrada - '

        if self.get_data():
            repr += self.get_data().strftime('%d/%m/%Y')

        repr += '\n\tTotal de débitos: {:.2f}\n\tTotal de créditos: {:.2f}'.format(
                self.get_total_debitos(),
                self.get_total_creditos())
        repr += '\n\tis_valid: {}'.format(self.is_valid())

        return repr

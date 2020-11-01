from datetime import datetime


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




if __name__ == '__main__':
    lc1 = LancamentoContabil(10)
    print(lc1)

    lc2 = LancamentoContabil(20, 2020, 10, 18)
    print(lc2)

    print('type(lc1): {}'.format(type(lc1)))
    print('type(lc1.valor): {}'.format(type(lc1.valor)))

    lcs = [lc1, lc2]
    print('type(lcs): {}'.format(type(lcs)))

    from functools import reduce

    total = reduce((lambda x, y: x.valor + y.valor), lcs)
    print('type(total): {}'.format(type(total)))
    print('total: {}'.format(total))


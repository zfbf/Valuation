from .conta import Conta
from ..lancamento_contabil import LancamentoContabil
#
# Incorporar listas de débitos e créditos
# criar atributo para natureza
# criar metodos para adicionar e subtrair o saldo, de acordo com a natureza
#

class ContaDevedora(Conta):
    def __init__(self, codigo, nome, parent):
        super().__init__(codigo, nome, parent)
        self.codigo = codigo
        self.nome = nome

    def get_saldo(self):
        return super().get_total_debitos() - super().get_total_creditos()

    #
    # * Se a conta devedora tem saldo s1 e se deseja aumentar o saldo
    #   para s2, ou seja, se s1 < s2, então deve-se lançar um débito no
    #   valor da subtração de s2 por s1.
    #
    # * Se a conta devedora tem saldo s1 e se deseja diminuir o saldo,
    #   ou seja, se s1 > s2, então deve-se lançar um crédito no valor
    #   da subtração de s1 por s2.
    #
    def set_saldo(self, saldo):
        if not super().is_saldo_equals(saldo):
            comentario = 'Ajuste de saldo para {:.2f}'.format(saldo)
            saldo_atual = self.get_saldo()

            if saldo_atual < saldo:
                valor_ajuste = saldo - saldo_atual
                lancamento = LancamentoContabil(valor=valor_ajuste,
                                                comentario=comentario)
                self.increase_saldo(lancamento)
            else:
                valor_ajuste = saldo_atual - saldo
                lancamento = LancamentoContabil(valor=valor_ajuste,
                                                comentario=comentario)
                self.decrease_saldo(lancamento)

    def increase_saldo(self, lancamento):
        super().add_debito(lancamento)

    def decrease_saldo(self, lancamento):
        super().add_credito(lancamento)

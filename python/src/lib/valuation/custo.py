from abc import ABC, abstractmethod

#
# Cálculo do ROIC:
#   https://www.treasy.com.br/blog/retorno-sobre-o-capital-investido-roic/
#

#TODO: Implementar WACC
#      - criar passos para calcular o WACC
# OBS: WACC não precisa guardar o nome da empresa.
# Pode-se tornar esta classe abstrata e implementar
# WaccTrimestral e WaccAnual

class Custo(ABC):
    def __init__(self, periodo_contabil):
        super().__init__()
        self.periodo_contabil = periodo_contabil

    def get_ano(self):
        return self.periodo_contabil.ano

    def get_dividas_onerosas(self):
        passivo = self.periodo_contabil.bp_ifrs.passivo
        dvd_onerosas_cp = passivo.circulante.get_conta(
                'emprestimos_e_financiamentos')
        dvd_onerosas_lp = passivo.nao_circulante.get_conta(
                'emprestimos_e_financiamentos')
        dvd_onerosas = dvd_onerosas_cp.get_saldo() + dvd_onerosas_lp.get_saldo()
        return dvd_onerosas

    def get_despesas_financeiras(self):
        resultado_financeiro = self.periodo_contabil.dre.resultado_financeiro
        despesas_financeiras = resultado_financeiro.get_conta('despesas_financeiras')
        return despesas_financeiras.get_saldo()

    def get_kd(self):
        print('Dentro de get_kd')
        dividas_onerosas = self.get_dividas_onerosas()
        despesas_financeiras = self.get_despesas_financeiras()
        kd = despesas_financeiras / dividas_onerosas
        print('kd: {}'.format(kd))
        return kd

    def get_ke(self):
        return -1

    def get_wacc(self):
        return -1

    def get_ebit(self):
        return self.periodo_contabil.dre.lajir

    # A ideia desse método é dar flexibilidade ao usuário
    # de usar os objetor que o convém sem provocar acoplamento.
    # Exemplo: Se o usuário desejar usar algum DataFrame, ele poderá
    # usar sem que essa classe tenha conhecimento deste objeto, bastando
    # que ele passe um objeto que tenha a interface report()
    def report(self, reporter):
        return reporter.execute(self)

    def __str__(self):
        lines = [
            'Custo:',
            'Dívidas onerosas: {}',
            'Despesas financeiras: {}',
            'Kd: {}',
            'Ke: {}',
            'Wacc: {}',
            'EBIT: {}',
            'ano: {}'
        ]

        repr = '\n\t'.join(lines).format(
            self.get_dividas_onerosas(),
            self.get_despesas_financeiras(),
            self.get_kd(),
            self.get_ke(),
            self.get_wacc(),
            self.get_ebit(),
            self.get_ano()
        )

        repr += self.str_comp()
        return repr

    @abstractmethod
    def str_comp(self):
        pass

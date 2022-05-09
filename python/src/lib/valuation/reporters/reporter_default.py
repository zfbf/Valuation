from .reporter import Reporter
from ...contabilidade.periodo_contabil import PeriodoContabil


class ReporterDefault(Reporter):
    def __init__(self):
        super().__init__('Default')

    def execute(self, valuation):
        report = []

        periodos = valuation.get_periodos()
        identificadores = []
        ativo_valores = []
        ativo_circulante_valores = []
        ativo_nao_circulante_valores = []
        ativo_verificacao_saldos = []

        for periodo in periodos:
            identificadores.append(periodo.identificador)
            bp_ifrs = periodo.bp_ifrs
            ativo = bp_ifrs.ativo
            ativo_valores.append(ativo.get_saldo())
            ativo_circulante = ativo.circulante
            ativo_circulante_valores.append(ativo_circulante.get_saldo())
            ativo_nao_circulante = ativo.nao_circulante
            ativo_nao_circulante_valores.append(ativo_nao_circulante.get_saldo())
            ativo_verificacao_saldos.append(ativo.verificar_saldo())

        report.append(identificadores)
        report.append(ativo_valores)
        report.append(ativo_circulante_valores)
        report.append(ativo_nao_circulante_valores)
        report.append(ativo_verificacao_saldos)

        #periodo_contabil
        #print('type(report): {}'.format(type(report)))
        #print('len(report): {}'.format(len(report)))
        #print('report: {}'.format(report))

        return report

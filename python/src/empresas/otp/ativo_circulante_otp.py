from lib.contabilidade.plano_de_contas.ativo_circulante import AtivoCirculante
from lib.contabilidade.plano_de_contas.conta_devedora import ContaDevedora



class AtivoCirculanteOtp(AtivoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def get_contas_disponibilidades(self):
        return [self.get_conta('caixa')]

    def init_contas(self):
        aux = (('aplicacoes_financeiras', 'Aplicações financeiras'),
               ('contas_a_receber', 'Contas a receber'),
               ('partes_relacionadas', 'Partes relacionadas'),
               ('tributos_a_recuperar', 'Tributos a recuperar'),
               ('despesas_antecipadas', 'Despesas antecipadas'),
               ('outros', 'Outros ativos'),
               ('ativos_nao_circulantes_mantidos_para_negociacao',
                    'Ativos não circulantes mantidos para negociação'))

        for pars in aux:
            self.add_conta(ContaDevedora(pars[0], pars[1]))

        self.rename_conta_caixa('Caixa e equivalentes de caixa')

from lib.contabilidade.plano_de_contas.passivo_circulante import PassivoCirculante
from lib.contabilidade.plano_de_contas.conta_credora import ContaCredora



class PassivoCirculanteOtp(PassivoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def get_contas_disponibilidades(self):
        return [self.get_conta('caixa')]

    def init_contas(self):
        aux = (('emp_financ_debentures',
                    'Empréstimos, financiamentos e debêntures'),
               ('arrendamento_mercantil', 'Arrendamento mercantil'),
               ('fornecedores', 'Fornecedores'),
               ('obrigacoes_sociais_e_trabalhistas',
                    'Obrigações sociais e trabalhistas'),
               ('impostos_taxas_e_contribuições_sociais',
                    'Impostos, taxas e contribuições sociais'),
               ('outros', 'Outros passivos'),
               ('passivos_rel_ativos_nao_circulantes_mpn',
                    'Passivos relacionados a ativos não circulantes mantidos para negociação'))

        for pars in aux:
            self.add_conta(ContaCredora(pars[0], pars[1]))

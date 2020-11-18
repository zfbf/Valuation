from lib.contabilidade.plano_de_contas.passivo_nao_circulante import PassivoNaoCirculante
from lib.contabilidade.plano_de_contas.conta_credora import ContaCredora
from lib.contabilidade.plano_de_contas.grupo_contas import GrupoContas
from lib.contabilidade.natureza import Natureza


class PassivoNaoCirculanteOtp(PassivoNaoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def init_contas(self):
        aux = (('emp_financ_debentures',
                    'Empréstimos, financiamentos e debêntures'),
               ('arrendamento_mercantil', 'Arrendamento mercantil'),
               ('fornecedores', 'Fornecedores'),
               ('partes_relacionadas', 'Partes relacionadas'),
               ('prov_civeis_trabalhistas_e_previdenciarias',
                    'Provisões cíveis, trabalhistas e previdenciárias'),
               ('prov_conserva_especial', 'Provisão para conserva especial'),
               ('outros', 'Outros passivos'))

        for pars in aux:
            self.add_conta(ContaCredora(pars[0], pars[1]))

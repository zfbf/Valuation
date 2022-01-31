from ..passivo_nao_circulante import PassivoNaoCirculante
from ..conta_credora import ContaCredora
from ..grupo_contas import GrupoContas
from ...natureza import Natureza


class PassivoNaoCirculanteDefault(PassivoNaoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def init_contas(self):
        aux = (('emp_financ_debentures',
                    'Empréstimos, financiamentos e debêntures'),
               ('arrendamento_mercantil', 'Arrendamento mercantil'),
               ('fornecedores', 'Fornecedores'),
               ('partes_relacionadas', 'Partes relacionadas'),
               ('credor_pela_aquisicao_da_concessao',
                    'Credor pela aquisição da concessão'),
               ('prov_civeis_trabalhistas_e_previdenciarias',
                    'Provisões cíveis, trabalhistas e previdenciárias'),
               ('prov_conserva_especial', 'Provisão para conserva especial'),
               ('outros', 'Outros passivos'))

        for pars in aux:
            self.add_conta(ContaCredora(pars[0], pars[1]))

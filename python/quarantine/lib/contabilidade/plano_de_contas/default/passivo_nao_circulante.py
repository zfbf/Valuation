from ..passivo_nao_circulante import PassivoNaoCirculante
from ..conta_credora import ContaCredora
from ..grupo_contas import GrupoContas
from ...natureza import Natureza


class PassivoNaoCirculanteDefault(PassivoNaoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def init_contas(self):
        contas = (('impostos_diferidos', 'Impostos Diferidos'),
                  ('provisoes', 'Provisões'),
                  ('lucros_e_receitas_a_apropriar', 'Lucros e Receitas a Apropriar'))

        for conta in contas:
            self.add_conta(ContaCredora(conta[0], conta[1]))

        emp_e_fin = GrupoContas('emprestimos_e_financiamentos',
                                'Empréstimos e Financiamentos',
                                Natureza.CREDORA,
                                self)

        self.add_conta(emp_e_fin)

        financiamentos = GrupoContas('financiamentos',
                                     'Financiamentos',
                                     Natureza.CREDORA,
                                     self)

        emp_e_fin.add_conta(financiamentos)

        contas = (('nacional', 'Nacional'),
                  ('estrangeiro', 'Estrangeiro'))

        for conta in contas:
            financiamentos.add_conta(ContaCredora(conta[0], conta[1]))

        contas = (('debentures', 'Debêntures'),
                  ('arrendamento_financeiro', 'Arrendamento Financeiro'))

        for conta in contas:
            emp_e_fin.add_conta(ContaCredora(conta[0], conta[1]))

        outras_obrig = GrupoContas('outras_obrigacoes',
                                   'Outras Obrigações',
                                   Natureza.CREDORA,
                                   self)

        self.add_conta(outras_obrig)
        contas = (('partes_relacionadas', 'Partes Relacionadas'),
                  ('outros_lp', 'Outros'))

        for conta in contas:
            outras_obrig.add_conta(ContaCredora(conta[0], conta[1]))

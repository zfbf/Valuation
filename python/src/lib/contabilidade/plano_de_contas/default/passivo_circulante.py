from ..passivo_circulante import PassivoCirculante
from ..conta_credora import ContaCredora
from ..grupo_contas import GrupoContas
from ...natureza import Natureza


class PassivoCirculanteDefault(PassivoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def init_contas(self):
        contas = (('obrigacoes_sociais', 'Obrigações Sociais'),
                  ('fornecedores', 'Fornecedores'),
                  ('impostos_a_pagar', 'Impostos a Pagar'),
                  ('provisoes', 'Provisões'))

        for conta in contas:
            self.add_conta(ContaCredora(conta[0], conta[1]))

        emp_e_fin = GrupoContas('emprestimos_e_financiamentos',
                                'Empréstimos e Financiamentos',
                                Natureza.CREDORA,
                                self)

        self.add_conta(emp_e_fin)

        contas = (('financiamentos', 'Financiamentos'),
                  ('debentures', 'Debêntures'),
                  ('arrendamento_financeiro', 'Arrendamento Financeiro'))

        for conta in contas:
            emp_e_fin.add_conta(ContaCredora(conta[0], conta[1]))

        outras_obrig = GrupoContas('outras_obrigacoes',
                                   'Outras Obrigações',
                                   Natureza.CREDORA,
                                   self)

        self.add_conta(outras_obrig)
        contas = (('partes_relacionadas', 'Partes Relacionadas'))

        outras_obrig_outros = GrupoContas('outros_cp',
                                          'Outros',
                                          Natureza.CREDORA,
                                          self)

        outras_obrig.add_conta(outras_obrig_outros)
        contas = (('dividendos', 'Dividendos'),
                  ('outros', 'Outros'))

        for conta in contas:
            outras_obrig_outros.add_conta(ContaCredora(conta[0], conta[1]))

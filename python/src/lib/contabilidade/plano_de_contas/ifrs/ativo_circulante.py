from ..ativo_circulante import AtivoCirculante
from ..conta_devedora import ContaDevedora


class AtivoCirculanteIFRS(AtivoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def get_contas_disponibilidades(self):
        return [self.get_conta_caixa(),
                self.get_conta('aplicacoes_financeiras')]

    def get_contas_estoques(self):
        return [self.get_conta('estoques')]

    def init_contas(self):
        self.rename_conta_caixa('Caixa e equivalentes de caixa')

        aux = (('aplicacoes_financeiras', 'Aplicações financeiras'),
               ('contas_a_receber', 'Contas a receber'),
               ('estoques', 'Estoques'),
               ('ativos_biologicos', 'Ativos Biológicos'),
               ('impostos_a_recuperar', 'Impostos a recuperar'),
               ('despesas_antecipadas', 'Despesas antecipadas'),
               ('outros', 'Outros ativos'))

        for pars in aux:
            self.add_conta(ContaDevedora(pars[0], pars[1]))
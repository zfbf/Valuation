from ..ativo_nao_circulante import AtivoNaoCirculante
from ..conta_devedora import ContaDevedora
from ..grupo_contas import GrupoContas
from ...natureza import Natureza


class AtivoNaoCirculanteDefault(AtivoNaoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def init_contas(self):
        realizavel_lp = GrupoContas('realizavel_lp',
                                    'Realizável a Longo Prazo',
                                    Natureza.DEVEDORA,
                                    self)

        self.add_conta(realizavel_lp)

        contas = (('aplicacao_financeira_valor_justo',
                        'Aplicação financeira a valor justo'),
                  ('aplicacao_financeira_custo_amortizado',
                        'Aplicação financeira a custo amortizado'),
                  ('contas_a_receber', 'Contas a receber'),
                  ('estoques', 'Estoques'),
                  ('ativos_biologicos', 'Ativos biológicos'),
                  ('impostos_diferidos', 'Impostos diferidos'),
                  ('despesas_antecipadas', 'Despesas antecipadas'),
                  ('partes_relacionadas', 'Partes relacionadas'),
                  ('outros', 'outros'))

        for conta in contas:
            realizavel_lp.add_conta(ContaDevedora(conta[0], conta[1]))

        contas = (('investimentos', 'Investimentos'),
                  ('imobilizado', 'Imobilizado'))

        for conta in contas:
            self.add_conta(ContaDevedora(conta[0], conta[1]))

        intangiveis_liquido = GrupoContas('intangiveis_liquido',
                                          'Intangíveis líquido',
                                          Natureza.DEVEDORA,
                                          self)

        self.add_conta(intangiveis_liquido)

        contas = (('intangiveis', 'Intangíveis'),
                  ('goodwill', 'Goodwill'))

        for conta in contas:
            intangiveis_liquido.add_conta(ContaDevedora(conta[0], conta[1]))

    def get_conta_realizavel_a_longo_prazo(self):
        return self.get_conta('realizavel_lp')

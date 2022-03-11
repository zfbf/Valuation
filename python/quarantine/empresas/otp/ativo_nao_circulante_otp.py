from lib.contabilidade.plano_de_contas.ativo_nao_circulante import AtivoNaoCirculante
from lib.contabilidade.plano_de_contas.conta_devedora import ContaDevedora
from lib.contabilidade.plano_de_contas.grupo_contas import GrupoContas
from lib.contabilidade.natureza import Natureza


class AtivoNaoCirculanteOtp(AtivoNaoCirculante):
    def __init__(self, parent):
        super().__init__(parent)

    def init_contas(self):
        realizavel_a_longo_prazo = GrupoContas('realizavel_a_longo_prazo',
                'Realizável a longo prazo', Natureza.DEVEDORA,
                 self)

        aux = (('mantidos_para_negociacao',
                    'Ativos não circulantes mantidos para negociação'),
               ('aplicacoes_financeiras', 'Aplicações financeiras'),
               ('contas_a_receber', 'Contas a receber'),
               ('partes_relacionadas', 'Partes relacionadas'),
               ('depositos_judiciais', 'Depósitos judiciais'),
               ('ir_e_cs_diferidos',
                    'Imposto de renda e contribuição social diferidos'),
               ('outros', 'Outros ativos'))

        for pars in aux:
            realizavel_a_longo_prazo.add_conta(ContaDevedora(
                    pars[0], pars[1], self))

        self.add_conta(realizavel_a_longo_prazo)
        aux = (('investimentos', 'Investimentos'),
               ('imobilizado', 'Imobilizado'),
               ('intangivel', 'Intangível'))

        for pars in aux:
            self.add_conta(ContaDevedora(pars[0], pars[1]))

    def get_conta_realizavel_a_longo_prazo(self):
        return self.get_conta('realizavel_a_longo_prazo')

from lib.contabilidade.plano_de_contas.patrimonio_liquido import PatrimonioLiquido
from lib.contabilidade.plano_de_contas.conta_credora import ContaCredora


class PatrimonioLiquidoDummy(PatrimonioLiquido):
    def __init__(self):
        super().__init__()

    def init_contas(self):
        aux = (('capital_social', 'Capital social'),
               ('reservas_de_capital', 'Reservas de capital'),
               ('ajustes_de_avaliacao_patrimonial',
                    'Ajustes de avaliação patrimonial'),
               ('prejuizos_acumulados', 'Prejuízos acumulados'),
               ('particip_acionistas_n_controladores',
                    'Participação dos acionistas não controladores'),
               ('particip_acionistas_n_controladores_em_ativos_mantidos_para_negociacao',
                     'Participação dos acionistas não controladores em ativos mantidos para negociação'))

        for pars in aux:
            self.add_conta(ContaCredora(pars[0], pars[1]))

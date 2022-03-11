from ..patrimonio_liquido import PatrimonioLiquido
from ..conta_credora import ContaCredora


class PatrimonioLiquidoDefault(PatrimonioLiquido):
    def __init__(self):
        super().__init__()

    def init_contas(self):
        contas = (('capital_social', 'Capital social'),
                  ('reservas_de_capital', 'Reservas de capital'),
                  ('reservas_de_reavaliacao', 'Reservas de Reavaliação'),
                  ('reservas_de_lucros', 'Reservas de Lucros'),
                  ('lucros_acumulados', 'Lucros acumulados'),
                  ('ajustes_avaliacao_patrimonial',
                        'Ajustes Avaliação Patrimonial'),
                  ('ajustes_acumulados_conversao',
                        'Ajustes Acumulados Conversão'),
                  ('outros_resultados_abrangentes',
                        'Outros Resultados Abrangentes'))

        for conta in contas:
            self.add_conta(ContaCredora(conta[0], conta[1]))

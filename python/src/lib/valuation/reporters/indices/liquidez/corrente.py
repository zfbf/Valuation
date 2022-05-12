import os
import numpy as np
from .indice_liquidez import IndiceLiquidezReporter


class IndiceLiquidezCorrenteReporter(IndiceLiquidezReporter):
    def __init__(self, valuation):
        super().__init__('Índice de Liquidez Corrente', 'liquidez_corrente',
                valuation)

    def get_indices(self, valuation, report):
        indices_liquidez = valuation.get_indices_liquidez(
                report['ano_inicial'],
                report['trimestre_inicial'],
                report['ano_final'],
                report['trimestre_final'])
        return indices_liquidez

    def get_tex_subdirectories(self):
        return ['indices', 'liquidez', 'corrente']
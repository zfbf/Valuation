import os
import numpy as np
from .indice_liquidez import IndiceLiquidezReporter


class IndiceLiquidezSecaReporter(IndiceLiquidezReporter):
    def __init__(self, valuation):
        super().__init__('Índice de Liquidez Seca', 'liquidez_seca', valuation)

    def get_indices(self, valuation, report):
        indices_liquidez = valuation.get_indices_liquidez(
                report['ano_inicial'],
                report['trimestre_inicial'],
                report['ano_final'],
                report['trimestre_final'])
        return indices_liquidez

    def get_tex_subdirectories(self):
        return ['indices', 'liquidez', 'seca']

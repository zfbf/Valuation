from datetime import date

from ..indice import Indice


class LiquidezImediata(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Imediata', valuation)

    # Disponibilidades / Passivo Circulante
    def get_valor(self, ano, trimestre):
        (periodo_contabil, bp) = (None, None)
        liquidez_imediata = None

        try:
            periodo_contabil = self.get_periodo_contabil(ano, trimestre)
            bp = super().get_periodo_contabil(ano, trimestre).bp_ifrs
            disponibilidades = bp.ativo.circulante.get_saldo_disponibilidades()
            passivo_circulante = bp.passivo.circulante
            liquidez_imediata = disponibilidades / passivo_circulante.get_saldo()
        except ZeroDivisionError as err:
            msg = 'ZeroDivisionError em LiquidezImediata'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tliquidez_imediata: {}'.format(liquidez_imediata)
            print(msg)
            #raise Exception(msg) from err
        except AttributeError as err:
            msg = 'AttributeError em LiquidezImediata'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tliquidez_imediata: {}'.format(liquidez_imediata)
            print(msg)
        except Exception as e:
            msg = 'Exception em LiquidezImediata'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tliquidez_imediata: {}'.format(liquidez_imediata)
            print(msg)
            raise Exception(msg) from e
        else:
            return liquidez_imediata

    def str_comp(self, ano, trimestre):
        pass

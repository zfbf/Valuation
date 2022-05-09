from datetime import date

from ..indice import Indice


class LiquidezCorrente(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Corrente', valuation)

    # (Ativo Circulante) / Passivo Circulante
    def get_valor(self, ano, trimestre):
        (periodo_contabil, bp, saldo_ac, saldo_pc) = (None, None, None, None)
        liquidez_corrente = None

        try:
            periodo_contabil = self.get_periodo_contabil(ano, trimestre)
            bp = self.get_periodo_contabil(ano, trimestre).bp_ifrs
            ativo_circulante = bp.ativo.circulante
            passivo_circulante = bp.passivo.circulante
            saldo_ac = ativo_circulante.get_saldo()
            saldo_pc = passivo_circulante.get_saldo()
            liquidez_corrente = saldo_ac / saldo_pc
        except ZeroDivisionError as err:
            msg = 'ZeroDivisionError em LiquidezCorrente'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tsaldo_ac: {}'.format(saldo_ac)
            msg += '\n\tsaldo_pc: {}'.format(saldo_pc)
            msg += '\n\tliquidez_corrente: {}'.format(liquidez_corrente)
            print(msg)
            raise Exception(msg) from err
        except AttributeError as err:
            msg = 'AttributeError em LiquidezCorrente'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tsaldo_ac: {}'.format(saldo_ac)
            msg += '\n\tsaldo_pc: {}'.format(saldo_pc)
            msg += '\n\tliquidez_corrente: {}'.format(liquidez_corrente)
            print(msg)
        except Exception as e:
            msg = 'Exception em LiquidezCorrente'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tsaldo_ac: {}'.format(saldo_ac)
            msg += '\n\tsaldo_pc: {}'.format(saldo_pc)
            msg += '\n\tliquidez_corrente: {}'.format(liquidez_corrente)
            print(msg)
            raise Exception(msg) from e
        else:
            return liquidez_corrente

    def str_comp(self, ano, trimestre):
        pass

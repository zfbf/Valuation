from ..indice import Indice


class LiquidezSeca(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Seca', valuation)

    # (Ativo Circulante - Estoques) / Passivo Circulante
    def get_valor(self, ano, trimestre):
        (periodo_contabil, bp) = (None, None)
        liquidez_seca = None

        try:
            periodo_contabil = self.get_periodo_contabil(ano, trimestre)
            bp = periodo_contabil.bp_ifrs
            ativo_circulante = bp.ativo.circulante
            saldo_estoques = ativo_circulante.get_saldo_estoques()
            passivo_circulante = bp.passivo.circulante
            liquidez_seca = ((ativo_circulante.get_saldo() - saldo_estoques) /
                    passivo_circulante.get_saldo())
        except ZeroDivisionError as err:
            msg = 'ZeroDivisionError em LiquidezSeca'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tliquidez_seca: {}'.format(liquidez_seca)
            print(msg)
            raise Exception(msg) from err
        except AttributeError as err:
            msg = 'AttributeError em LiquidezSeca'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tliquidez_seca: {}'.format(liquidez_seca)
            print(msg)
        except Exception as e:
            msg = 'Exception em LiquidezSeca'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tperiodo_contabil is None: {}'.format(
                    periodo_contabil is None)
            msg += '\n\tbp is None: {}'.format(bp is None)
            msg += '\n\tliquidez_seca: {}'.format(liquidez_seca)
            print(msg)
            raise Exception(msg) from e
        else:
            return liquidez_seca

    def str_comp(self, ano, trimestre):
        pass

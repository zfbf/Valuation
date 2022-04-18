from datetime import date

from ..indice import Indice


class LiquidezGeral(Indice):
    def __init__(self, valuation):
        super().__init__('Liquidez Geral', valuation)

    # (Ativo Circulante + Realizãvel a Longo Prazo) / Passivo
    def get_valor(self, ano, trimestre):
        (saldo_ac, saldo_rlp, saldo_pc, saldo_pnc) = (None, None, None, None)
        liquidez_geral = None

        try:
            periodo_contabil = self.get_periodo_contabil(ano, trimestre)
            ativo = periodo_contabil.bp_ifrs.ativo
            saldo_ac = ativo.circulante.get_saldo()
            saldo_rlp = ativo.nao_circulante.get_saldo_realizavel_a_longo_prazo()
            passivo = periodo_contabil.bp_ifrs.passivo
            saldo_pc = passivo.circulante.get_saldo()
            saldo_pnc = passivo.nao_circulante.get_saldo()
            liquidez_geral = ((saldo_ac + saldo_rlp) / (saldo_pc + saldo_pnc))
        except ZeroDivisionError as err:
            msg = 'ZeroDivisionError em LiquidezGeral'
            msg += '\n\tano: {}, trimestre: {}'.format(ano, trimestre)
            msg += '\n\tsaldo_ac: {}'.format(saldo_ac)
            msg += '\n\tsaldo_rlp: {}'.format(saldo_rlp)
            msg += '\n\tsaldo_pc: {}'.format(saldo_pc)
            msg += '\n\tsaldo_pnc: {}'.format(saldo_pnc)
            msg += '\n\tliquidez_geral: {}'.format(liquidez_geral)
            print(msg)
            raise err
        except Exception as e:
            msg = 'Exception em LiquidezGeral'
            print(msg)
            raise e
        else:
            return liquidez_geral

    def str_comp(self, ano, trimestre):
        pass

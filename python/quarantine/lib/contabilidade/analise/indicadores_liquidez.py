from ..plano_de_contas.grupo_contas import GrupoContas


class IndicadoresLiquidez():
    def __init__(self, plano_de_contas):
        super().__init__()
        self.pc = plano_de_contas

    def get_liquidez_imediata(self):
        saldo_disponibilidades = self.pc.ativo.circulante.get_saldo_disponibilidades()
        saldo_passivo_circulante = self.pc.passivo.circulante.get_saldo()
        li = saldo_disponibilidades / saldo_passivo_circulante
        return li

    def get_liquidez_seca(self):
        saldo_ativo_circulante = self.pc.ativo.circulante.get_saldo()
        saldo_estoques = self.pc.ativo.circulante.get_saldo_estoques()
        saldo_passivo_circulante = self.pc.passivo.circulante.get_saldo()
        ls = (saldo_ativo_circulante - saldo_estoques) / saldo_passivo_circulante

        print('\nliquidez_seca:')
        print('saldo_ativo_circulante: {:,.2f}'.format(saldo_ativo_circulante))
        print('saldo_estoques: {:,.2f}'.format(saldo_estoques))
        print('saldo_passivo_circulante: {:,.2f}'.format(saldo_passivo_circulante))
        print('ls: {:,.2f}'.format(ls))

        return ls

    def get_liquidez_corrente(self):
        saldo_ativo_circulante = self.pc.ativo.circulante.get_saldo()
        saldo_passivo_circulante = self.pc.passivo.circulante.get_saldo()
        liquidez_corrente = saldo_ativo_circulante / saldo_passivo_circulante
        return liquidez_corrente

    def get_liquidez_geral(self):
        saldo_ativo_circulante = self.pc.ativo.circulante.get_saldo()
        saldo_realizavel_a_longo_prazo = self.pc.ativo.nao_circulante \
                .get_conta_realizavel_a_longo_prazo().get_saldo()
        saldo_passivo_circulante = self.pc.passivo.circulante.get_saldo()
        saldo_passivo_nao_circulante = self.pc.passivo.nao_circulante.get_saldo()
        liquidez_geral = ((saldo_ativo_circulante + saldo_realizavel_a_longo_prazo)
                / (saldo_passivo_circulante + saldo_passivo_nao_circulante))

        print('\nliquidez_geral:')
        print('saldo_ativo_circulante: {:,.2f}'.format(saldo_ativo_circulante))
        print('saldo_realizavel_a_longo_prazo: {:,.2f}'.format(saldo_realizavel_a_longo_prazo))
        print('saldo_passivo_circulante: {:,.2f}'.format(saldo_passivo_circulante))
        print('saldo_passivo_nao_circulante: {:,.2f}'.format(saldo_passivo_nao_circulante))
        print('liquidez_geral: {:,.2f}'.format(liquidez_geral))

        return liquidez_geral

    def get_kanitz(self):
        pass

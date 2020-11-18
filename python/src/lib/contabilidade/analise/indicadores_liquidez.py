class IndicadoresLiquidez(Conta):
    def __init__(self, plano_de_contas):
        super().__init__()
        self.pc = plano_de_contas

    def get_liquidez_imediata(self):
        saldo_disponibilidades = 0

        for conta in self.pc.get_contas_disponibilidade():
            saldo_disponibilidades += conta.get_saldo()

        saldo_passivo_circulante = pc.passivo.circulante.get_saldo()
        li = disponibilidades / saldo_passivo_circulante
        return li

    def get_liquidez_seca(self):
        saldo_ativo_circulante = self.pc.ativo.circulante.get_saldo()
        saldo_estoques = self.pc.ativo.circulante.get_estoques()
        saldo_passivo_circulante = pc.passivo.circulante.get_saldo()
        ls = saldo_ativo_circulante - saldo_estoques / saldo_passivo_circulante
        return ls

    def get_liquidez_corrente(self):
        pass

    def get_liquidez_geral(self):
        pass

    def get_kanitz(self):
        pass

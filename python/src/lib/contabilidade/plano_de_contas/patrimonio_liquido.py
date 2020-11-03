from src.lib.contabilidade.grupo_contas import GrupoContas
from src.lib.contabilidade.conta import Conta


class PatrimonioLiquido(GrupoContas):
    def __init__(self):
        super().__init__('patrimonio_liquido', 'Patrimônio Líquido')
        # self.capital_social = GrupoContas('Capital Social')
        # self.reservas_de_capital = GrupoContas('Reservas de Capital')
        # self.ajustes_avaliacao_patrimonial = GrupoContas('Ajustes Avaliação Patrimonial')
        # self.reservas_de_lucro = GrupoContas('Reservas de Lucros')
        # self.prejuizos_acumulados = GrupoContas('Prejuízos Acumulados')

    def method_1(self):
        return 'method_1'


if __name__ == '__main__':
    patrimonio_liquido = PatrimonioLiquido()
    patrimonio_liquido.capital_social.add_conta(Conta('Capital Social', 1000))
    print(patrimonio_liquido)

from src.lib.contabilidade.grupo_contas import GrupoContas
from src.lib.contabilidade.conta import Conta


class Passivo(GrupoContas):
    def __init__(self):
        super().__init__('passivo', 'Passivo')
        self.circulante = GrupoContas('passivo_circulante', 'Circulante')
        self.nao_circulante = GrupoContas('passivo_nao_circulante', 'Não Circulante')

    def method_1(self):
        return 'method_1'




if __name__ == '__main__':
    conta_1 = Conta('Caixa', 10)
    conta_2 = Conta('Duplicatas', 20)
    print(conta)

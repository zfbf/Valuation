from src.lib.contabilidade.conta import Conta
from src.lib.contabilidade.grupo_contas import GrupoContas


class AtivoCirculante(GrupoContas):
    def __init__(self):
        super().__init__('ativo_circulante', 'Circulante')
        self.init_conta_caixa()

    def init_conta_caixa(self):
        self.add_conta(Conta('caixa', 'caixa'))

    def rename_conta_caixa(self, nome):
        self.get_conta('caixa').rename_conta(nome)




if __name__ == '__main__':
    ativo_circulante = AtivoCirculante()
    print(ativo_circulante)

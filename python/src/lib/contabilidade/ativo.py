from src.lib.contabilidade.grupo_contas import GrupoContas
from src.lib.contabilidade.ativo_circulante import AtivoCirculante
from src.lib.contabilidade.ativo_nao_circulante import AtivoNaoCirculante


class Ativo(GrupoContas):
    def __init__(self, total=None):
        super().__init__('ativo', 'Ativo', total)
        self.circulante = AtivoCirculante()
        self.add_conta(self.circulante)
        self.nao_circulante = AtivoNaoCirculante()
        self.add_conta(self.nao_circulante)




if __name__ == '__main__':
    ativo = Ativo(10)
    print(ativo)

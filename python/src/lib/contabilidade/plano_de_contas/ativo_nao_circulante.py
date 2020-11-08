from .grupo_contas import GrupoContas


class AtivoNaoCirculante(GrupoContas):
    def __init__(self, parent):
        super().__init__('ativo_nao_circulante', 'Não Circulante', parent)
        self.realizavel_longo_prazo = None




if __name__ == '__main__':
    ativo_nao_circulante = AtivoNaoCirculante()
    print(ativo_nao_circulante)

from src.lib.contabilidade.relatorios_contabeis.demonstrativo_financeiro import DemonstrativoFinanceiro
from src.lib.contabilidade.ativo import Ativo
from src.lib.contabilidade.passivo import Passivo
from src.lib.contabilidade.patrimonio_liquido import PatrimonioLiquido


#TODO Verificar se esta classe está sendo usada e caso não esteja remover
class BalancoPatrimonial(DemonstrativoFinanceiro):
    def __init__(self, ano):
        super().__init__(ano)
        self.ativo = Ativo()
        self.passivo = Passivo()
        self.patrimonio_liquido = PatrimonioLiquido()

    def add_ativo_circulante(self, codigos, nomes, valores):
        self.ativo.circulante.add_nomes_valores(codigos, nomes, valores)

    def add_ativo_nao_circulante(self, codigos, nomes, valores):
        self.ativo.nao_circulante.add_nomes_valores(codigos, nomes, valores)

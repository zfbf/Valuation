from .conta import Conta
from ..natureza import Natureza


class GrupoContas(Conta):
    def __init__(self, codigo, nome, natureza, parent=None):
        super().__init__(codigo, nome, natureza, parent)
        self.contas = []
        self.valor_verificacao = None

    def add_conta(self, conta):
        conta.parent = self
        self.contas.append(conta)

    def add_nomes_valores(self, codigos, nomes, valores):
        tuplas = list(zip(codigos, nomes, valores))

        for tupla in tuplas:
            self.add_conta(Conta(tupla[0], tupla[1], tupla[2]))

    def get_conta(self, codigo):
        founded = None

        if codigo.lower() == self.codigo.lower():
            founded = self
        else:
            for conta in self.contas:
                if conta.get_conta(codigo):
                    founded = conta.get_conta(codigo)

        return founded

    def get_saldo(self):
        saldo = self.get_total_debitos() - self.get_total_creditos()

        if self.is_natureza_credora():
            saldo = saldo * -1

        return saldo

    #TODO: Verificar se esse método ainda é usado
    def get_saldo_contas(self, contas):
        totais = {
            "debitos": 0,
            "creditos": 0
        }

        for conta in contas:
            self.set_totais_postorder(conta, totais)

        saldo = 0

        if self.is_natureza_devedora():
            saldo = totais['debitos'] - totais['creditos']
        else:
            saldo = totais['creditos'] - totais['debitos']

        return saldo

    #TODO: Este método precisa ser reverificado pois a lógica das
    #      contas faz com que os nós pais já sejam o resultado
    #      dos nós filhos de forma que somá-los provocaria
    #      uma conta dobrada.
    def set_totais_postorder(self, conta, totais):
        try:
            for child in conta.contas:
                self.set_totais_postorder(child, totais)
        except Exception:
            pass

        totais['debitos'] += conta.get_total_debitos()
        totais['creditos'] += conta.get_total_creditos()

    #
    # Por default, a utilização deste método é desabilitada
    # para promover a verificação de erros de digitação de
    # balanços fechados de empresas, porém em cenários de
    # simulação, pode-se redefinir este método para criar alguma
    # conta como Outros e fazer com que o valor do passivo se
    # ajuste a um determinado valor sem necessariamente modificar
    # os valores das outras contas componentes do grupo.
    #
    def set_saldo(self, saldo):
        raise TypeError()

    def increase_saldo(self, lancamento):
        raise TypeError()

    def decrease_saldo(self, lancamento):
        raise TypeError()

    def verificar_saldo(self):
        verificacao = False

        try:
            verificacao = self.is_saldo_equals(self.valor_verificacao)
        except TypeError:
            pass

        return verificacao

    def get_total_creditos(self):
        total_creditos = 0

        for conta in self.contas:
            total_creditos += conta.get_total_creditos()

        return total_creditos

    def get_total_debitos(self):
        total_debitos = 0

        for conta in self.contas:
            total_debitos += conta.get_total_debitos()

        return total_debitos

    def __str__(self):
        return self.str_indent()

    def str_indent(self, level=0):
        str = '\n{:s}{:s}: {:.2f}'.format('\t' * level, self.nome, self.get_saldo())
        str += '\t(valor para verificação: {})'.format(self.valor_verificacao)

        for conta in self.contas:
            str += '{}'.format(conta.str_indent(level + 1))

        return str

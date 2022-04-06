from .custo import Custo


class CustoTrimestral(Custo):
    def __init__(self, periodo_contabil):
        super().__init__(periodo_contabil)

    def get_trimestre(self):
        return self.periodo_contabil.trimestre

    # A ideia desse método é dar flexibilidade ao usuário
    # de usar os objetor que o convém sem provocar acoplamento.
    # Exemplo: Se o usuário desejar usar algum DataFrame, ele poderá
    # usar sem que essa classe tenha conhecimento deste objeto, bastando
    # que ele passe um objeto que tenha a interface report()
    def report(self, reporter):
        return reporter.execute(self)

    def str_comp(self):
        repr = '\n\ttrimestre: {}'.format(self.get_trimestre())
        return repr

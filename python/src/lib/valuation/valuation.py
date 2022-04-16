from abc import ABC, abstractmethod
from .indices.liquidez.geral import LiquidezGeral
from .indices.liquidez.corrente import LiquidezCorrente
from .indices.liquidez.seca import LiquidezSeca
from .indices.liquidez.imediata import LiquidezImediata
from .indices.atividade.prazo_medio_pagamento import PrazoMedioPagamento


class Valuation(ABC):
    def __init__(self, empresa):
        super().__init__()
        self.empresa = empresa
        self.periodos = []
        self.init()

    @abstractmethod
    def init(self):
        pass

    def get_empresa(self):
        return self.empresa

    def set_periodos(self, periodos):
        self.periodos = periodos

    def append_periodo(self, periodo):
        self.periodos.append(periodo)

    def get_periodos(self):
        return self.periodos

    def get_periodo(self, identificador):
        target = None

        for periodo in self.periodos:
            if periodo.identificador == identificador:
                target = periodo
                break

        return target

    def get_indices_liquidez(self, ano_inicial, trimestre_inicial,
            ano_final, trimestre_final):
        print('Dentro de get_indices_liquidez')
        liquidez_geral = LiquidezGeral(self)
        liquidez_corrente = LiquidezCorrente(self)
        liquidez_seca = LiquidezSeca(self)
        liquidez_imediata = LiquidezImediata(self)
        ano_array = []
        trimestre_array = []
        il_geral_array = []
        il_corrente_array = []
        il_seca_array = []
        il_imediata_array = []
        trimestre = trimestre_inicial

        for ano in range(ano_inicial, ano_final):
            #print('ano: {}'.format(ano))
            while trimestre <= 4:
                ano_array.append(ano)
                trimestre_array.append(trimestre)
                il_geral_array.append(liquidez_geral.get_valor(ano, trimestre))
                il_corrente_array.append(liquidez_corrente.get_valor(ano, trimestre))
                il_seca_array.append(liquidez_seca.get_valor(ano, trimestre))
                il_imediata_array.append(liquidez_imediata.get_valor(ano, trimestre))
                trimestre += 1

            trimestre = 1

        ano = ano_final
        print('ano: {}'.format(ano))

        for trimestre in range(1, trimestre_final + 1):
            ano_array.append(ano)
            trimestre_array.append(trimestre)
            il_geral_array.append(liquidez_geral.get_valor(ano, trimestre))
            il_corrente_array.append(liquidez_corrente.get_valor(ano, trimestre))
            il_seca_array.append(liquidez_seca.get_valor(ano, trimestre))
            il_imediata_array.append(liquidez_imediata.get_valor(ano, trimestre))

        keys = ['ano', 'trimestre', 'liquidez_geral', 'liquidez_corrente',
                'liquidez_seca', 'liquidez_Imediata']
        values = [ano_array, trimestre_array, il_geral_array, il_corrente_array,
                il_seca_array, il_imediata_array]
        indices_liquidez = dict(zip(keys, values))
        return indices_liquidez

    def get_indices_atividade(self, ano_inicial, trimestre_inicial,
            ano_final, trimestre_final):
        print('Dentro de get_indices_atividade')
        prazo_medio_pagamento = PrazoMedioPagamento(self)
        ano_array = []
        trimestre_array = []
        pmp_array = []
        trimestre = trimestre_inicial

        for ano in range(ano_inicial, ano_final):
            #print('ano: {}'.format(ano))
            while trimestre <= 4:
                ano_array.append(ano)
                trimestre_array.append(trimestre)
                pmp_array.append(prazo_medio_pagamento.get_valor(ano, trimestre))
                trimestre += 1

            trimestre = 1

        ano = ano_final
        print('ano: {}'.format(ano))

        for trimestre in range(1, trimestre_final + 1):
            ano_array.append(ano)
            trimestre_array.append(trimestre)
            pmp_array.append(prazo_medio_pagamento.get_valor(ano, trimestre))

        keys = ['ano', 'trimestre', 'prazo_medio_pagamento']
        values = [ano_array, trimestre_array, pmp_array]
        indices_atividade = dict(zip(keys, values))
        return indices_atividade

    # A ideia desse método é dar flexibilidade ao usuário
    # de usar os objetor que o convém sem provocar acoplamento.
    # Exemplo: Se o usuário desejar usar algum DataFrame, ele poderá
    # usar sem que essa classe tenha conhecimento deste objeto, bastando
    # que ele passe um objeto que tenha a interface report()
    def report(self, reporter):
        return reporter.execute(self)

    def __str__(self):
        repr = 'Valuation - {}'.format(self.get_empresa())
        repr += '\n\tTotal de períodos: {}'.format(len(self.get_periodos()))
        ultimo_periodo = self.periodos[-1]
        repr += '\n\tÚltimo período: {}'.format(ultimo_periodo.identificador)
        repr += '\n\t{}'.format(ultimo_periodo.bp_ifrs)
        repr += '\n\t{}'.format(ultimo_periodo.dre.lucro_liquido)
        return repr

from abc import ABC, abstractmethod

from .indices.liquidez.geral import LiquidezGeral
from .indices.liquidez.corrente import LiquidezCorrente
from .indices.liquidez.seca import LiquidezSeca
from .indices.liquidez.imediata import LiquidezImediata
from .indices.atividade.prazo_medio_estoques import PrazoMedioEstoques
from .indices.atividade.prazo_medio_recebimento import PrazoMedioRecebimento
from .indices.atividade.prazo_medio_pagamento import PrazoMedioPagamento
from .indices.rentabilidade.giro_ativo import GiroAtivo
from .indices.margem.bruta import MargemBruta
from .indices.margem.operacional import MargemOperacional
from .indices.margem.liquida import MargemLiquida


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
        #print('Dentro de get_indices_liquidez')
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

        for ano in range(ano_inicial, ano_final + 1):
            while ((ano < ano_final and trimestre <= 4) or
                   (ano == ano_final and trimestre <= trimestre_final)):
                il_geral = liquidez_geral.get_valor(ano, trimestre)
                il_corrente = liquidez_corrente.get_valor(ano, trimestre)
                il_seca = liquidez_seca.get_valor(ano, trimestre)
                il_imediata = liquidez_imediata.get_valor(ano, trimestre)
                ano_array.append(ano)
                trimestre_array.append(trimestre)
                il_geral_array.append(il_geral)
                il_corrente_array.append(il_corrente)
                il_seca_array.append(il_seca)
                il_imediata_array.append(il_imediata)
                trimestre += 1

            trimestre = 1

        keys = ['ano', 'trimestre', 'liquidez_geral', 'liquidez_corrente',
                'liquidez_seca', 'liquidez_imediata']
        values = [ano_array, trimestre_array, il_geral_array, il_corrente_array,
                  il_seca_array, il_imediata_array]
        indices_liquidez = dict(zip(keys, values))
        return indices_liquidez

    def get_indices_atividade(self, ano_inicial, trimestre_inicial,
            ano_final, trimestre_final):
        #print('Dentro de get_indices_atividade')
        prazo_medio_estoques = PrazoMedioEstoques(self)
        prazo_medio_recebimento = PrazoMedioRecebimento(self)
        prazo_medio_pagamento = PrazoMedioPagamento(self)
        ano_array = []
        trimestre_array = []
        pme_array = []
        pmr_array = []
        pmp_array = []
        cc_array = []
        trimestre = trimestre_inicial

        for ano in range(ano_inicial, ano_final + 1):
            while ((ano < ano_final and trimestre <= 4) or
                   (ano == ano_final and trimestre <= trimestre_final)):
                pme = prazo_medio_estoques.get_valor(ano, trimestre)
                pmr = prazo_medio_recebimento.get_valor(ano, trimestre)
                pmp = prazo_medio_pagamento.get_valor(ano, trimestre)
                cc = pme + pmr - pmp
                ano_array.append(ano)
                trimestre_array.append(trimestre)
                pme_array.append(pme)
                pmr_array.append(pmr)
                pmp_array.append(pmp)
                cc_array.append(cc)
                trimestre += 1

            trimestre = 1

        keys = ['ano', 'trimestre', 'prazo_medio_estoques',
                'prazo_medio_recebimento', 'prazo_medio_pagamento',
                'ciclo_de_caixa']
        values = [ano_array, trimestre_array, pme_array, pmr_array, pmp_array,
                  cc_array]
        indices_atividade = dict(zip(keys, values))
        return indices_atividade

    def get_indices_rentabilidade(self, ano_inicial, trimestre_inicial,
            ano_final, trimestre_final):
        #print('Dentro de get_indices_rentabilidade')
        giro_ativo = GiroAtivo(self)
        ano_array = []
        trimestre_array = []
        ga_array = []
        trimestre = trimestre_inicial

        for ano in range(ano_inicial, ano_final + 1):
            while ((ano < ano_final and trimestre <= 4) or
                   (ano == ano_final and trimestre <= trimestre_final)):
                ga = giro_ativo.get_valor(ano, trimestre)
                ano_array.append(ano)
                trimestre_array.append(trimestre)
                ga_array.append(ga)
                trimestre += 1

            trimestre = 1

        keys = ['ano', 'trimestre', 'giro_ativo']
        values = [ano_array, trimestre_array, ga_array]
        indices_rentabilidade = dict(zip(keys, values))
        return indices_rentabilidade

    def get_indices_margens(self, ano_inicial, trimestre_inicial,
            ano_final, trimestre_final):
        #print('Dentro de get_indices_margens')
        margem_bruta = MargemBruta(self)
        margem_operacional = MargemOperacional(self)
        margem_liquida = MargemLiquida(self)
        ano_array = []
        trimestre_array = []
        mb_array = []
        mo_array = []
        ml_array = []
        trimestre = trimestre_inicial

        for ano in range(ano_inicial, ano_final + 1):
            while ((ano < ano_final and trimestre <= 4) or
                   (ano == ano_final and trimestre <= trimestre_final)):
                mb = margem_bruta.get_valor(ano, trimestre)
                mo = margem_operacional.get_valor(ano, trimestre)
                ml = margem_liquida.get_valor(ano, trimestre)
                ano_array.append(ano)
                trimestre_array.append(trimestre)
                mb_array.append(mb)
                mo_array.append(mo)
                ml_array.append(ml)
                trimestre += 1

            trimestre = 1

        keys = ['ano', 'trimestre', 'margem_bruta', 'margem_operacional',
                'margem_liquida']
        values = [ano_array, trimestre_array, mb_array, mo_array, ml_array]
        indices_margens = dict(zip(keys, values))
        return indices_margens

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

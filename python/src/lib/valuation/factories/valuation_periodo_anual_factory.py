#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from .valuation_factory import ValuationFactory
from ...contabilidade.periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.ifrs.balanco_patrimonial import BalancoPatrimonialIFRS
from ...contabilidade.plano_de_contas.dre import DRE
from ...contabilidade.plano_de_contas.dfc import DFC
from .ativo_loader import AtivoIFRSLoader
from .ativo_circulante_loader import AtivoCirculanteIFRSLoader
from .ativo_nao_circulante_loader import AtivoNaoCirculanteIFRSLoader
from .passivo_circulante_loader import PassivoCirculanteIFRSLoader
from .passivo_nao_circulante_loader import PassivoNaoCirculanteIFRSLoader
from .patrimonio_liquido_loader import PatrimonioLiquidoIFRSLoader
from .dre_loader import DRELoader
from .dfc_loader import DFCLoader


class ValuationPeriodoAnualFactory(ValuationFactory):
    def __init__(self):
        super().__init__()

    def build(self, economatica_dados):
        valuation = ValuationDefault(economatica_dados.nome_empresa)

        for codigo_periodo in economatica_dados.get_codigos_periodos():
            periodo_cont = PeriodoContabil(codigo_periodo)
            valuation.append_periodo(periodo_cont)

        return valuation

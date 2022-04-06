from abc import ABC, abstractmethod

#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
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


class ValuationFactory(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def build(self, economatica_dados):
        pass
    
    def load(self, valuation, economatica_dados):
        a_loader = AtivoIFRSLoader()
        ac_loader = AtivoCirculanteIFRSLoader()
        anc_loader = AtivoNaoCirculanteIFRSLoader()
        pc_loader = PassivoCirculanteIFRSLoader()
        pnc_loader = PassivoNaoCirculanteIFRSLoader()
        pl_loader = PatrimonioLiquidoIFRSLoader()
        dre_loader = DRELoader()
        dfc_loader = DFCLoader()

        for periodo in valuation.get_periodos():
            identificador = periodo.identificador
            bp_ifrs = periodo.bp_ifrs
            a_loader.load(bp_ifrs.ativo, identificador, economatica_dados)
            ac_loader.load(bp_ifrs.ativo.circulante, identificador, economatica_dados)
            anc_loader.load(bp_ifrs.ativo.nao_circulante, identificador, economatica_dados)
            pc_loader.load(bp_ifrs.passivo.circulante, identificador, economatica_dados)
            pnc_loader.load(bp_ifrs.passivo.nao_circulante, identificador, economatica_dados)
            pl_loader.load(bp_ifrs.patrimonio_liquido, identificador, economatica_dados)
            dre = periodo.dre
            dre_loader.load(dre, identificador, economatica_dados)
            dfc = periodo.dfc
            dfc_loader.load(dfc, identificador, economatica_dados)

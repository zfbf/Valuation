#from ....importacao.economatica.iochpe_dados_anuais import IochpeDadosAnuais
from ..periodo_contabil import PeriodoContabil
from ..valuation_default import ValuationDefault
from ...contabilidade.plano_de_contas.default.balanco_patrimonial import BalancoPatrimonialDefault
from .ativo_circulante_loader import AtivoCirculanteDefaultLoader
from .ativo_nao_circulante_loader import AtivoNaoCirculanteDefaultLoader
from .passivo_circulante_loader import PassivoCirculanteDefaultLoader
from .passivo_nao_circulante_loader import PassivoNaoCirculanteDefaultLoader
from .patrimonio_liquido_loader import PatrimonioLiquidoDefaultLoader


class ValuationDefaultFactory():
    def __init__(self):
        super().__init__()
#        self.iochpe_da = IochpeDadosAnuais(2009, 2020)

    def build(self, economatica_dados):
        valuation = ValuationDefault(economatica_dados.nome_empresa)

        for periodo in economatica_dados.get_periodos():
            bp = BalancoPatrimonialDefault()
            valuation.append_periodo({
                'identificador': periodo,
                'bp': bp})

        return valuation

    def load(self, valuation, economatica_dados):
        ac_loader = AtivoCirculanteDefaultLoader()
        anc_loader = AtivoNaoCirculanteDefaultLoader()
        pc_loader = PassivoCirculanteDefaultLoader()
        pnc_loader = PassivoNaoCirculanteDefaultLoader()
        pl_loader = PatrimonioLiquidoDefaultLoader()

        for periodo in valuation.get_periodos():
            identificador = periodo['identificador']
            bp = periodo['bp']
            ac_loader.load(bp.ativo.circulante, identificador, economatica_dados)
            anc_loader.load(bp.ativo.nao_circulante, identificador, economatica_dados)
            pc_loader.load(bp.passivo.circulante, identificador, economatica_dados)
            pnc_loader.load(bp.passivo.nao_circulante, identificador, economatica_dados)
            pl_loader.load(bp.patrimonio_liquido, identificador, economatica_dados)

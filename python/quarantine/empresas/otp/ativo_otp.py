from lib.contabilidade.plano_de_contas.ativo import Ativo
from .ativo_circulante_otp import AtivoCirculanteOtp
from .ativo_nao_circulante_otp import AtivoNaoCirculanteOtp


class AtivoOtp(Ativo):
    def __init__(self):
        super().__init__()

    def build_ativo_circulante(self):
        return AtivoCirculanteOtp(self)

    def build_ativo_nao_circulante(self):
        return AtivoNaoCirculanteOtp(self)

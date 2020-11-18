from lib.contabilidade.plano_de_contas.passivo import Passivo
from .passivo_circulante_otp import PassivoCirculanteOtp
from .passivo_nao_circulante_otp import PassivoNaoCirculanteOtp


class PassivoOtp(Passivo):
    def __init__(self):
        super().__init__()

    def build_passivo_circulante(self):
        return PassivoCirculanteOtp(self)

    def build_passivo_nao_circulante(self):
        return PassivoNaoCirculanteOtp(self)

from abc import ABC, abstractmethod

from lib.contabilidade.plano_de_contas.plano_de_contas import PlanoDeContas
from .ativo_otp import AtivoOtp
from .passivo_otp import PassivoOtp
from .patrimonio_liquido_otp import PatrimonioLiquidoOtp


class PlanoDeContasOtp(PlanoDeContas):

    def build_ativo(self):
        self.ativo = AtivoOtp()

    def build_passivo(self):
        self.passivo = PassivoOtp()

    def build_patrimonio_liquido(self):
        self.patrimonio_liquido = PatrimonioLiquidoOtp()

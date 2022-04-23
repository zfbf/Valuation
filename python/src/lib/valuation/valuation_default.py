from .valuation import Valuation


class ValuationDefault(Valuation):
    def __init__(self, empresa, ticker):
        super().__init__(empresa, ticker)

    def init(self):
        pass
